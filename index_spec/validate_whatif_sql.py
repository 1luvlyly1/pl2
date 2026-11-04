#!/usr/bin/env python3
"""Kiểm tra SQL what-if theo danh mục feature.

Cách dùng:
    python3 validate_whatif_sql.py --catalog playbook/core/whatif_chung/feature_catalog.csv FILE [FILE ...]
FILE là .sql hoặc .md (lấy các khối ```sql). Thoát mã 1 nếu có lỗi.

Quy ước được kiểm (playbook/whatif/wc_04_sql.md):
- Bảng gốc viết đầy đủ ...ai_champion_trio.<bảng> kèm bí danh; cột bảng gốc viết bí_danh.cột.
- Mọi (bảng, cột) phải có trong danh mục; cột bị chặn → lỗi; cột cờ trống/0 → cảnh báo cần xác nhận.
- Chỉ SELECT/WITH; câu SELECT cuối không trả khóa khách hàng.
Giới hạn: không phân tích cú pháp đầy đủ; cột viết không có bí danh chỉ được cảnh báo.
"""
import argparse, csv, re, sys
from collections import defaultdict

SCHEMA = 'ai_champion_trio'
BLOCKED = {('cus_coll_transformed', 'ds_parition_date'), ('cus_coll_transformed', 'td_mm_current_balance')}
KEY_COLS = {'customer_code', 'cusid', 'cus_key', 'company_code', 'coll_id'}
DML = r'\b(INSERT|UPDATE|DELETE|MERGE|CREATE|DROP|ALTER|TRUNCATE|GRANT|REPLACE\s+TABLE)\b'
SQL_KW = {'where', 'join', 'left', 'right', 'inner', 'full', 'cross', 'on', 'group', 'order', 'limit',
          'union', 'having', 'lateral', 'window', 'as'}


def load_catalog(path):
    cat = defaultdict(dict)
    for r in csv.DictReader(open(path, encoding='utf-8')):
        cat[r['table']][r['column']] = r
    return cat


def strip_sql(s):
    s = re.sub(r'/\*.*?\*/', ' ', s, flags=re.S)
    s = re.sub(r'--[^\n]*', ' ', s)
    s = re.sub(r"'(?:[^'\\]|\\.)*'", "''", s)
    return s


def blocks_from(path):
    txt = open(path, encoding='utf-8').read()
    if path.endswith('.md'):
        return [m.group(1) for m in re.finditer(r'```sql\s*\n(.*?)```', txt, flags=re.S)]
    return [txt]


def strip_count_calls(sel):
    """Bỏ các lời gọi COUNT(...)/APPROX_COUNT_DISTINCT(...) – khóa nằm trong hàm đếm là đã gộp."""
    out, i = [], 0
    pat = re.compile(r'\b(COUNT|APPROX_COUNT_DISTINCT)\s*\(', re.I)
    while True:
        m = pat.search(sel, i)
        if not m:
            out.append(sel[i:])
            return ''.join(out)
        out.append(sel[i:m.start()])
        j, depth = m.end(), 1
        while j < len(sel) and depth:
            depth += {'(': 1, ')': -1}.get(sel[j], 0)
            j += 1
        out.append(' ')
        i = j


def final_select_list(stmt):
    depth, last, i = 0, None, 0
    up = stmt.upper()
    while i < len(stmt):
        c = stmt[i]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        elif depth == 0 and up.startswith('SELECT', i) and (i == 0 or not stmt[i-1].isalnum()):
            last = i
        i += 1
    if last is None:
        return ''
    depth, j = 0, last + 6
    while j < len(stmt):
        c = stmt[j]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        elif depth == 0 and re.match(r'\bFROM\b', up[j:j+5]) and not stmt[j-1].isalnum():
            return stmt[last+6:j]
        j += 1
    return stmt[last+6:]


def check(path, cat, all_cols):
    errs, warns, params = [], [], set()
    for bi, raw in enumerate(blocks_from(path), 1):
        s = strip_sql(raw)
        tag = f'{path} [khối {bi}]'
        if re.search(DML, s, flags=re.I):
            errs.append(f'{tag}: có lệnh ghi/sửa – chỉ được SELECT/WITH')
        params |= set(re.findall(r'(?<![:\w]):([a-zA-Z_]\w*)', s))
        for stmt in [x for x in s.split(';') if x.strip()]:
            alias = {}
            for m in re.finditer(SCHEMA + r'\.(\w+)(?:\s+(?:AS\s+)?(\w+))?', stmt, flags=re.I):
                t, a = m.group(1), m.group(2)
                if t not in cat:
                    errs.append(f'{tag}: bảng `{t}` không có trong danh mục')
                    continue
                if not a or a.lower() in SQL_KW:
                    errs.append(f'{tag}: bảng `{t}` thiếu bí danh')
                    continue
                if a in alias and alias[a] != t:
                    errs.append(f'{tag}: bí danh `{a}` dùng cho hai bảng `{alias[a]}` và `{t}` trong cùng câu')
                alias[a] = t
            for m in re.finditer(r'(?<![\w.])(\w+)\.(\w+)\b(?!\s*\()', stmt):
                a, col = m.group(1), m.group(2)
                if a not in alias:
                    continue
                t = alias[a]
                if (t, col) in BLOCKED:
                    errs.append(f'{tag}: `{t}.{col}` bị chặn (nghi nhầm bảng/sai chính tả)')
                elif col not in cat[t]:
                    errs.append(f'{tag}: `{t}.{col}` không có trong danh mục')
                else:
                    f = cat[t][col]['flag']
                    if f != '1' and col not in KEY_COLS and cat[t][col]['group'] not in ('key', 'timekey'):
                        warns.append(f'{tag}: `{t}.{col}` cờ {"trống" if f == "" else f} – cần xác nhận')
            if alias:
                bare = set(re.findall(r'(?<![\w.:])([a-z_][a-z0-9_]*)\b(?!\s*[.(])', stmt)) & all_cols
                derived = set(re.findall(r'\bAS\s+(\w+)', stmt, flags=re.I)) | set(
                    re.findall(r'(\w+)\s+AS\s*\(', stmt, flags=re.I))
                for b in sorted(bare - derived - {'month', 'age', 'gender', 'sector'}):
                    warns.append(f'{tag}: `{b}` trùng tên cột danh mục nhưng không có bí danh – kiểm tra')
                for a, t in alias.items():
                    if t.startswith('trio_') and not re.search(rf'\b{a}\.month\b', stmt):
                        warns.append(f'{tag}: bảng `{t}` (bí danh `{a}`) không lọc `month`')
                sel = strip_count_calls(final_select_list(stmt))
                for k in KEY_COLS:
                    if re.search(rf'\b{k}\b', sel):
                        errs.append(f'{tag}: câu SELECT cuối trả khóa `{k}` – phải gộp nhóm')
                if stmt.strip().upper().startswith('WITH') and 'min_group_size' not in stmt:
                    warns.append(f'{tag}: truy vấn chính thiếu HAVING COUNT(*) >= :min_group_size')
    return errs, sorted(set(warns)), sorted(params)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--catalog', required=True)
    ap.add_argument('files', nargs='+')
    a = ap.parse_args()
    cat = load_catalog(a.catalog)
    all_cols = {c for t in cat for c in cat[t]}
    bad = 0
    for f in a.files:
        e, w, p = check(f, cat, all_cols)
        print(f'== {f}: {len(e)} lỗi, {len(w)} cảnh báo, {len(p)} tham số')
        for x in e:
            print('  LỖI     ', x)
        for x in w:
            print('  CẢNH BÁO', x)
        if p:
            print('  Tham số:', ', '.join(':' + x for x in p))
        bad += len(e)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
