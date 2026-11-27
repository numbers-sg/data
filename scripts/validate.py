#!/usr/bin/env python3
"""Check every dataset before it is trusted: run on each push and pull request (.github/workflows/validate.yml).

For each dataset in index.json: the CSV header equals the JSON field list; the CSV, the JSON and index.json agree on
the row count; every value parses as its field's type (number, integer, date YYYY-MM-DD, month YYYY-MM, url);
fields not marked nullable are never empty; no two rows are identical. Exits 1 and lists every problem it finds.
Standard library only.
"""
import csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = {
    'number': lambda v: re.fullmatch(r'-?\d+(\.\d+)?([eE][-+]?\d+)?', v),
    'integer': lambda v: re.fullmatch(r'-?\d+', v),
    'date': lambda v: re.fullmatch(r'\d{4}-\d{2}-\d{2}', v),
    'month': lambda v: re.fullmatch(r'\d{4}-\d{2}', v),
    'url': lambda v: v.startswith('https://') or v.startswith('http://'),
    'string': lambda v: True,
}


def main():
    idx = json.load(open(os.path.join(ROOT, 'index.json'), encoding='utf-8'))['datasets']
    problems, rows_total = [], 0
    for d in idx:
        i = d['id']
        j = json.load(open(os.path.join(ROOT, f'datasets/{i}/{i}.json'), encoding='utf-8'))
        with open(os.path.join(ROOT, f'datasets/{i}/{i}.csv'), encoding='utf-8', newline='') as f:
            table = list(csv.reader(f))
        fields = j['fields']
        names = [x['name'] for x in fields]
        if not table or table[0] != names:
            problems.append(f'{i}: CSV header does not match the field list')
            continue
        body = table[1:]
        if not (len(body) == len(j['data']) == d['rows']):
            problems.append(f'{i}: row counts differ (CSV {len(body)}, JSON {len(j["data"])}, index {d["rows"]})')
        seen = set()
        for n, row in enumerate(body, 2):
            if len(row) != len(names):
                problems.append(f'{i} line {n}: {len(row)} cells, expected {len(names)}')
                continue
            t = tuple(row)
            if t in seen:
                problems.append(f'{i} line {n}: duplicate row')
            seen.add(t)
            for f, v in zip(fields, row):
                if v == '':
                    if not f.get('nullable'):
                        problems.append(f'{i} line {n}: {f["name"]} is empty but not nullable')
                elif not CHECK.get(f['type'], CHECK['string'])(v):
                    problems.append(f'{i} line {n}: {f["name"]}={v!r} is not a valid {f["type"]}')
        rows_total += len(body)
    for p in problems[:200]:
        print('PROBLEM', p)
    print(f'{len(idx)} datasets, {rows_total:,} rows, {len(problems)} problems')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
