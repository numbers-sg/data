# Singapore dollar to Chinese yuan, monthly averages since 1993

SingStat's monthly average exchange rate for the yuan (table M700051, averages of MAS's figures) since June 1993, both ways round.

**The question it answers:** What was the average yuan rate for the Singapore dollar each month since 1993?

| | |
|---|---|
| Rows | 401 |
| Each row | One month (the average of the month) |
| Covers | Jun 1993 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Department of Statistics (SingStat) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-cny/](https://numbers.sg/currency/sgd-to-cny/) |

## Download

- CSV: [`fx-sgd-cny-monthly.csv`](fx-sgd-cny-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-cny-monthly/fx-sgd-cny-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-cny-monthly.json`](fx-sgd-cny-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-cny-monthly` (newest rows), `https://numbers.sg/api/v1/fx-sgd-cny-monthly/history` (every row), `https://numbers.sg/api/v1/fx-sgd-cny-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-cny-monthly/fx-sgd-cny-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-cny-monthly/fx-sgd-cny-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-cny-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `cny_per_sgd` | 5.2247 |
| `sgd_per_100_cny` | 19.14 |
| `source` | SingStat M700051 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `cny_per_sgd` | number | Yuan per S$1: SingStat's S$ figure, turned round. Unit: yuan per S$1. |
| `sgd_per_100_cny` | number | S$ per 100 yuan: SingStat's monthly average, in the daily table's unit. Unit: S$ per 100 yuan. |
| `source` | string | Where the month's figure comes from. |

## Where the numbers come from

- [Department of Statistics (SingStat)](https://www.singstat.gov.sg/), under the [SingStat terms of use](https://www.singstat.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-cny/#method](https://numbers.sg/currency/sgd-to-cny/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-cny-monthly/changes.atom`](https://numbers.sg/api/v1/fx-sgd-cny-monthly/changes.atom).

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Department of Statistics, compiled by Numbers.sg (numbers.sg/currency/sgd-to-cny/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Singapore Department of Statistics

To cite it:

```
Numbers.sg (2026). Singapore dollar to Chinese yuan, monthly averages since 1993 [Data set]. https://numbers.sg/currency/sgd-to-cny/
```

```bibtex
@misc{numberssg_fx_sgd_cny_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Chinese yuan, monthly averages since 1993}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-cny/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-cny-monthly/as-of/YYYY-MM-DD`.
