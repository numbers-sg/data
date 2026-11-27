# Singapore dollar to Korean won, daily since 1981

[![Chart of Singapore dollar to Korean won, daily since 1981, from Numbers.sg](https://numbers.sg/charts/sgd-to-krw-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-krw/)

Won per Singapore dollar and Singapore dollars per 10,000 won, each working day since 1981: MAS's noon rate where MAS publishes one, and earlier days from the source named on each row.

**The question it answers:** What is the Singapore dollar worth in won, on any working day since 1981?

| | |
|---|---|
| Rows | 11,408 |
| Each row | One working day |
| Covers | 13 Apr 1981 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS), Federal Reserve Board |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-krw/](https://numbers.sg/currency/sgd-to-krw/) |

## Download

- CSV: [`fx-sgd-krw.csv`](fx-sgd-krw.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-krw/fx-sgd-krw.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-krw.json`](fx-sgd-krw.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-krw` (newest rows), `https://numbers.sg/api/v1/fx-sgd-krw/history` (every row), `https://numbers.sg/api/v1/fx-sgd-krw.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-krw/fx-sgd-krw.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-krw/fx-sgd-krw.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-krw.csv")`

## The last row

| Field | Value |
|---|---|
| `date` | 2026-11-26 |
| `krw_per_sgd` | 1041.666667 |
| `sgd_per_10000_krw` | 9.6 |
| `source` | MAS |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `date` | date | The day the rate is for. |
| `krw_per_sgd` | number | How many won one Singapore dollar buys (the inverse of the next column, kept to six decimals). Unit: won per S$1. |
| `sgd_per_10000_krw` | number | Singapore dollars per 10,000 won, the way MAS quotes it. Unit: S$ per 10,000 won. |
| `source` | string | Which figure the row is: FED-H10 = the US Federal Reserve's H.10 noon rates, crossed (before MAS's daily record); MAS = MAS, as of noon. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)
- [Federal Reserve Board](https://www.federalreserve.gov/releases/h10/current/), under the [Federal Reserve Board website: public domain](https://www.federalreserve.gov/disclaimer.htm)

How each figure is read and checked: [numbers.sg/currency/sgd-to-krw/#method](https://numbers.sg/currency/sgd-to-krw/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-krw/changes.atom`](https://numbers.sg/api/v1/fx-sgd-krw/changes.atom).

## Corrections

Each mistake found in this dataset or on its page, newest first. The same list is on [numbers.sg/corrections](https://numbers.sg/corrections/).

- **26 Nov 2026:** SGD to KRW: the history before 2003 had rates for 12 and 15 December 1997, at the height of the Asian financial crisis. The Federal Reserve’s own H.10 table has no won rate for those two days (it marks them ND, no data); the figures came from a copy of the series elsewhere. They are gone from the chart and the CSV, and the history is now read from the Fed’s own tables, which match on every other day.

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore and Federal Reserve Board, compiled by Numbers.sg (numbers.sg/currency/sgd-to-krw/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore dollar to Korean won, daily since 1981 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

> Source: Board of Governors of the Federal Reserve System (H.10)

To cite it:

```
Numbers.sg (2026). Singapore dollar to Korean won, daily since 1981 [Data set]. https://numbers.sg/currency/sgd-to-krw/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_sgd_krw,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Korean won, daily since 1981}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-krw/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-krw/as-of/YYYY-MM-DD`.
