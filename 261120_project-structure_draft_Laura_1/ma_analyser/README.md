# M&A Analyser

Streamlit app that shows whether an acquisition increases or decreases the
acquirer's earnings per share (EPS accretion/dilution) and estimates the
target's fair P/E with a self-trained linear regression.

## How to run
```
pip install -r requirements.txt
streamlit run app.py
```
Run the tests with `pytest`.

## Project structure
| File | Content | Owner |
|---|---|---|
| `data.py` | yfinance data + CSV backup | Noelle |
| `finance.py` | deal calculations | Illia |
| `ml_model.py` | P/E regression | Ivan |
| `app.py` | Streamlit interface | Flurin |
| `tests/` | automatic tests | Laura |

## Interfaces (agreed function names)
- `data.get_company_data(ticker) -> dict` with keys `ticker, name, net_income, shares, price, revenue_growth, profit_margin`
- `data.get_training_data() -> DataFrame` with columns `ticker, pe, revenue_growth, profit_margin`
- `finance.acquisition_price(target_price, target_shares, premium)`
- `finance.new_shares_issued(purchase_price, acquirer_price)`
- `finance.pro_forma_eps(acquirer_income, target_income, acquirer_shares, new_shares)`
- `finance.accretion_dilution(eps_before, eps_after)`
- `finance.break_even_premium(acquirer, target)`
- `ml_model.train_model(training_data) -> (model, r2)`
- `ml_model.fair_value(model, company) -> {"fair_pe", "fair_price"}`

Premiums and percentages are always decimals (0.30 = 30 %).

## Data sources
yfinance (Yahoo Finance). Offline backup: `data/companies.csv`. *(to be completed)*

## Limitations
*(to be completed in week 3)*

## Use of generative AI
- Project structure, function skeletons, tests and this README draft were generated with Claude (Anthropic) on 20.11.2026 and reviewed by the team. AI-generated code is cited at the top of each file.
- *(further AI use by each member to be completed in week 3)*
