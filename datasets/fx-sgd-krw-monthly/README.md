# Singapore dollar to South Korean won, monthly averages since 2003

[![Chart of Singapore dollar to South Korean won, monthly averages since 2003, from Numbers.sg](https://numbers.sg/charts/sgd-to-krw-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-krw/)

Monthly averages of the won, worked out by Numbers.sg from MAS's daily rates for each complete month (the mean of MAS's S$ per 100 won, turned round), since January 2003.

**The question it answers:** What was the average won rate for the Singapore dollar each month since 2003?

| | |
|---|---|
| Rows | 286 |
| Each row | One month (the average of the month) |
| Covers | Jan 2003 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-krw/](https://numbers.sg/currency/sgd-to-krw/) |

## Download

- CSV: [`fx-sgd-krw-monthly.csv`](fx-sgd-krw-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-krw-monthly/fx-sgd-krw-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-krw-monthly.json`](fx-sgd-krw-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-krw-monthly` (newest rows), `https://numbers.sg/api/v1/fx-sgd-krw-monthly/history` (every row), `https://numbers.sg/api/v1/fx-sgd-krw-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-krw-monthly/fx-sgd-krw-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-krw-monthly/fx-sgd-krw-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-krw-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `krw_per_sgd` | 1045.080994 |
| `sgd_per_10000_krw` | 9.568636 |
| `source` | Numbers.sg mean of MAS daily rates |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `krw_per_sgd` | number | Won per S$1: our monthly mean of MAS's S$ figure, turned round. Unit: won per S$1. |
| `sgd_per_10000_krw` | number | S$ per 10,000 won: our mean of MAS's daily figures for the month. Unit: S$ per 10,000 won. |
| `source` | string | Where the month's figure comes from. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-krw/#method](https://numbers.sg/currency/sgd-to-krw/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-krw-monthly/changes.atom`](https://numbers.sg/api/v1/fx-sgd-krw-monthly/changes.atom).

## Corrections

Each mistake found in this dataset or on its page, newest first. The same list is on [numbers.sg/corrections](https://numbers.sg/corrections/).

- **26 Nov 2026:** SGD to KRW: the history before 2003 had rates for 12 and 15 December 1997, at the height of the Asian financial crisis. The Federal Reserve’s own H.10 table has no won rate for those two days (it marks them ND, no data); the figures came from a copy of the series elsewhere. They are gone from the chart and the CSV, and the history is now read from the Fed’s own tables, which match on every other day.

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/currency/sgd-to-krw/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore dollar to South Korean won, monthly averages since 2003 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). Singapore dollar to South Korean won, monthly averages since 2003 [Data set]. https://numbers.sg/currency/sgd-to-krw/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_sgd_krw_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to South Korean won, monthly averages since 2003}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-krw/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-krw-monthly/as-of/YYYY-MM-DD`.
