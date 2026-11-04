#!/usr/bin/env python3
"""Chạy thử SQL what-if trên Spark cục bộ với bảng rỗng dựng từ danh mục feature.

Bắt lỗi cú pháp và lỗi phân giải cột/bảng trước khi đưa lên Databricks.
Cách dùng:
    pip install pyspark   # cần Java 17+
    python3 spark_check_whatif_sql.py --catalog playbook/core/whatif_chung/feature_catalog.csv FILE [FILE ...]
Tham số :ten được gán giá trị mẫu theo tên (chỉ để chạy thử, không phải số liệu).
"""
import argparse, csv, datetime, re, shutil, sys, tempfile
from collections import OrderedDict

PREFIX = 'tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.'
TYPES = {'string': 'STRING', 'bigint': 'BIGINT', 'int': 'INT', 'long': 'BIGINT', 'double': 'DOUBLE',
         'decimal': 'DECIMAL(38,4)', 'date': 'DATE', 'date (year month)': 'DATE'}


def blocks_from(path):
    txt = open(path, encoding='utf-8').read()
    if path.endswith('.md'):
        return [m.group(1) for m in re.finditer(r'```sql\s*\n(.*?)```', txt, flags=re.S)]
    return [txt]


SMOKE = False


def sample(name):
    if SMOKE and name == 'min_group_size':
        return 1
    if SMOKE and name == 'gso_list':
        return '1'
    if name == 'as_of_month':
        return datetime.date(2026, 10, 1)
    if name == 'as_of_date':
        return datetime.date(2026, 10, 31)
    if name == 'min_group_size':
        return 20
    if name in ('horizon_months', 'size_small', 'size_large'):
        return 2
    if name in ('min_paid_trigger', 'score_trigger'):
        return 1
    if name == 'dpd_days':
        return 0
    if re.search(r'(list|keyword|value|values|products)$', name):
        return 'x'
    return 0.3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--catalog', required=True)
    ap.add_argument('--smoke', action='store_true',
                    help='chèn 1 dòng giả (chuỗi "x", số 1, ngày theo kỳ mẫu) vào mỗi bảng để chạy thử cả phần tính toán')
    ap.add_argument('files', nargs='+')
    a = ap.parse_args()
    global SMOKE
    SMOKE = a.smoke
    from pyspark.sql import SparkSession
    tmp = tempfile.mkdtemp(prefix='whatif_spark_')
    spark = (SparkSession.builder.master('local[1]').appName('whatif-check')
             .config('spark.sql.warehouse.dir', tmp + '/wh')
             .config('spark.driver.extraJavaOptions', f'-Dderby.system.home={tmp}')
             .config('spark.ui.enabled', 'false').config('spark.ui.showConsoleProgress', 'false').config('spark.sql.ansi.enabled', 'true').getOrCreate())
    spark.sparkContext.setLogLevel('ERROR')
    tables = OrderedDict()
    for r in csv.DictReader(open(a.catalog, encoding='utf-8')):
        dt = r['data_type'].strip().lower()
        ty = dt.upper() if re.fullmatch(r'decimal\(\d+,\d+\)', dt) else TYPES.get(dt, 'STRING')
        tables.setdefault(r['table'], OrderedDict())[r['column']] = ty
    spark.sql('CREATE DATABASE IF NOT EXISTS ai_champion_trio')
    for t, cols in tables.items():
        ddl = ', '.join(f'`{c}` {ty}' for c, ty in cols.items())
        spark.sql(f'DROP TABLE IF EXISTS ai_champion_trio.{t}')
        spark.sql(f'CREATE TABLE ai_champion_trio.{t} ({ddl}) USING parquet')
        if a.smoke:
            # một dòng cho kỳ hiện tại và hai kỳ lịch sử, để chạy được truy vấn nhiều tháng
            for m in ('2026-10-01', '2026-08-01', '2026-07-01'):
                vals = []
                for c, ty in cols.items():
                    if ty == 'DATE':
                        vals.append(f"DATE'{m}'" if c in ('month', 'month_id') else "DATE'2026-10-31'")
                    elif ty == 'STRING' and c not in ('gso_code',):
                        vals.append("'x'")
                    elif 'dpd' in c:
                        vals.append(f'CAST(0 AS {ty})')   # khách chưa quá hạn, để các bộ lọc "chưa quá hạn" có dòng
                    else:
                        vals.append(f'CAST(1 AS {ty})')
                spark.sql(f'INSERT INTO ai_champion_trio.{t} VALUES ({", ".join(vals)})')
                if not any(ty == 'DATE' and c in ('month', 'month_id') for c, ty in cols.items()):
                    break
    bad = 0
    for f in a.files:
        for bi, blk in enumerate(blocks_from(f), 1):
            body = re.sub(r'--[^\n]*', '', blk).replace(PREFIX, 'ai_champion_trio.')
            for si, stmt in enumerate([s for s in body.split(';') if s.strip()], 1):
                if not re.match(r'\s*(SELECT|WITH)\b', stmt, flags=re.I):
                    print(f'BỎ  {f} [khối {bi}, câu {si}]: đoạn CTE minh họa, không phải câu hoàn chỉnh')
                    continue
                names = sorted(set(re.findall(r'(?<![:\w]):([a-zA-Z_]\w*)', stmt)))
                try:
                    rows = spark.sql(stmt, args={n: sample(n) for n in names}).collect()
                    print(f'OK   {f} [khối {bi}, câu {si}]' + (f' – {len(rows)} dòng' if a.smoke else ''))
                except Exception as e:
                    bad += 1
                    msg = str(e).strip().splitlines()[0][:300]
                    print(f'LỖI  {f} [khối {bi}, câu {si}]: {msg}')
    spark.stop()
    shutil.rmtree(tmp, ignore_errors=True)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
