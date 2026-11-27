# Singapore dollar to Indonesian rupiah, monthly averages since 2003

[![Chart of Singapore dollar to Indonesian rupiah, monthly averages since 2003, from Numbers.sg](https://numbers.sg/charts/sgd-to-idr-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-idr/)

Monthly averages of the rupiah, worked out by Numbers.sg from MAS's daily rates for each complete month (the mean of MAS's S$ per 100 rupiah, turned round), since January 2003.

**The question it answers:** What was the average rupiah rate for the Singapore dollar each month since 2003?

| | |
|---|---|
| Rows | 286 |
| Each row | One month (the average of the month) |
| Covers | Jan 2003 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-idr/](https://numbers.sg/currency/sgd-to-idr/) |

## Download

- CSV: [`fx-sgd-idr-monthly.csv`](fx-sgd-idr-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-idr-monthly/fx-sgd-idr-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-idr-monthly.json`](fx-sgd-idr-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-idr-monthly` (newest rows), `https://numbers.sg/api/v1/fx-sgd-idr-monthly/history` (every row), `https://numbers.sg/api/v1/fx-sgd-idr-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-idr-monthly/fx-sgd-idr-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-idr-monthly/fx-sgd-idr-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-idr-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `idr_per_sgd` | 14060.382954 |
| `sgd_per_1000000_idr` | 71.121818 |
| `source` | Numbers.sg mean of MAS daily rates |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `idr_per_sgd` | number | Rupiah per S$1: our monthly mean of MAS's S$ figure, turned round. Unit: rupiah per S$1. |
| `sgd_per_1000000_idr` | number | S$ per 1,000,000 rupiah: our mean of MAS's daily figures for the month. Unit: S$ per 1,000,000 rupiah. |
| `source` | string | Where the month's figure comes from. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-idr/#method](https://numbers.sg/currency/sgd-to-idr/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-idr-monthly/changes.atom`](https://numbers.sg/api/v1/fx-sgd-idr-monthly/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/currency/sgd-to-idr/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore dollar to Indonesian rupiah, monthly averages since 2003 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). Singapore dollar to Indonesian rupiah, monthly averages since 2003 [Data set]. https://numbers.sg/currency/sgd-to-idr/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_sgd_idr_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Indonesian rupiah, monthly averages since 2003}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-idr/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-idr-monthly/as-of/YYYY-MM-DD`.
