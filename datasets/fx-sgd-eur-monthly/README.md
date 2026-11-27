# Singapore dollar to euro, monthly averages since 1999

SingStat's monthly average exchange rate for the euro (table M700051, averages of MAS's figures) since January 1999, both ways round.

**The question it answers:** What was the average euro rate for the Singapore dollar each month since 1999?

| | |
|---|---|
| Rows | 334 |
| Each row | One month (the average of the month) |
| Covers | Jan 1999 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Department of Statistics (SingStat) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-eur/](https://numbers.sg/currency/sgd-to-eur/) |

## Download

- CSV: [`fx-sgd-eur-monthly.csv`](fx-sgd-eur-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-eur-monthly/fx-sgd-eur-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-eur-monthly.json`](fx-sgd-eur-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-eur-monthly` (newest rows), `https://numbers.sg/api/v1/fx-sgd-eur-monthly/history` (every row), `https://numbers.sg/api/v1/fx-sgd-eur-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-eur-monthly/fx-sgd-eur-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-eur-monthly/fx-sgd-eur-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-eur-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `eur_per_sgd` | 0.697 |
| `sgd_per_eur` | 1.4348 |
| `source` | SingStat M700051 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `eur_per_sgd` | number | Euros per S$1: SingStat's S$ figure, turned round. Unit: euros per S$1. |
| `sgd_per_eur` | number | S$ per euro: SingStat's monthly average, in the daily table's unit. Unit: S$ per euro. |
| `source` | string | Where the month's figure comes from. |

## Where the numbers come from

- [Department of Statistics (SingStat)](https://www.singstat.gov.sg/), under the [SingStat terms of use](https://www.singstat.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-eur/#method](https://numbers.sg/currency/sgd-to-eur/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-eur-monthly/changes.atom`](https://numbers.sg/api/v1/fx-sgd-eur-monthly/changes.atom).

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Department of Statistics, compiled by Numbers.sg (numbers.sg/currency/sgd-to-eur/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Singapore Department of Statistics

To cite it:

```
Numbers.sg (2026). Singapore dollar to euro, monthly averages since 1999 [Data set]. https://numbers.sg/currency/sgd-to-eur/
```

```bibtex
@misc{numberssg_fx_sgd_eur_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to euro, monthly averages since 1999}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-eur/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-eur-monthly/as-of/YYYY-MM-DD`.
