# Singapore dollar to Malaysian ringgit, daily since 1999

[![Chart of Singapore dollar to Malaysian ringgit, daily since 1999, from Numbers.sg](https://numbers.sg/charts/sgd-to-myr-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-myr/)

Ringgit per Singapore dollar each working day since 1999, from our cross of the ECB's euro reference rates, with Bank Negara Malaysia's noon interbank middle rate beside it from 2010.

**The question it answers:** What is the Singapore dollar worth in ringgit, on any working day since 1999?

| | |
|---|---|
| Rows | 7,145 |
| Each row | One working day |
| Covers | 4 Jan 1999 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | European Central Bank, Bank Negara Malaysia (BNM) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-myr/](https://numbers.sg/currency/sgd-to-myr/) |

## Download

- CSV: [`fx-sgd-myr.csv`](fx-sgd-myr.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr/fx-sgd-myr.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-myr.json`](fx-sgd-myr.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-myr` (newest rows), `https://numbers.sg/api/v1/fx-sgd-myr/history` (every row), `https://numbers.sg/api/v1/fx-sgd-myr.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr/fx-sgd-myr.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr/fx-sgd-myr.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-myr.csv")`

## The last row

| Field | Value |
|---|---|
| `date` | 2026-11-26 |
| `myr_per_sgd_ecb_cross` | 3.190708 |
| `myr_per_sgd_bnm_noon_middle` | 3.192 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `date` | date | The day the rate is for. |
| `myr_per_sgd_ecb_cross` | number | Our cross of the ECB's euro reference rates: ringgit per euro divided by S$ per euro. Unit: ringgit per S$1. |
| `myr_per_sgd_bnm_noon_middle` | number | Bank Negara Malaysia's noon interbank middle rate for the Singapore dollar; from January 2010. Unit: ringgit per S$1. Empty when the source gave no figure. |

## Where the numbers come from

- [European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html), under the [ECB copyright and reuse rules](https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html)
- [Bank Negara Malaysia (BNM)](https://www.bnm.gov.my/exchange-rates), under the [Terms of Use for BNM Datasets](https://www.bnm.gov.my/terms-of-use-bnm-datasets)

How each figure is read and checked: [numbers.sg/currency/sgd-to-myr/#method](https://numbers.sg/currency/sgd-to-myr/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-myr/changes.atom`](https://numbers.sg/api/v1/fx-sgd-myr/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: European Central Bank and Bank Negara Malaysia, compiled by Numbers.sg (numbers.sg/currency/sgd-to-myr/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: European Central Bank; SGD cross rates calculated by Numbers.sg

> Source: Bank Negara Malaysia. Data and information are subject to Terms of Use for BNM Datasets (https://www.bnm.gov.my/terms-of-use-bnm-datasets)

To cite it:

```
Numbers.sg (2026). Singapore dollar to Malaysian ringgit, daily since 1999 [Data set]. https://numbers.sg/currency/sgd-to-myr/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_fx_sgd_myr,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Malaysian ringgit, daily since 1999}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-myr/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-myr/as-of/YYYY-MM-DD`.
