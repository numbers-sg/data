# Singapore dollar to Malaysian ringgit, monthly averages since 1988

[![Chart of Singapore dollar to Malaysian ringgit, monthly averages since 1988, from Numbers.sg](https://numbers.sg/charts/sgd-to-myr-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-myr/)

SingStat's monthly average exchange rate for the ringgit (table M700051, averages of MAS's figures) since January 1988, both ways round.

**The question it answers:** What was the average ringgit rate for the Singapore dollar each month since 1988?

| | |
|---|---|
| Rows | 466 |
| Each row | One month (the average of the month) |
| Covers | Jan 1988 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Department of Statistics (SingStat) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-myr/](https://numbers.sg/currency/sgd-to-myr/) |

## Download

- CSV: [`fx-sgd-myr-monthly.csv`](fx-sgd-myr-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr-monthly/fx-sgd-myr-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-myr-monthly.json`](fx-sgd-myr-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-myr-monthly` (newest rows), `https://numbers.sg/api/v1/fx-sgd-myr-monthly/history` (every row), `https://numbers.sg/api/v1/fx-sgd-myr-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr-monthly/fx-sgd-myr-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr-monthly/fx-sgd-myr-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-myr-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `myr_per_sgd` | 3.1898 |
| `sgd_per_myr` | 0.3135 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `myr_per_sgd` | number | Ringgit per Singapore dollar: SingStat's S$ per ringgit, turned round. Unit: ringgit per S$1. |
| `sgd_per_myr` | number | Singapore dollars per ringgit, SingStat's monthly average. Unit: S$ per ringgit. |

## Where the numbers come from

- [Department of Statistics (SingStat)](https://www.singstat.gov.sg/), under the [SingStat terms of use](https://www.singstat.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-myr/#method](https://numbers.sg/currency/sgd-to-myr/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-myr-monthly/changes.atom`](https://numbers.sg/api/v1/fx-sgd-myr-monthly/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Department of Statistics, compiled by Numbers.sg (numbers.sg/currency/sgd-to-myr/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Singapore Department of Statistics

To cite it:

```
Numbers.sg (2026). Singapore dollar to Malaysian ringgit, monthly averages since 1988 [Data set]. https://numbers.sg/currency/sgd-to-myr/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_sgd_myr_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Malaysian ringgit, monthly averages since 1988}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-myr/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-myr-monthly/as-of/YYYY-MM-DD`.
