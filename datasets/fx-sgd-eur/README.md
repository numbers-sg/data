# Singapore dollar to euro, daily since 1999

[![Chart of Singapore dollar to euro, daily since 1999, from Numbers.sg](https://numbers.sg/charts/eur-to-sgd-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-eur/)

Euros per Singapore dollar and Singapore dollars per euro, each working day since 1999: MAS's noon rate where MAS publishes one, and earlier days from the source named on each row.

**The question it answers:** What is the Singapore dollar worth in euros, on any working day since 1999?

| | |
|---|---|
| Rows | 7,024 |
| Each row | One working day |
| Covers | 4 Jan 1999 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS), European Central Bank |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-eur/](https://numbers.sg/currency/sgd-to-eur/) |

## Download

- CSV: [`fx-sgd-eur.csv`](fx-sgd-eur.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-eur/fx-sgd-eur.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-eur.json`](fx-sgd-eur.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-eur` (newest rows), `https://numbers.sg/api/v1/fx-sgd-eur/history` (every row), `https://numbers.sg/api/v1/fx-sgd-eur.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-eur/fx-sgd-eur.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-eur/fx-sgd-eur.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-eur.csv")`

## The last row

| Field | Value |
|---|---|
| `date` | 2026-11-26 |
| `eur_per_sgd` | 0.707214 |
| `sgd_per_eur` | 1.413999 |
| `source` | MAS |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `date` | date | The day the rate is for. |
| `eur_per_sgd` | number | How many euros one Singapore dollar buys (the inverse of the next column, kept to six decimals). Unit: euros per S$1. |
| `sgd_per_eur` | number | Singapore dollars per euro, the way MAS quotes it. Unit: S$ per euro. |
| `source` | string | Which figure the row is: ECB = the ECB's euro reference rates, crossed (before MAS's daily record); MAS = MAS, as of noon. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)
- [European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html), under the [ECB copyright and reuse rules](https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html)

How each figure is read and checked: [numbers.sg/currency/sgd-to-eur/#method](https://numbers.sg/currency/sgd-to-eur/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-eur/changes.atom`](https://numbers.sg/api/v1/fx-sgd-eur/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore and European Central Bank, compiled by Numbers.sg (numbers.sg/currency/sgd-to-eur/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore dollar to euro, daily since 1999 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

> Source: European Central Bank; SGD cross rates calculated by Numbers.sg

To cite it:

```
Numbers.sg (2026). Singapore dollar to euro, daily since 1999 [Data set]. https://numbers.sg/currency/sgd-to-eur/
```

```bibtex
@misc{numberssg_fx_sgd_eur,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to euro, daily since 1999}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-eur/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-eur/as-of/YYYY-MM-DD`.
