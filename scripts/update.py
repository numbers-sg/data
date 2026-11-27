#!/usr/bin/env python3
"""Rebuild this repository from the Numbers.sg data API (https://numbers.sg/developers/).

Mirrors every dataset whose sources all grant reuse in writing ("open" in the API's meta.licence.reuse). Writes, per
dataset, datasets/<id>/<id>.csv, <id>.json and README.md, then the root README, index.json, datapackage.json and
CITATION.cff. Everything is generated from the API: nothing here is typed by hand, so counts and dates heal themselves.

A file changes only when the dataset's rows change (meta.hash), so the nightly workflow commits only real changes.
Standard library only. Usage: python3 scripts/update.py [--check]   (--check: report what would change, write nothing)
"""
import csv, io, json, os, re, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta

API = 'https://numbers.sg/api/v1/'
REPO = 'https://github.com/numbers-sg/data'
_Z = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'zenodo.json')
DOI = json.load(open(_Z)).get('concept_doi') if os.path.exists(_Z) else None  # the concept DOI: always resolves to the newest archived version
RAW = 'https://raw.githubusercontent.com/numbers-sg/data/main/'
UA = 'numbers-sg-data-mirror/1.0 (+https://github.com/numbers-sg/data)'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SGT = timezone(timedelta(hours=8))
TODAY = datetime.now(SGT).strftime('%Y-%m-%d')
CHECK = '--check' in sys.argv


def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'identity'})
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read().decode('utf-8')
            time.sleep(0.4)  # well under the API's limit of 60 requests per 10 seconds
            return body
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503, 504) and i < tries - 1:
                time.sleep(12 * (i + 1))
                continue
            raise
        except urllib.error.URLError:
            if i < tries - 1:
                time.sleep(12 * (i + 1))
                continue
            raise


def write(path, text):
    """Write only when the text differs; return True when it did (or would, with --check)."""
    full = os.path.join(ROOT, path)
    old = open(full, encoding='utf-8').read() if os.path.exists(full) else None
    if old == text:
        return False
    if not CHECK:
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
    return True


def md(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')


def nice_date(d):
    """2026-11-26 -> 26 Nov 2026; 2026-11 -> Nov 2026; anything else as it is."""
    for fmt, out in (('%Y-%m-%d', '%-d %b %Y'), ('%Y-%m', '%b %Y')):
        try:
            return datetime.strptime(str(d), fmt).strftime(out)
        except ValueError:
            pass
    return str(d) if d else ''


TYPES = {'date': ('date', 'string'), 'month': ('yearmonth', 'string'), 'quarter': ('string', 'string'), 'year': ('year', 'integer'),
         'integer': ('integer', 'integer'), 'number': ('number', 'number'), 'string': ('string', 'string'), 'boolean': ('boolean', 'boolean')}
TOPICS = [  # (id prefix, group heading, phrase for the intro): only groups with a mirrored dataset are shown
    (('sora', 'tbill', 'ssb'), 'Interest rates and government bonds', 'interest rates and government bonds (SORA, T-bills, Singapore Savings Bonds)'),
    (('coe',), 'Cars', 'COE bidding results'),
    (('cpf',), 'CPF', 'CPF figures'),
    (('income-tax', 'tax-', 'stamp', 'bsd', 'absd'), 'Tax', 'income tax rates'),
    (('inflation', 'cpi', 'electricity'), 'Prices', 'inflation'),
    (('fx-',), 'Exchange rates', 'exchange rates for the Singapore dollar'),
]


def topic(i):
    for n, (pre, head, phrase) in enumerate(TOPICS):
        if i.startswith(pre):
            return n
    return len(TOPICS)


def topics_phrase(mirrored):
    ph = [TOPICS[n][2] for n in sorted({topic(d['id']) for d in mirrored}) if n < len(TOPICS)]
    return ph[0] if len(ph) == 1 else ', '.join(ph[:-1]) + ' and ' + ph[-1]


def covers(d):
    return f"{nice_date(d['from'])} to {nice_date(d['to'])}" if d.get('from') else 'Today’s figures (not a time series)'


NULLS = {'not_published': 'the source gave no figure', 'not_applicable': 'it does not apply to that row', 'not_yet': 'not out yet',
         'source_unreadable': 'we could not read the source that day'}


def main():
    cat = json.loads(get(API))
    prev = {}
    if os.path.exists(os.path.join(ROOT, 'index.json')):
        prev = {d['id']: d for d in json.load(open(os.path.join(ROOT, 'index.json'), encoding='utf-8'))['datasets']}
    mirrored, skipped, changed, all_fixes = [], [], [], []
    for item in sorted(cat['data'], key=lambda x: x['id']):
        if item.get('reuse') != 'open':
            skipped.append(item)
            continue
        i = item['id']
        full = json.loads(get(API + i + '/history'))
        m, rows = full['meta'], full['data']
        csv_text = get(API + i + '.csv')
        fixes = [c for c in json.loads(get(API + i + '/changes'))['data'] if c.get('type') == 'correction']
        all_fixes.extend((c['date'], c['text'], i, m['title']) for c in fixes)
        p = prev.get(i, {})
        same = p.get('hash') == m['hash']
        updated = p['updated'] if same and p.get('updated') else TODAY  # the day the rows last changed here
        notices = [re.sub(r'accessed on \d{4}-\d{2}-\d{2}', 'accessed on ' + updated, n) for n in m['attribution'].get('notices', [])]
        cov = m.get('coverage') or {}
        rec = {
            'id': i, 'title': m['title'], 'question': m.get('question'), 'rows': len(rows), 'from': cov.get('from'), 'to': cov.get('to'),
            'hash': m['hash'], 'updated': updated, 'page_url': m['page_url'], 'api': API + i,
            'sources': [s['publisher'] for s in m['sources']],
        }
        doc = {
            'dataset': i, 'title': m['title'], 'description': m.get('description'), 'question': m.get('question'), 'row': m.get('row'),
            'coverage': cov, 'fields': m['fields'], 'sources': m['sources'],
            'licence': {'name': m['licence']['name'], 'url': m['licence']['url'], 'terms_page': m['licence']['terms_page']},
            'attribution': {'text': m['attribution']['text'], 'notices': notices},
            'page_url': m['page_url'], 'method': m.get('method', {}).get('notes'), 'api': API + i, 'hash': m['hash'],
            'rows_updated': updated, 'data': rows,
        }
        a = write(f'datasets/{i}/{i}.csv', csv_text if csv_text.endswith('\n') else csv_text + '\n')
        b = write(f'datasets/{i}/{i}.json', json.dumps(doc, ensure_ascii=False, indent=1) + '\n')
        c = write(f'datasets/{i}/README.md', dataset_readme(m, rec, notices, rows, fixes))
        if a or b or c:
            changed.append(i)
        mirrored.append(rec)
    write('index.json', json.dumps({'source': API, 'licence': 'CC BY 4.0', 'datasets': mirrored}, ensure_ascii=False, indent=1) + '\n')
    write('datapackage.json', datapackage(mirrored))
    write('README.md', root_readme(mirrored, skipped, all_fixes))
    write('CITATION.cff', citation(mirrored))
    print(('Would change: ' if CHECK else 'Changed: ') + (', '.join(changed) if changed else 'nothing'))
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            f.write('changed=' + ' '.join(changed) + '\n')


def first_sentence(s):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z])', s, maxsplit=1)[0]


def fix_text(s):
    return re.sub(r'^(Correction|Corrected)\s*:\s*', '', s.strip(), flags=re.I)


def dataset_readme(m, rec, notices, rows, fixes):
    i = rec['id']
    ch = m.get('chart') or {}
    chart = f"[![Chart of {md(m['title'])}, from Numbers.sg]({ch['url']})]({m['page_url']})\n\n" if ch.get('url') else ''
    if fixes:
        fx = 'Each mistake found in this dataset or on its page, newest first. The same list is on [numbers.sg/corrections](https://numbers.sg/corrections/).\n\n' + '\n'.join(f'- **{nice_date(c["date"])}:** {md(fix_text(c["text"]))}' for c in sorted(fixes, key=lambda c: c['date'], reverse=True))
    else:
        fx = 'None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).'
    fx += f'\n\nFound a wrong number? [Report it]({REPO}/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.'
    fields = '\n'.join(
        '| `{}` | {} | {}{}{} |'.format(
            f['name'], f['type'], md(f['meaning']), f' Unit: {md(f["unit"])}.' if f.get('unit') else '',
            (' Empty when ' + ' or '.join(NULLS.get(r, r.replace('_', ' ')) for r in f.get('null_reasons', [])) + '.') if f.get('nullable') and f.get('null_reasons') else '')
        for f in m['fields'])
    src = '\n'.join(f'- [{s["publisher"]}]({s["url"]}), under the [{s["terms"]}]({s["terms_url"]})' for s in m['sources'])
    note = ('\n\nThe publishers ask for this notice wherever you use their figures. Copy it as it is:\n\n' + '\n\n'.join('> ' + n for n in notices)) if notices else ''
    last = rows[-1] if rows else {}
    sample = '\n'.join(f'| `{k}` | {md(v) if v is not None else "(empty)"} |' for k, v in last.items())
    year = rec['updated'][:4]
    return f'''# {m['title']}

{chart}{m.get('description') or ''}

**The question it answers:** {m.get('question') or ''}

| | |
|---|---|
| Rows | {rec['rows']:,} |
| Each row | {md(m['row']['is']) if isinstance(m.get('row'), dict) else ''} |
| Covers | {covers(rec)} |
| Rows last changed here | {nice_date(rec['updated'])} |
| Source | {', '.join(md(s) for s in rec['sources'])} |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [{m['page_url'].replace('https://', '')}]({m['page_url']}) |

## Download

- CSV: [`{i}.csv`]({i}.csv) · raw: `{RAW}datasets/{i}/{i}.csv`
- JSON, with the field list, sources and notices: [`{i}.json`]({i}.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `{API}{i}` (newest rows), `{API}{i}/history` (every row), `{API}{i}.csv`

```python
import pandas as pd
df = pd.read_csv("{RAW}datasets/{i}/{i}.csv")
```

```r
df <- read.csv("{RAW}datasets/{i}/{i}.csv")
```

In Google Sheets: `=IMPORTDATA("{API}{i}.csv")`

## The last row

| Field | Value |
|---|---|
{sample}

## Fields

| Field | Type | Meaning |
|---|---|---|
{fields}

## Where the numbers come from

{src}

How each figure is read and checked: [{m['page_url'].replace('https://', '')}#method]({m.get('method', {}).get('notes') or m['page_url']}). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`{API}{i}/changes.atom`]({API}{i}/changes.atom).

## Corrections

{fx}

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> {m['attribution']['text']}{note}

To cite it:

```
Numbers.sg ({year}). {m['title']} [Data set]. {m['page_url']}{(chr(10) + 'Part of: Say, J. (' + year + '). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/' + DOI) if DOI else ''}
```

```bibtex
@misc{{numberssg_{i.replace('-', '_')},
  author = {{{{Numbers.sg}}}},
  title = {{{{{m['title']}}}}},
  year = {{{year}}},
  howpublished = {{\\url{{{m['page_url']}}}}},
  note = {{Rows last changed {rec['updated']}; CC BY 4.0{('; archived in https://doi.org/' + DOI) if DOI else ''}}}
}}
```

For a copy that never changes, cite the API's dated copy: `{API}{i}/as-of/YYYY-MM-DD`.
'''


def root_readme(mirrored, skipped, all_fixes):
    total = sum(d['rows'] for d in mirrored)
    oldest = min((d for d in mirrored if d['from']), key=lambda d: str(d['from']))
    newest = max(d['updated'] for d in mirrored)
    groups = []
    for n in sorted({topic(d['id']) for d in mirrored}):
        rows = '\n'.join(
            f'| [{md(d["title"])}](datasets/{d["id"]}/) | `{d["id"]}` | {d["rows"]:,} | {covers(d)} | {nice_date(d["updated"])} |'
            for d in sorted((d for d in mirrored if topic(d['id']) == n), key=lambda d: d['title'].lower()))
        groups.append(f"### {TOPICS[n][1] if n < len(TOPICS) else 'Other'}\n\n| Dataset | Id | Rows | Covers | Rows last changed |\n|---|---|---:|---|---|\n{rows}")
    table = '\n\n'.join(groups)
    ex = next((d for d in mirrored if d['id'] == 'sora'), mirrored[0])
    credit = json.load(open(os.path.join(ROOT, f"datasets/{ex['id']}/{ex['id']}.json"), encoding='utf-8'))['attribution']['text']
    seen, recent = set(), []
    for c in sorted(all_fixes, key=lambda c: c[0], reverse=True):  # daily and monthly copies of one page share a correction: list it once
        if c[1] not in seen:
            seen.add(c[1]); recent.append(c)
    fixlist = '\n'.join(f'- **{nice_date(c[0])}**, [{md(c[3])}](datasets/{c[2]}/#corrections): {md(first_sentence(fix_text(c[1])))}' for c in recent[:5])
    badges = ' '.join([
        f'[![Data checks]({REPO}/actions/workflows/validate.yml/badge.svg)]({REPO}/actions/workflows/validate.yml)',
        '[![Licence: CC BY 4.0](https://img.shields.io/badge/licence-CC_BY_4.0-13233A)](LICENSE)',
        *([f'[![DOI](https://zenodo.org/badge/DOI/{DOI}.svg)](https://doi.org/{DOI})'] if DOI else []),
        f'![{len(mirrored)} datasets](https://img.shields.io/badge/datasets-{len(mirrored)}-13233A)',
        f'![{total:,} rows](https://img.shields.io/badge/rows-{total:,}-13233A)',
        f'![Rows last changed {newest}](https://img.shields.io/badge/rows_last_changed-{newest.replace("-", "--")}-13233A)',
    ])
    facts = '\n'.join(f'- {md(d["title"])}: [`{API}{d["id"]}`]({API}{d["id"]})' for d in sorted(skipped, key=lambda d: d['title'].lower()))
    return f'''# Singapore rates and prices: open data from Numbers.sg

{badges}

{len(mirrored)} datasets of Singapore {topics_phrase(mirrored)}, as CSV and JSON. Each is read from the agency or bank that publishes it, checked against the page it appears on, and free to use under [CC BY 4.0](LICENSE).

{total:,} rows in all, the oldest from {nice_date(oldest['from'])} ({md(oldest['title'])}). Rows last changed here on {nice_date(newest)}.

This repository is a copy of the [Numbers.sg data API](https://numbers.sg/developers/), refreshed every night at 00:20 Singapore time and committed only when the rows change. For the freshest numbers, use the API: it is free and needs no key, and every answer says when we last read the source.

## Who checks these numbers

Numbers.sg is edited by [Jeremiah Say](https://numbers.sg/about/jeremiah-say/) and published by [Numbers Publishing Pte. Ltd.](https://numbers.sg/company/), a Singapore company. Every figure here goes through the same checks as the page it comes from:

1. **Read from the source.** A scheduled job reads each figure from the agency or bank that publishes it. Figures that change rarely are kept by hand and re-read on a booked date, listed on the [update schedule](https://numbers.sg/update-schedule/).
2. **Matched every night.** Before the nightly copy is saved, a job compares each dataset with the table on its own page, cell by cell.
3. **Checked again here.** Every commit to this repository runs [`scripts/validate.py`](scripts/validate.py): headers, row counts, types, empty values and duplicate rows. The nightly update won't commit a copy that fails it.
4. **Corrected in the open.** Each mistake is listed with its date and what changed, in the dataset's README and on [numbers.sg/corrections](https://numbers.sg/corrections/).

How each dataset is read is set out on its page, under "How we get these numbers", and the overall method at [numbers.sg/how-we-get-our-numbers](https://numbers.sg/how-we-get-our-numbers/). Numbers.sg is independent: none of it is part of, endorsed by or paid by the Singapore Government or any of its agencies, it is not part of any bank, and no one pays for a figure, a ranking or a place on a page.

## Recent corrections

{fixlist}

Every correction: [numbers.sg/corrections](https://numbers.sg/corrections/). Found a wrong number? [Report it]({REPO}/issues/new?template=wrong-number.yml).

## Datasets

{table}

Each folder has the CSV, a JSON copy with the field list and sources, and a README with every field's meaning, the sources and their terms, and how to cite it.

## Quick start

```python
import pandas as pd
sora = pd.read_csv("{RAW}datasets/sora/sora.csv")
```

```r
sora <- read.csv("{RAW}datasets/sora/sora.csv")
```

```bash
curl -s {API}sora            # the newest rows, as JSON
curl -s {API}sora.csv        # every row, as CSV
```

Google Sheets: `=IMPORTDATA("{API}coe-results.csv")` gives a table that refreshes itself.

[`index.json`](index.json) lists every dataset with its rows, dates and hash. [`datapackage.json`](datapackage.json) describes the CSVs in the [Frictionless](https://frictionlessdata.io/) standard, so `frictionless` and pandas read them with their types.

## Freshness and changes

- The API reads each source on its own schedule, as often as every 10 minutes on COE results days. The [update schedule](https://numbers.sg/update-schedule/) lists each one.
- Every API answer says when we last read the source (`meta.checked_at`) and whether that read is late (`meta.stale`).
- Follow every change in a feed reader: [`{API}changes.atom`]({API}changes.atom) (JSON Feed: [`changes.json`]({API}changes.json)).
- Mistakes are fixed in the open, with the date and what changed, on [numbers.sg/corrections](https://numbers.sg/corrections/).

## Licence and credit

Free to use, in apps, research, articles and paid products, under [CC BY 4.0](LICENSE). Credit Numbers.sg and the publisher, for example:

> {credit}

Each dataset's README has its exact credit line, and any notice its publisher asks you to carry. What the licence covers and what it doesn't is set out in plain words at [numbers.sg/data/licence](https://numbers.sg/data/licence/).

## Citing

{('**DOI: [' + DOI + '](https://doi.org/' + DOI + ')**. Each January a dated snapshot of this repository is archived on Zenodo; this DOI always resolves to the newest one, and each snapshot has its own DOI for a copy that never changes.' + chr(10) + chr(10) + '```' + chr(10) + 'Say, J. (' + TODAY[:4] + '). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/' + DOI + chr(10) + '```' + chr(10) + chr(10)) if DOI else ''}GitHub's "Cite this repository" button uses [`CITATION.cff`](CITATION.cff). Each dataset's README has its own citation and BibTeX entry. To cite numbers as they stood on a given day, use the API's dated copies: `{API}{{id}}/as-of/YYYY-MM-DD`, saved every night since 26 Nov 2026 and never changed afterwards.

## Not in this repository

These datasets rest on at least one source whose terms grant no reuse beyond personal use. We publish their figures as facts on Numbers.sg and in the API, but we don't redistribute the whole series here. Read each source's terms before republishing:

{facts}

## About

[Numbers.sg](https://numbers.sg/) tracks Singapore rates, prices and rules, each read from its official source. It is independent: none of it is part of, endorsed by or paid by the Singapore Government or any of its agencies, it is not part of any bank, and no one pays for a figure, a ranking or a place on a page. Something that looks wrong: [report a wrong number]({REPO}/issues/new?template=wrong-number.yml). A dataset you'd like: [ask for it]({REPO}/issues/new?template=dataset-request.yml). Or write to hello@numbers.sg.
'''


def datapackage(mirrored):
    res = []
    for d in mirrored:
        doc = json.load(open(os.path.join(ROOT, f'datasets/{d["id"]}/{d["id"]}.json'), encoding='utf-8')) if not CHECK or os.path.exists(os.path.join(ROOT, f'datasets/{d["id"]}/{d["id"]}.json')) else None
        if not doc:
            continue
        res.append({
            'name': d['id'], 'path': f'datasets/{d["id"]}/{d["id"]}.csv', 'format': 'csv', 'mediatype': 'text/csv', 'encoding': 'utf-8',
            'title': d['title'], 'description': doc.get('description'), 'homepage': d['page_url'],
            'sources': [{'title': s['publisher'], 'path': s['url']} for s in doc['sources']],
            'licenses': [{'name': 'CC-BY-4.0', 'path': 'https://creativecommons.org/licenses/by/4.0/', 'title': 'Creative Commons Attribution 4.0'}],
            'schema': {'fields': [{'name': f['name'], 'type': TYPES.get(f['type'], ('string',))[0], 'description': f['meaning']} for f in doc['fields']],
                       'missingValues': ['']},
        })
    return json.dumps({
        'name': 'numbers-sg-data', 'title': 'Singapore rates and prices: open data from Numbers.sg', 'homepage': 'https://numbers.sg/developers/',
        'licenses': [{'name': 'CC-BY-4.0', 'path': 'https://creativecommons.org/licenses/by/4.0/', 'title': 'Creative Commons Attribution 4.0'}],
        'resources': res,
    }, ensure_ascii=False, indent=1) + '\n'


def citation(mirrored):
    newest = max(d['updated'] for d in mirrored)
    return f'''cff-version: 1.2.0
message: "If you use these data, please cite them as below, and credit the publisher named in each dataset's README."
type: dataset
title: "Singapore rates and prices: open data from Numbers.sg"
authors:
  - name: "Numbers.sg"
    website: "https://numbers.sg/"
date-released: "{newest}"
license: CC-BY-4.0
url: "https://numbers.sg/developers/"
repository-code: "{REPO}"
{('doi: ' + DOI + chr(10) + 'identifiers:' + chr(10) + '  - type: doi' + chr(10) + '    value: ' + DOI + chr(10) + '    description: Archived on Zenodo; resolves to the newest version' + chr(10)) if DOI else ''}{('preferred-citation:' + chr(10) + '  type: dataset' + chr(10) + '  title: "Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data)"' + chr(10) + '  authors:' + chr(10) + '    - family-names: Say' + chr(10) + '      given-names: Jeremiah' + chr(10) + '      orcid: "https://orcid.org/0009-0009-2025-7691"' + chr(10) + '      affiliation: "Numbers Publishing Pte. Ltd."' + chr(10) + '  publisher:' + chr(10) + '    name: Numbers.sg' + chr(10) + '  doi: ' + DOI + chr(10) + '  year: ' + newest[:4] + chr(10) + '  license: CC-BY-4.0' + chr(10) + '  url: "https://doi.org/' + DOI + '"' + chr(10)) if DOI else ''}abstract: "{len(mirrored)} datasets of Singapore {topics_phrase(mirrored)}, each read from its official source and refreshed nightly from the Numbers.sg data API."
keywords:
  - Singapore
  - open data
  - SORA
  - COE
  - CPF
  - exchange rates
  - interest rates
'''


if __name__ == '__main__':
    main()
