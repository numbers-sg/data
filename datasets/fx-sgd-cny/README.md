# Singapore dollar to Chinese yuan, since 1993 (daily from 2003)

Yuan per Singapore dollar and Singapore dollars per 100 yuan, each working day from 2003 and each week from 1993: MAS's noon rate where MAS publishes one, and earlier days from the source named on each row.

**The question it answers:** What is the Singapore dollar worth in yuan, on any day since 1993?

| | |
|---|---|
| Rows | 6,501 |
| Each row | One working day (one week before 2003) |
| Covers | 4 Jun 1993 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-cny/](https://numbers.sg/currency/sgd-to-cny/) |

## Download

- CSV: [`fx-sgd-cny.csv`](fx-sgd-cny.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-cny/fx-sgd-cny.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-cny.json`](fx-sgd-cny.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-cny` (newest rows), `https://numbers.sg/api/v1/fx-sgd-cny/history` (every row), `https://numbers.sg/api/v1/fx-sgd-cny.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-cny/fx-sgd-cny.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-cny/fx-sgd-cny.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-cny.csv")`

## The last row

| Field | Value |
|---|---|
| `date` | 2026-11-26 |
| `cny_per_sgd` | 5.165289 |
| `sgd_per_100_cny` | 19.360001 |
| `source` | MAS |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `date` | date | The day the rate is for. |
| `cny_per_sgd` | number | How many yuan one Singapore dollar buys (the inverse of the next column, kept to six decimals). Unit: yuan per S$1. |
| `sgd_per_100_cny` | number | Singapore dollars per 100 yuan, the way MAS quotes it. Unit: S$ per 100 yuan. |
| `source` | string | Which figure the row is: MAS = MAS, as of noon; MAS weekly = MAS, weekly (before 2003). |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-cny/#method](https://numbers.sg/currency/sgd-to-cny/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-cny/changes.atom`](https://numbers.sg/api/v1/fx-sgd-cny/changes.atom).

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/currency/sgd-to-cny/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore dollar to Chinese yuan, since 1993 (daily from 2003) accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). Singapore dollar to Chinese yuan, since 1993 (daily from 2003) [Data set]. https://numbers.sg/currency/sgd-to-cny/
```

```bibtex
@misc{numberssg_fx_sgd_cny,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Chinese yuan, since 1993 (daily from 2003)}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-cny/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-cny/as-of/YYYY-MM-DD`.
