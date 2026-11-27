# Singapore dollar to Japanese yen, monthly averages since 1988

SingStat's monthly average exchange rate for the yen (table M700051, averages of MAS's figures) since January 1988, both ways round.

**The question it answers:** What was the average yen rate for the Singapore dollar each month since 1988?

| | |
|---|---|
| Rows | 466 |
| Each row | One month (the average of the month) |
| Covers | Jan 1988 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Department of Statistics (SingStat) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-jpy/](https://numbers.sg/currency/sgd-to-jpy/) |

## Download

- CSV: [`fx-sgd-jpy-monthly.csv`](fx-sgd-jpy-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-jpy-monthly/fx-sgd-jpy-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-jpy-monthly.json`](fx-sgd-jpy-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-jpy-monthly` (newest rows), `https://numbers.sg/api/v1/fx-sgd-jpy-monthly/history` (every row), `https://numbers.sg/api/v1/fx-sgd-jpy-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-jpy-monthly/fx-sgd-jpy-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-jpy-monthly/fx-sgd-jpy-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-jpy-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `jpy_per_sgd` | 123.3959 |
| `sgd_per_100_jpy` | 0.8104 |
| `source` | SingStat M700051 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `jpy_per_sgd` | number | Yen per S$1: SingStat's S$ figure, turned round. Unit: yen per S$1. |
| `sgd_per_100_jpy` | number | S$ per 100 yen: SingStat's monthly average, in the daily table's unit. Unit: S$ per 100 yen. |
| `source` | string | Where the month's figure comes from. |

## Where the numbers come from

- [Department of Statistics (SingStat)](https://www.singstat.gov.sg/), under the [SingStat terms of use](https://www.singstat.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-jpy/#method](https://numbers.sg/currency/sgd-to-jpy/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-jpy-monthly/changes.atom`](https://numbers.sg/api/v1/fx-sgd-jpy-monthly/changes.atom).

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Department of Statistics, compiled by Numbers.sg (numbers.sg/currency/sgd-to-jpy/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Singapore Department of Statistics

To cite it:

```
Numbers.sg (2026). Singapore dollar to Japanese yen, monthly averages since 1988 [Data set]. https://numbers.sg/currency/sgd-to-jpy/
```

```bibtex
@misc{numberssg_fx_sgd_jpy_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Japanese yen, monthly averages since 1988}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-jpy/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-jpy-monthly/as-of/YYYY-MM-DD`.
