# US dollar to Singapore dollar, monthly averages since 1988

[![Chart of US dollar to Singapore dollar, monthly averages since 1988, from Numbers.sg](https://numbers.sg/charts/usd-to-sgd-exchange-rate-chart.png)](https://numbers.sg/currency/usd-to-sgd/)

SingStat's monthly average exchange rate for the US dollar (table M700051, averages of MAS's figures) since January 1988, both ways round.

**The question it answers:** What was the average US dollar rate in Singapore dollars each month since 1988?

| | |
|---|---|
| Rows | 466 |
| Each row | One month (the average of the month) |
| Covers | Jan 1988 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Department of Statistics (SingStat) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/usd-to-sgd/](https://numbers.sg/currency/usd-to-sgd/) |

## Download

- CSV: [`fx-usd-sgd-monthly.csv`](fx-usd-sgd-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-usd-sgd-monthly/fx-usd-sgd-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-usd-sgd-monthly.json`](fx-usd-sgd-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-usd-sgd-monthly` (newest rows), `https://numbers.sg/api/v1/fx-usd-sgd-monthly/history` (every row), `https://numbers.sg/api/v1/fx-usd-sgd-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-usd-sgd-monthly/fx-usd-sgd-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-usd-sgd-monthly/fx-usd-sgd-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-usd-sgd-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `sgd_per_usd` | 1.2796 |
| `usd_per_sgd` | 0.781494 |
| `source` | SingStat M700051 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `sgd_per_usd` | number | S$ per US$1: SingStat's monthly average. Unit: S$ per US$1. |
| `usd_per_sgd` | number | US$ per S$1: SingStat's figure, turned round. Unit: US$ per S$1. |
| `source` | string | Where the month's figure comes from. |

## Where the numbers come from

- [Department of Statistics (SingStat)](https://www.singstat.gov.sg/), under the [SingStat terms of use](https://www.singstat.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/usd-to-sgd/#method](https://numbers.sg/currency/usd-to-sgd/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-usd-sgd-monthly/changes.atom`](https://numbers.sg/api/v1/fx-usd-sgd-monthly/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Department of Statistics, compiled by Numbers.sg (numbers.sg/currency/usd-to-sgd/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Singapore Department of Statistics

To cite it:

```
Numbers.sg (2026). US dollar to Singapore dollar, monthly averages since 1988 [Data set]. https://numbers.sg/currency/usd-to-sgd/
```

```bibtex
@misc{numberssg_fx_usd_sgd_monthly,
  author = {{Numbers.sg}},
  title = {{US dollar to Singapore dollar, monthly averages since 1988}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/usd-to-sgd/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-usd-sgd-monthly/as-of/YYYY-MM-DD`.
