#!/usr/bin/env python3
"""Archive a dated snapshot of this repository on Zenodo, with a DOI.

  python3 scripts/zenodo.py            make a DRAFT (first run: a new record; later runs: a new version of the same
                                       record, so the concept DOI never changes) and print its URL. Nothing public.
  python3 scripts/zenodo.py --publish  publish the draft made above. A published DOI cannot be deleted.

Token: ZENODO_TOKEN, or GC_ZENODO_TOKEN in ~/.gc-secrets (the owner's Zenodo account, shared by all the sites).
State: zenodo.json (record ids and DOIs, nothing secret). Uses Zenodo's InvenioRDM API (/api/records), which takes
alternative titles, a publisher, locations and method notes that the older deposit API can't.
Standard library only. Yearly: run it each January after the nightly update has committed.
"""
import datetime as dt, io, json, os, re, subprocess, sys, urllib.error, urllib.request, zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from update import TOPICS, topic, topics_phrase  # noqa: E402  (same grouping as the README)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = 'https://zenodo.org/api'
STATE = os.path.join(ROOT, 'zenodo.json')
ORCID = '0009-0009-2025-7691'
REPO = 'https://github.com/numbers-sg/data'
FILES = ['README.md', 'LICENSE', 'CITATION.cff', 'datapackage.json', 'index.json', 'datasets', 'scripts']


def token():
    t = os.environ.get('ZENODO_TOKEN')
    if not t:
        for line in open(os.path.expanduser('~/.gc-secrets'), encoding='utf-8'):
            m = re.match(r'\s*(?:export\s+)?GC_ZENODO_TOKEN=["\']?([^"\'\s]+)', line)
            if m:
                t = m.group(1)
    if not t:
        sys.exit('No Zenodo token')
    return t


def call(method, url, body=None, raw=None, ctype='application/json'):
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    req = urllib.request.Request(url if url.startswith('http') else API + url, data=data, method=method,
                                 headers={'Authorization': 'Bearer ' + token(), 'Content-Type': ctype, 'Accept': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            txt = r.read().decode()
            return json.loads(txt) if txt else {}
    except urllib.error.HTTPError as e:
        sys.exit(f'{method} {url}: HTTP {e.code}\n{e.read().decode()[:2000]}')


def snapshot(day):
    """A zip of the committed repository (git archive: only tracked files, exactly as on GitHub)."""
    if subprocess.run(['git', '-C', ROOT, 'status', '--porcelain', '--'] + FILES, capture_output=True, text=True).stdout.strip():
        sys.exit('Uncommitted changes: commit and push first, so the archive equals GitHub')
    head = subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    tar = subprocess.run(['git', '-C', ROOT, 'archive', '--format=zip', f'--prefix=numbers-sg-data-{day}/', 'HEAD'] + FILES,
                         capture_output=True).stdout
    zipfile.ZipFile(io.BytesIO(tar)).testzip()
    return tar, head


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def metadata(day, head):
    idx = json.load(open(os.path.join(ROOT, 'index.json'), encoding='utf-8'))['datasets']
    rows = sum(d['rows'] for d in idx)
    first = min(str(d['from']) for d in idx if d['from'])[:4]
    srcs = {}
    for d in idx:
        for s in json.load(open(os.path.join(ROOT, f"datasets/{d['id']}/{d['id']}.json"), encoding='utf-8'))['sources']:
            srcs.setdefault(s['url'], s['publisher'])
    groups = ''
    for n in sorted({topic(d['id']) for d in idx}):
        ds = sorted((d for d in idx if topic(d['id']) == n), key=lambda d: d['title'].lower())
        groups += f"<p><strong>{esc(TOPICS[n][1] if n < len(TOPICS) else 'Other')}</strong></p><ul>" + ''.join(
            f"<li>{esc(d['title'])} (<code>{d['id']}</code>, {d['rows']:,} rows)</li>" for d in ds) + '</ul>'
    pubs = sorted(set(re.sub(r',\s*via .*$', '', p) for p in srcs.values()))
    desc = (
        f"<p>Singapore {esc(topics_phrase(idx))}, as {len(idx)} ready-to-use CSV and JSON time series ({rows:,} rows, the oldest from {first}). "
        "Includes SORA and compounded SORA, Singapore Government T-bill auction results, Singapore Savings Bonds rates, "
        "COE bidding results (Certificate of Entitlement prices), CPF wage ceilings, resident income tax rates, inflation "
        "(consumer price index) and exchange rates for the Singapore dollar against the US dollar, euro, yen, yuan, ringgit, "
        "rupiah, baht, peso, won and rupee.</p>"
        f"<p>Each figure is read from the body that publishes it: {esc(', '.join(pubs))}. "
        "Every dataset carries its sources, the terms each source is published under, a meaning and unit for every field, "
        "and the credit line to use.</p>"
        f"<p>This record is a dated snapshot of <a href=\"{REPO}\">github.com/numbers-sg/data</a>, which is refreshed every night. "
        "For the newest numbers use the free <a href=\"https://numbers.sg/developers/\">Numbers.sg data API</a> (no key; JSON and CSV; "
        "every answer says when the source was last read) or the GitHub repository. Cite this record's DOI for a fixed copy.</p>"
        f"<p><strong>Datasets in this version</strong></p>{groups}"
        "<p><strong>Files</strong>: one folder per dataset with a CSV, a JSON copy (field list, sources, licence notices) and a README; "
        "<code>datapackage.json</code> (Frictionless Data), <code>index.json</code>, <code>CITATION.cff</code>, and the scripts that build and check the files.</p>"
        "<p><strong>Quick start</strong>: <code>pandas.read_csv(\"datasets/sora/sora.csv\")</code>, or from the web: "
        "<code>https://raw.githubusercontent.com/numbers-sg/data/main/datasets/sora/sora.csv</code>.</p>"
        "<p><strong>Publisher</strong>: <a href=\"https://numbers.sg/\">Numbers.sg</a>, published by Numbers Publishing Pte. Ltd., Singapore, and "
        "edited by Jeremiah Say. Numbers.sg is independent: none of it is part of, endorsed by or paid by the Singapore Government or any of its agencies, "
        "and no one pays for a figure, a ranking or a place on a page. Corrections are listed at "
        "<a href=\"https://numbers.sg/corrections/\">numbers.sg/corrections</a>.</p>"
    )
    methods = (
        "<p>1. Each figure is read from its official source by a scheduled job, as often as every 10 minutes for COE results; figures that change "
        "rarely are kept by hand and re-read on a booked date (<a href=\"https://numbers.sg/update-schedule/\">update schedule</a>).</p>"
        "<p>2. Every night at 23:50 Singapore time a separate job compares each dataset, cell for cell, with the CSV on its own Numbers.sg page, "
        "and keeps a dated copy only when both match.</p>"
        f"<p>3. At 00:20 the GitHub repository rebuilds every file from the API and runs <code>scripts/validate.py</code> (headers, row counts, "
        "types, empty values, duplicate rows) before committing. This archive is a zip of that repository at commit "
        f"<code>{head[:12]}</code>.</p>"
        "<p>4. Mistakes are corrected in the open, with the date and what changed, in each dataset's README and at numbers.sg/corrections. "
        "How each dataset is read is set out on its page under \"How we get these numbers\", and overall at "
        "<a href=\"https://numbers.sg/how-we-get-our-numbers/\">numbers.sg/how-we-get-our-numbers</a>.</p>"
    )
    kw = ['Singapore', 'open data', 'time series', 'SORA', 'Singapore Overnight Rate Average', 'interest rates', 'Treasury bills',
          'T-bills', 'Singapore Savings Bonds', 'government bonds', 'COE', 'Certificate of Entitlement', 'car prices', 'CPF',
          'Central Provident Fund', 'income tax', 'tax rates', 'inflation', 'consumer price index', 'exchange rates',
          'Singapore dollar', 'SGD', 'foreign exchange', 'Monetary Authority of Singapore', 'MAS', 'SingStat', 'finance', 'economics']
    return {
        'resource_type': {'id': 'dataset'},
        'title': 'Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data)',
        'additional_titles': [
            {'title': 'Numbers.sg open data: Singapore rates and prices', 'type': {'id': 'alternative-title'}, 'lang': {'id': 'eng'}},
            {'title': 'Singapore SORA, T-bill, Savings Bond, COE, CPF, income tax, inflation and exchange rate time series',
             'type': {'id': 'alternative-title'}, 'lang': {'id': 'eng'}},
        ],
        'publication_date': day,
        'version': day,
        'publisher': 'Numbers.sg',
        'creators': [{
            'person_or_org': {'type': 'personal', 'given_name': 'Jeremiah', 'family_name': 'Say',
                              'identifiers': [{'scheme': 'orcid', 'identifier': ORCID}]},
            'affiliations': [{'name': 'Numbers Publishing Pte. Ltd.'}],
        }],
        'contributors': [
            {'person_or_org': {'type': 'organizational', 'name': 'Numbers Publishing Pte. Ltd.'}, 'role': {'id': 'rightsholder'}},
            {'person_or_org': {'type': 'organizational', 'name': 'Numbers.sg'}, 'role': {'id': 'producer'}},
        ],
        'description': desc,
        'additional_descriptions': [{'description': methods, 'type': {'id': 'methods'}}],
        'rights': [{'id': 'cc-by-4.0'}],
        'subjects': [{'subject': k} for k in kw],
        'languages': [{'id': 'eng'}],
        'dates': [{'date': f'{first}/{day[:4]}', 'type': {'id': 'other'}, 'description': 'Years covered by the data'}],
        'locations': {'features': [{'place': 'Singapore', 'description': 'Republic of Singapore',
                                    'identifiers': [{'scheme': 'geonames', 'identifier': '1880251'}],
                                    'geometry': {'type': 'Point', 'coordinates': [103.8198, 1.3521]}}]},
        'related_identifiers': [
            {'identifier': REPO, 'scheme': 'url', 'relation_type': {'id': 'issupplementto'}, 'resource_type': {'id': 'dataset'}},
            {'identifier': 'https://numbers.sg/developers/', 'scheme': 'url', 'relation_type': {'id': 'isdocumentedby'}, 'resource_type': {'id': 'other'}},
            {'identifier': 'https://numbers.sg/how-we-get-our-numbers/', 'scheme': 'url', 'relation_type': {'id': 'isdescribedby'}, 'resource_type': {'id': 'other'}},
        ] + [{'identifier': u, 'scheme': 'url', 'relation_type': {'id': 'isderivedfrom'}, 'resource_type': {'id': 'dataset'}} for u in srcs],
    }


def main():
    publish = '--publish' in sys.argv
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    if publish:
        if not st.get('draft_id'):
            sys.exit('No draft: run without --publish first')
        rec = call('POST', f"/records/{st['draft_id']}/draft/actions/publish")
        st.update({'record_id': rec['id'], 'doi': rec['pids']['doi']['identifier'], 'version': rec['metadata']['version'],
                   'concept_doi': rec.get('parent', {}).get('pids', {}).get('doi', {}).get('identifier') or st.get('concept_doi'),
                   'concept_id': rec.get('parent', {}).get('id') or st.get('concept_id')})
        st.pop('draft_id', None)
        json.dump(st, open(STATE, 'w'), indent=1)
        print('PUBLISHED', rec['links']['self_html'], 'DOI', st['doi'], 'concept DOI', st['concept_doi'])
        return
    day = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    blob, head = snapshot(day)
    if st.get('record_id'):  # a new version of the same record: the concept DOI stays
        d = call('POST', f"/records/{st['record_id']}/versions")
        for f in call('GET', f"/records/{d['id']}/draft/files").get('entries', []):
            call('DELETE', f"/records/{d['id']}/draft/files/{f['key']}")
    else:
        d = call('POST', '/records', {'metadata': {'resource_type': {'id': 'dataset'}, 'title': 'draft', 'publication_date': day,
                                                   'creators': [{'person_or_org': {'type': 'personal', 'given_name': 'Jeremiah', 'family_name': 'Say'}}]},
                                      'files': {'enabled': True}})
    rid = d['id']
    call('POST', f'/records/{rid}/draft/pids/doi')  # reserve the DOI now, so it can go in the files' citations later
    call('PUT', f'/records/{rid}/draft', {'metadata': metadata(day, head), 'files': {'enabled': True, 'default_preview': 'README.md'}})
    files = {f'numbers-sg-data-{day}.zip': blob, 'README.md': open(os.path.join(ROOT, 'README.md'), 'rb').read()}
    call('POST', f'/records/{rid}/draft/files', [{'key': k} for k in files])
    for k, v in files.items():
        call('PUT', f'/records/{rid}/draft/files/{k}/content', raw=v, ctype='application/octet-stream')
        call('POST', f'/records/{rid}/draft/files/{k}/commit')
    dr = call('GET', f'/records/{rid}/draft')
    st['draft_id'] = rid
    json.dump(st, open(STATE, 'w'), indent=1)
    print('DRAFT', f'https://zenodo.org/uploads/{rid}', 'reserved DOI', dr.get('pids', {}).get('doi', {}).get('identifier'))


if __name__ == '__main__':
    main()
