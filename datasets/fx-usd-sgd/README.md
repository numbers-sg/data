# US dollar to Singapore dollar, daily since 1981

[![Chart of US dollar to Singapore dollar, daily since 1981, from Numbers.sg](https://numbers.sg/charts/usd-to-sgd-exchange-rate-chart.png)](https://numbers.sg/currency/usd-to-sgd/)

Singapore dollars per US dollar and US dollars per Singapore dollar since 1981: MAS's noon rate (daily from 2003, weekly from 1988) and, from 1981 to 1987, the US Federal Reserve's H.10 noon buying rates.

**The question it answers:** How many Singapore dollars is one US dollar, on any day since 1981?

| | |
|---|---|
| Rows | 8,541 |
| Each row | One working day (one week from 1988 to 2002) |
| Covers | 2 Jan 1981 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS), Federal Reserve Board |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/usd-to-sgd/](https://numbers.sg/currency/usd-to-sgd/) |

## Download

- CSV: [`fx-usd-sgd.csv`](fx-usd-sgd.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-usd-sgd/fx-usd-sgd.csv`
- JSON, with the field list, sources and notices: [`fx-usd-sgd.json`](fx-usd-sgd.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-usd-sgd` (newest rows), `https://numbers.sg/api/v1/fx-usd-sgd/history` (every row), `https://numbers.sg/api/v1/fx-usd-sgd.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-usd-sgd/fx-usd-sgd.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-usd-sgd/fx-usd-sgd.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-usd-sgd.csv")`

## The last row

| Field | Value |
|---|---|
| `date` | 2026-11-26 |
| `sgd_per_usd` | 1.2901 |
| `usd_per_sgd` | 0.775134 |
| `source` | MAS |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `date` | date | The day the rate is for. |
| `sgd_per_usd` | number | Singapore dollars per US dollar, the way MAS quotes it. Unit: S$ per US$1. |
| `usd_per_sgd` | number | US dollars one Singapore dollar buys (the inverse, kept to six decimals). Unit: US$ per S$1. |
| `source` | string | Which figure the row is: MAS = MAS, as of noon; Federal Reserve H.10 = the US Federal Reserve's H.10 noon buying rates (1981 to 1987). |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)
- [Federal Reserve Board](https://www.federalreserve.gov/releases/h10/current/), under the [Federal Reserve Board website: public domain](https://www.federalreserve.gov/disclaimer.htm)

How each figure is read and checked: [numbers.sg/currency/usd-to-sgd/#method](https://numbers.sg/currency/usd-to-sgd/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-usd-sgd/changes.atom`](https://numbers.sg/api/v1/fx-usd-sgd/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore and Federal Reserve Board, compiled by Numbers.sg (numbers.sg/currency/usd-to-sgd/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from US dollar to Singapore dollar, daily since 1981 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

> Source: Board of Governors of the Federal Reserve System (H.10)

To cite it:

```
Numbers.sg (2026). US dollar to Singapore dollar, daily since 1981 [Data set]. https://numbers.sg/currency/usd-to-sgd/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_usd_sgd,
  author = {{Numbers.sg}},
  title = {{US dollar to Singapore dollar, daily since 1981}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/usd-to-sgd/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-usd-sgd/as-of/YYYY-MM-DD`.
