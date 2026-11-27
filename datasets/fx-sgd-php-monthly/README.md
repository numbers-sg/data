# Singapore dollar to Philippine peso, monthly averages since 2003

Monthly averages of the peso, worked out by Numbers.sg from MAS's daily rates for each complete month (the mean of MAS's S$ per 100 peso, turned round), since January 2003.

**The question it answers:** What was the average peso rate for the Singapore dollar each month since 2003?

| | |
|---|---|
| Rows | 286 |
| Each row | One month (the average of the month) |
| Covers | Jan 2003 to Oct 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/currency/sgd-to-php/](https://numbers.sg/currency/sgd-to-php/) |

## Download

- CSV: [`fx-sgd-php-monthly.csv`](fx-sgd-php-monthly.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-php-monthly/fx-sgd-php-monthly.csv`
- JSON, with the field list, sources and notices: [`fx-sgd-php-monthly.json`](fx-sgd-php-monthly.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/fx-sgd-php-monthly` (newest rows), `https://numbers.sg/api/v1/fx-sgd-php-monthly/history` (every row), `https://numbers.sg/api/v1/fx-sgd-php-monthly.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-php-monthly/fx-sgd-php-monthly.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/fx-sgd-php-monthly/fx-sgd-php-monthly.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/fx-sgd-php-monthly.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-10 |
| `php_per_sgd` | 49.350259 |
| `sgd_per_1000_php` | 20.263318 |
| `source` | Numbers.sg mean of MAS daily rates |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month averaged. |
| `php_per_sgd` | number | Pesos per S$1: our monthly mean of MAS's S$ figure, turned round. Unit: pesos per S$1. |
| `sgd_per_1000_php` | number | S$ per 1,000 pesos: our mean of MAS's daily figures for the month. Unit: S$ per 1,000 pesos. |
| `source` | string | Where the month's figure comes from. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/currency/sgd-to-php/#method](https://numbers.sg/currency/sgd-to-php/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/fx-sgd-php-monthly/changes.atom`](https://numbers.sg/api/v1/fx-sgd-php-monthly/changes.atom).

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/currency/sgd-to-php/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore dollar to Philippine peso, monthly averages since 2003 accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). Singapore dollar to Philippine peso, monthly averages since 2003 [Data set]. https://numbers.sg/currency/sgd-to-php/
```

```bibtex
@misc{numberssg_fx_sgd_php_monthly,
  author = {{Numbers.sg}},
  title = {{Singapore dollar to Philippine peso, monthly averages since 2003}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/currency/sgd-to-php/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/fx-sgd-php-monthly/as-of/YYYY-MM-DD`.
