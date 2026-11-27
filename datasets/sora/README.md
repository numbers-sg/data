# SORA and Compounded SORA, daily

[![Chart of SORA and Compounded SORA, daily, from Numbers.sg](https://numbers.sg/charts/sora-rate-chart.png)](https://numbers.sg/rates/sora/)

The Singapore Overnight Rate Average for every business day since July 2005, with MAS's SORA Index, the 1, 3 and 6-month Compounded SORA, and, from August 2020, the volume and the highest and lowest rates traded.

**The question it answers:** What is SORA today, and how has it moved since 2005?

| | |
|---|---|
| Rows | 5,373 |
| Each row | One business day (the value date) |
| Covers | 1 Jul 2005 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/rates/sora/](https://numbers.sg/rates/sora/) |

## Download

- CSV: [`sora.csv`](sora.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/sora/sora.csv`
- JSON, with the field list, sources and notices: [`sora.json`](sora.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/sora` (newest rows), `https://numbers.sg/api/v1/sora/history` (every row), `https://numbers.sg/api/v1/sora.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/sora/sora.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/sora/sora.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/sora.csv")`

## The last row

| Field | Value |
|---|---|
| `value_date` | 2026-11-26 |
| `publication_date` | 2026-11-27 |
| `sora_pct` | 1.4628 |
| `sora_index` | 1.1272439642 |
| `compounded_1m_pct` | 1.5658 |
| `compounded_3m_pct` | 1.3891 |
| `compounded_6m_pct` | 1.2757 |
| `volume_sgd_m` | 3537 |
| `highest_rate_pct` | 1.7 |
| `lowest_rate_pct` | 1 |
| `source` | MAS Domestic Interest Rates; compiled by Numbers.sg |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `value_date` | date | The business day the rate is for. |
| `publication_date` | date | The day MAS published it, usually the next business day. |
| `sora_pct` | number | SORA: the volume-weighted average rate of unsecured overnight interbank S$ lending that day. Unit: percent a year. |
| `sora_index` | number | MAS's SORA Index, which compounds SORA day by day; the change between two dates gives the compounded rate between them. Unit: index (MAS SORA Index). |
| `compounded_1m_pct` | number | 1-month Compounded SORA: SORA compounded over the month before the publication date (MAS's figure from 6 Aug 2020; ours, by MAS's method, before that). Unit: percent a year. Empty when it does not apply to that row. |
| `compounded_3m_pct` | number | 3-month Compounded SORA, worked out the same way over three months. Most SORA home loans use this one. Unit: percent a year. Empty when it does not apply to that row. |
| `compounded_6m_pct` | number | 6-month Compounded SORA, worked out the same way over six months. Unit: percent a year. Empty when it does not apply to that row. |
| `volume_sgd_m` | number | Total overnight lending SORA was worked out from that day. Unit: S$ million. Empty when the source gave no figure. |
| `highest_rate_pct` | number | The highest rate among the trades that day. Unit: percent a year. Empty when the source gave no figure. |
| `lowest_rate_pct` | number | The lowest rate among the trades that day. Unit: percent a year. Empty when the source gave no figure. |
| `source` | string | Where the row comes from. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/rates/sora/#method](https://numbers.sg/rates/sora/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/sora/changes.atom`](https://numbers.sg/api/v1/sora/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/rates/sora/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Domestic Interest Rates (SORA) accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). SORA and Compounded SORA, daily [Data set]. https://numbers.sg/rates/sora/
```

```bibtex
@misc{numberssg_sora,
  author = {{Numbers.sg}},
  title = {{SORA and Compounded SORA, daily}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/rates/sora/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/sora/as-of/YYYY-MM-DD`.
