# Singapore inflation: CPI and MAS Core, monthly since 1961

[![Chart of Singapore inflation: CPI and MAS Core, monthly since 1961, from Numbers.sg](https://numbers.sg/charts/singapore-inflation-rate-chart.png)](https://numbers.sg/prices/inflation/)

SingStat's Consumer Price Index for all items every month since 1961 and the year-on-year headline inflation rate, with MAS Core inflation (which leaves out accommodation and private transport) from 1991.

**The question it answers:** What is Singapore's inflation rate, headline and MAS Core, every month since 1961?

| | |
|---|---|
| Rows | 790 |
| Each row | One month |
| Covers | Jan 1961 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Department of Statistics (SingStat), Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/prices/inflation/](https://numbers.sg/prices/inflation/) |

## Download

- CSV: [`inflation.csv`](inflation.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/inflation/inflation.csv`
- JSON, with the field list, sources and notices: [`inflation.json`](inflation.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/inflation` (newest rows), `https://numbers.sg/api/v1/inflation/history` (every row), `https://numbers.sg/api/v1/inflation.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/inflation/inflation.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/inflation/inflation.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/inflation.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `cpi_all_items` | 103.229 |
| `headline_inflation_pct_yoy` | 1.9 |
| `mas_core_index` | 102.837 |
| `mas_core_inflation_pct_yoy` | 1.5 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month the prices are for. |
| `cpi_all_items` | number | SingStat's Consumer Price Index for all items. Unit: index (2024 = 100). |
| `headline_inflation_pct_yoy` | number | Headline inflation: how much the CPI rose over the year; blank for 1961, which has no year before. Unit: percent, against the same month a year before. Empty when it does not apply to that row. |
| `mas_core_index` | number | SingStat's MAS Core index, which leaves out accommodation and private transport; from 1990. Unit: index. Empty when the source gave no figure. |
| `mas_core_inflation_pct_yoy` | number | MAS Core inflation: how much the MAS Core index rose over the year; from 1991. Unit: percent, against the same month a year before. Empty when the source gave no figure or it does not apply to that row. |

## Where the numbers come from

- [Department of Statistics (SingStat)](https://www.singstat.gov.sg/), under the [SingStat terms of use](https://www.singstat.gov.sg/terms-of-use)
- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/prices/inflation/#method](https://numbers.sg/prices/inflation/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/inflation/changes.atom`](https://numbers.sg/api/v1/inflation/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Department of Statistics and Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/prices/inflation/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Singapore Department of Statistics

> Contains information from Singapore inflation: CPI and MAS Core, monthly since 1961 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). Singapore inflation: CPI and MAS Core, monthly since 1961 [Data set]. https://numbers.sg/prices/inflation/
```

```bibtex
@misc{numberssg_inflation,
  author = {{Numbers.sg}},
  title = {{Singapore inflation: CPI and MAS Core, monthly since 1961}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/prices/inflation/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/inflation/as-of/YYYY-MM-DD`.
