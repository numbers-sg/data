# Singapore dollar to Indian rupee, daily since 2006

[![Chart of Singapore dollar to Indian rupee, daily since 2006, from Numbers.sg](https://numbers.sg/charts/sgd-to-inr-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-inr/)

Rupees per Singapore dollar and Singapore dollars per 100 rupees, each working day since 2006: MAS's noon rate where MAS publishes one, and earlier days from the source named on each row.

**The question it answers:** What is the Singapore dollar worth in rupees, on any working day since 2006?

| | |
|---|---|
| Rows | 5,246 |
| Each row | One working day |
| Covers | 3 Jan 2006 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-inr/](https://numbers.sg/currency/sgd-to-inr/) |

## Download

- CSV: [`fx-sgd-inr.csv`](fx-sgd-inr.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-inr/fx-sgd-inr.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-inr.json`](fx-sgd-inr.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-inr` (newest rows), `https://numbers.sg/api/v1/fx-sgd-inr/history` (every row), `https://numbers.sg/api/v1/fx-sgd-inr.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-inr/fx-sgd-inr.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-inr/fx-sgd-inr.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-inr.csv")`

## The last row

| Field | Value |
|---|---|
| `date` | 2026-11-26 |
| `inr_per_sgd` | 71.63837 |
| `sgd_per_100_inr` | 1.3959 |
| `source` | MAS |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `date` | date | The day the rate is for. |
| `inr_per_sgd` | number | How many rupees one Singapore dollar buys (the inverse of the next column, kept to six decimals). Unit: rupees per S$1. |
| `sgd_per_100_inr` | number | Singapore dollars per 100 rupees, the way MAS quotes it. Unit: S$ per 100 rupees. |
| `source` | string | Which figure the row is: MAS = MAS, as of noon. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-inr/#method](https://numbers.sg/currency/sgd-to-inr/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-inr/changes.atom`](https://numbers.sg/api/v1/fx-sgd-inr/changes.atom).

## Corrections

Each mistake found in this dataset or on its page, newest first. The same list is on [numbers.sg/corrections](https://numbers.sg/corrections/).

- **26 Nov 2026:** SGD to INR: the CSV’s note said it held SingStat’s monthly averages for the years before the daily record, but the file had none of them. It now ends with a second table of SingStat’s monthly averages of MAS’s rupee figures, 250 months from January 2006 to October 2026, and the chart’s key no longer lists a SingStat line that is not drawn.
- **7 Nov 2026:** SGD to INR: the summary and search description said the page had every day since 2008. MAS’s daily rupee rate begins on 3 January 2006, and the page now says so. A record date read “In 3 January”; it now reads “On”.
- **2 Nov 2026:** on our SGD to INR page, under “Is today’s rate good?”, the sentence on changing rupees into S$ said your rupees bought fewer S$ today than on a share of days, but gave the share of days on which they bought fewer S$ than today, the opposite. It now gives the right share. The table beside it and the figures for changing S$ into rupees were right.

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/currency/sgd-to-inr/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore dollar to Indian rupee, daily since 2006 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). Singapore dollar to Indian rupee, daily since 2006 [Data set]. https://numbers.sg/currency/sgd-to-inr/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_sgd_inr,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Indian rupee, daily since 2006}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-inr/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-inr/as-of/YYYY-MM-DD`.
