# Singapore dollar to Japanese yen, monthly averages since 1988

[![Chart of Singapore dollar to Japanese yen, monthly averages since 1988, from Numbers.sg](https://numbers.sg/charts/sgd-to-jpy-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-jpy/)

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

## Corrections

Each mistake found in this dataset or on its page, newest first. The same list is on [numbers.sg/corrections](https://numbers.sg/corrections/).

- **26 Nov 2026:** SGD to JPY: the CSV’s note said it held SingStat’s monthly averages for the years before the daily record, but the file had none of them. It now ends with a second table of SingStat’s monthly averages of MAS’s yen figures, 466 months from January 1988 to October 2026, and the chart’s key no longer lists a SingStat line that is not drawn.
- **7 Nov 2026:** SGD to JPY: the page called MAS’s figures daily all the way back to 1988. MAS published the yen rate once a week until the end of 2002 and every working day from January 2003. The chart, the year-by-year table, the records and the rate-on-a-date tool now say which, and a date before 2003 shows that week’s figure. The rates themselves were right.
- **2 Nov 2026:** on our SGD to JPY page, under “Is today’s rate good?”, the sentence on changing yen into S$ said your yen bought fewer S$ today than on a share of days, but gave the share of days on which they bought fewer S$ than today, the opposite. It now gives the right share. The table beside it and the figures for changing S$ into yen were right.

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Department of Statistics, compiled by Numbers.sg (numbers.sg/currency/sgd-to-jpy/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Singapore Department of Statistics

To cite it:

```
Numbers.sg (2026). Singapore dollar to Japanese yen, monthly averages since 1988 [Data set]. https://numbers.sg/currency/sgd-to-jpy/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_sgd_jpy_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Japanese yen, monthly averages since 1988}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-jpy/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-jpy-monthly/as-of/YYYY-MM-DD`.
