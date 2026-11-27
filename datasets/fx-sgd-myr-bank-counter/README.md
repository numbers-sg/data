# Malaysian banks' counter rates for the Singapore dollar, daily since 2021

[![Chart of Malaysian banks' counter rates for the Singapore dollar, daily since 2021, from Numbers.sg](https://numbers.sg/charts/sgd-to-myr-exchange-rate-chart.png)](https://numbers.sg/currency/sgd-to-myr/)

Bank Negara Malaysia's 11:30 am figures for the best counter rates selected Malaysian commercial banks offered for the Singapore dollar, buying and selling, each working day since January 2021.

**The question it answers:** What do Malaysian banks pay and charge in ringgit for Singapore dollars at the counter?

| | |
|---|---|
| Rows | 1,444 |
| Each row | One working day (BNM's 11:30 am figure) |
| Covers | 4 Jan 2021 to 26 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Bank Negara Malaysia (BNM) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-myr/](https://numbers.sg/currency/sgd-to-myr/) |

## Download

- CSV: [`fx-sgd-myr-bank-counter.csv`](fx-sgd-myr-bank-counter.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr-bank-counter/fx-sgd-myr-bank-counter.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-myr-bank-counter.json`](fx-sgd-myr-bank-counter.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-myr-bank-counter` (newest rows), `https://numbers.sg/api/v1/fx-sgd-myr-bank-counter/history` (every row), `https://numbers.sg/api/v1/fx-sgd-myr-bank-counter.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr-bank-counter/fx-sgd-myr-bank-counter.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-myr-bank-counter/fx-sgd-myr-bank-counter.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-myr-bank-counter.csv")`

## The last row

| Field | Value |
|---|---|
| `date` | 2026-11-26 |
| `banks_buy_myr_per_sgd` | 3.1674 |
| `banks_sell_myr_per_sgd` | 3.2094 |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `date` | date | The day of the rates. |
| `banks_buy_myr_per_sgd` | number | The best rate the banks pay for a Singapore dollar (what you get selling S$ to them). Unit: ringgit per S$1. |
| `banks_sell_myr_per_sgd` | number | The best rate the banks sell a Singapore dollar at (what you pay buying S$ from them). Unit: ringgit per S$1. |

## Where the numbers come from

- [Bank Negara Malaysia (BNM)](https://www.bnm.gov.my/exchange-rates), under the [Terms of Use for BNM Datasets](https://www.bnm.gov.my/terms-of-use-bnm-datasets)

How each figure is read and checked: [numbers.sg/currency/sgd-to-myr/#method](https://numbers.sg/currency/sgd-to-myr/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-myr-bank-counter/changes.atom`](https://numbers.sg/api/v1/fx-sgd-myr-bank-counter/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Bank Negara Malaysia, compiled by Numbers.sg (numbers.sg/currency/sgd-to-myr/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Source: Bank Negara Malaysia. Data and information are subject to Terms of Use for BNM Datasets (https://www.bnm.gov.my/terms-of-use-bnm-datasets)

To cite it:

```
Numbers.sg (2026). Malaysian banks' counter rates for the Singapore dollar, daily since 2021 [Data set]. https://numbers.sg/currency/sgd-to-myr/
```

```bibtex
@misc{numberssg_fx_sgd_myr_bank_counter,
  author = {{Numbers.sg}},
  title = {{Malaysian banks' counter rates for the Singapore dollar, daily since 2021}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-myr/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-myr-bank-counter/as-of/YYYY-MM-DD`.
