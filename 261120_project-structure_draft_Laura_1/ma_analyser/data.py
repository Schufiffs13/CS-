# AI citation: file skeleton (function names, inputs, docstrings) generated with
# Claude (Anthropic), 20.11.2026, prompted and reviewed by Laura Niklaus.
"""Data & API module — owner: Noelle (& Illia).

Fetches company figures from yfinance and saves/loads a CSV backup.
"""


def get_company_data(ticker: str) -> dict:
    """Return the key figures of ONE company.

    Input:  ticker, e.g. "NESN.SW"
    Output: dict with exactly these keys:
        {
            "ticker": str,
            "name": str,
            "net_income": float,      # yearly net profit
            "shares": float,          # number of shares outstanding
            "price": float,           # current share price
            "revenue_growth": float,  # e.g. 0.05 for 5 %
            "profit_margin": float,   # e.g. 0.12 for 12 %
        }
    If yfinance fails (no internet / wrong ticker): load from data/companies.csv.
    """
    raise NotImplementedError("TODO Noelle")


def get_training_data():
    """Return a pandas DataFrame with 50-80 companies for the ML model.

    Columns: ticker, pe, revenue_growth, profit_margin
    """
    raise NotImplementedError("TODO Noelle (week 2)")
