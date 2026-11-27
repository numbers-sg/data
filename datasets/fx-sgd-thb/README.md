# Singapore dollar to Thai baht, daily since 1981

[![Chart of Singapore dollar to Thai baht, daily since 1981, from Numbers.sg](https://numbers.sg/charts/sgd-to-thb-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-thb/)

Baht per Singapore dollar and Singapore dollars per 1,000 baht, each working day since 1981: MAS's noon rate where MAS publishes one, and earlier days from the source named on each row.

**The question it answers:** What is the Singapore dollar worth in baht, on any working day since 1981?

| | |
|---|---|
| Rows | 11,442 |
| Each row | One working day |
| Covers | 2 Jan 1981 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS), Federal Reserve Board |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-thb/](https://numbers.sg/currency/sgd-to-thb/) |

## Download

- CSV: [`fx-sgd-thb.csv`](fx-sgd-thb.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-thb/fx-sgd-thb.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-thb.json`](fx-sgd-thb.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-thb` (newest rows), `https://numbers.sg/api/v1/fx-sgd-thb/history` (every row), `https://numbers.sg/api/v1/fx-sgd-thb.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-thb/fx-sgd-thb.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-thb/fx-sgd-thb.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-thb.csv")`

## The last row

| Field | Value |
|---|---|
| `date` | 2026-11-26 |
| `thb_per_sgd` | 26.359491 |
| `sgd_per_1000_thb` | 37.937 |
| `source` | MAS |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `date` | date | The day the rate is for. |
| `thb_per_sgd` | number | How many baht one Singapore dollar buys (the inverse of the next column, kept to six decimals). Unit: baht per S$1. |
| `sgd_per_1000_thb` | number | Singapore dollars per 1,000 baht, the way MAS quotes it. Unit: S$ per 1,000 baht. |
| `source` | string | Which figure the row is: FED-H10 = the US Federal Reserve's H.10 noon rates, crossed (before MAS's daily record); MAS = MAS, as of noon. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)
- [Federal Reserve Board](https://www.federalreserve.gov/releases/h10/current/), under the [Federal Reserve Board website: public domain](https://www.federalreserve.gov/disclaimer.htm)

How each figure is read and checked: [numbers.sg/currency/sgd-to-thb/#method](https://numbers.sg/currency/sgd-to-thb/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-thb/changes.atom`](https://numbers.sg/api/v1/fx-sgd-thb/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore and Federal Reserve Board, compiled by Numbers.sg (numbers.sg/currency/sgd-to-thb/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore dollar to Thai baht, daily since 1981 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

> Source: Board of Governors of the Federal Reserve System (H.10)

To cite it:

```
Numbers.sg (2026). Singapore dollar to Thai baht, daily since 1981 [Data set]. https://numbers.sg/currency/sgd-to-thb/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_sgd_thb,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Thai baht, daily since 1981}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-thb/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-thb/as-of/YYYY-MM-DD`.
