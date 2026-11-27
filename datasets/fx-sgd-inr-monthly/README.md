# Singapore dollar to Indian rupee, monthly averages since 2006

[![Chart of Singapore dollar to Indian rupee, monthly averages since 2006, from Numbers.sg](https://numbers.sg/charts/sgd-to-inr-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-inr/)

SingStat's monthly average exchange rate for the rupee (table M700051, averages of MAS's figures) since January 2006, both ways round.

**The question it answers:** What was the average rupee rate for the Singapore dollar each month since 2006?

| | |
|---|---|
| Rows | 250 |
| Each row | One month (the average of the month) |
| Covers | Jan 2006 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Department of Statistics (SingStat) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-inr/](https://numbers.sg/currency/sgd-to-inr/) |

## Download

- CSV: [`fx-sgd-inr-monthly.csv`](fx-sgd-inr-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-inr-monthly/fx-sgd-inr-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-inr-monthly.json`](fx-sgd-inr-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-inr-monthly` (newest rows), `https://numbers.sg/api/v1/fx-sgd-inr-monthly/history` (every row), `https://numbers.sg/api/v1/fx-sgd-inr-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-inr-monthly/fx-sgd-inr-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-inr-monthly/fx-sgd-inr-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-inr-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `inr_per_sgd` | 74.5935 |
| `sgd_per_100_inr` | 1.3406 |
| `source` | SingStat M700051 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `inr_per_sgd` | number | Rupees per S$1: SingStat's S$ figure, turned round. Unit: rupees per S$1. |
| `sgd_per_100_inr` | number | S$ per 100 rupees: SingStat's monthly average, in the daily table's unit. Unit: S$ per 100 rupees. |
| `source` | string | Where the month's figure comes from. |

## Where the numbers come from

- [Department of Statistics (SingStat)](https://www.singstat.gov.sg/), under the [SingStat terms of use](https://www.singstat.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-inr/#method](https://numbers.sg/currency/sgd-to-inr/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-inr-monthly/changes.atom`](https://numbers.sg/api/v1/fx-sgd-inr-monthly/changes.atom).

## Corrections

Each mistake found in this dataset or on its page, newest first. The same list is on [numbers.sg/corrections](https://numbers.sg/corrections/).

- **26 Nov 2026:** SGD to INR: the CSV’s note said it held SingStat’s monthly averages for the years before the daily record, but the file had none of them. It now ends with a second table of SingStat’s monthly averages of MAS’s rupee figures, 250 months from January 2006 to October 2026, and the chart’s key no longer lists a SingStat line that is not drawn.
- **7 Nov 2026:** SGD to INR: the summary and search description said the page had every day since 2008. MAS’s daily rupee rate begins on 3 January 2006, and the page now says so. A record date read “In 3 January”; it now reads “On”.
- **2 Nov 2026:** on our SGD to INR page, under “Is today’s rate good?”, the sentence on changing rupees into S$ said your rupees bought fewer S$ today than on a share of days, but gave the share of days on which they bought fewer S$ than today, the opposite. It now gives the right share. The table beside it and the figures for changing S$ into rupees were right.

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Department of Statistics, compiled by Numbers.sg (numbers.sg/currency/sgd-to-inr/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Singapore Department of Statistics

To cite it:

```
Numbers.sg (2026). Singapore dollar to Indian rupee, monthly averages since 2006 [Data set]. https://numbers.sg/currency/sgd-to-inr/
```

```bibtex
@misc{numberssg_fx_sgd_inr_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Indian rupee, monthly averages since 2006}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-inr/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-inr-monthly/as-of/YYYY-MM-DD`.
