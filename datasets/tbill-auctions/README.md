# Singapore T-bill auction results

[![Chart of Singapore T-bill auction results, from Numbers.sg](https://numbers.sg/charts/t-bill-yield-chart.png)](https://numbers.sg/rates/t-bills/)

Every MAS auction of 6-month and 1-year Singapore Treasury bills since May 1987: the cut-off yield and price, the yield on the cash you actually pay, the median and average yields, the amount sold, total bids and how much of each kind of bid was filled.

**The question it answers:** What yield did each 6-month and 1-year T-bill auction give, since 1987?

| | |
|---|---|
| Rows | 343 |
| Each row | One T-bill auction (one issue) |
| Covers | 25 May 1987 to 19 Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/rates/t-bills/](https://numbers.sg/rates/t-bills/) |

## Download

- CSV: [`tbill-auctions.csv`](tbill-auctions.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/tbill-auctions/tbill-auctions.csv`
- JSON, with the field list, sources and notices: [`tbill-auctions.json`](tbill-auctions.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/tbill-auctions` (newest rows), `https://numbers.sg/api/v1/tbill-auctions/history` (every row), `https://numbers.sg/api/v1/tbill-auctions.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/tbill-auctions/tbill-auctions.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/tbill-auctions/tbill-auctions.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/tbill-auctions.csv")`

## The last row

| Field | Value |
|---|---|
| `auction_date` | 2026-11-19 |
| `tbill` | 6-month |
| `issue_code` | BS26123A |
| `issue_date` | 2026-11-24 |
| `maturity_date` | 2027-05-25 |
| `days` | 182 |
| `cutoff_yield_pct` | 2.07 |
| `cutoff_price_sgd_per_100` | 98.968 |
| `yield_on_cash_paid_pct` | 2.09 |
| `median_yield_pct` | 2 |
| `average_yield_pct` | 1.88 |
| `amount_sold_sgd_m` | 8600 |
| `bids_sgd_m` | 17102.787 |
| `bid_to_cover` | 1.99 |
| `non_competitive_filled_pct` | 100 |
| `competitive_at_cutoff_filled_pct` | 90.91 |
| `source` | MAS SGS auction results; compiled by Numbers.sg |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `auction_date` | date | The day the auction closed and the result was published. |
| `tbill` | string | Which T-bill: 6-month or 1-year. |
| `issue_code` | string | MAS's issue code, the code you apply for at a bank or ATM. |
| `issue_date` | date | The day the T-bill is issued and paid for. |
| `maturity_date` | date | The day it pays back its face value. |
| `days` | integer | Days from issue to maturity. Unit: days. |
| `cutoff_yield_pct` | number | The cut-off yield: the highest yield MAS accepted, which every successful bidder gets. Unit: percent a year. |
| `cutoff_price_sgd_per_100` | number | What you pay for every S$100 you get back at maturity. Unit: S$ per S$100 of face value. |
| `yield_on_cash_paid_pct` | number | The return on the cash you actually pay (the discounted price), which is a little above the cut-off yield. Unit: percent a year. |
| `median_yield_pct` | number | The median yield of the competitive bids that were accepted; MAS records none before November 2009. Unit: percent a year. Empty when the source gave no figure. |
| `average_yield_pct` | number | The average yield of the competitive bids that were accepted. Unit: percent a year. |
| `amount_sold_sgd_m` | number | How much MAS sold at the auction. Unit: S$ million. |
| `bids_sgd_m` | number | How much was bid for in total. Unit: S$ million. |
| `bid_to_cover` | number | Total bids divided by the amount sold: above 1 means more was asked for than was sold. Unit: ratio (bids ÷ amount sold). |
| `non_competitive_filled_pct` | number | How much of each non-competitive bid (no yield named, the usual choice for individuals) was filled; none before the 27 Nov 2002 auction, the first where MAS records non-competitive bids allotted. Unit: percent of the amount asked for. Empty when it does not apply to that row. |
| `competitive_at_cutoff_filled_pct` | number | How much of each competitive bid at exactly the cut-off yield was filled; bids at a lower yield were filled in full. Unit: percent of the amount asked for. |
| `source` | string | Where the row comes from. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/rates/t-bills/#method](https://numbers.sg/rates/t-bills/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/tbill-auctions/changes.atom`](https://numbers.sg/api/v1/tbill-auctions/changes.atom).

## Corrections

None so far for this dataset or its page. Every correction on the site is listed on [numbers.sg/corrections](https://numbers.sg/corrections/).

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/rates/t-bills/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from SGS auction results and issuance calendar accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). Singapore T-bill auction results [Data set]. https://numbers.sg/rates/t-bills/
```

```bibtex
@misc{numberssg_tbill_auctions,
  author = {{Numbers.sg}},
  title = {{Singapore T-bill auction results}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/rates/t-bills/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/tbill-auctions/as-of/YYYY-MM-DD`.
