# AI citation: file skeleton (function names, inputs, docstrings) generated with
# Claude (Anthropic), 20.11.2026, prompted and reviewed by Laura Niklaus.
"""Financial logic module — owner: Illia (& Noelle).

All deal calculations. Pure functions: numbers in, numbers out.
"""


def acquisition_price(target_price: float, target_shares: float, premium: float) -> float:
    """Total price paid for the target.  premium: 0.30 means 30 %."""
    raise NotImplementedError("TODO Illia")


def new_shares_issued(purchase_price: float, acquirer_price: float) -> float:
    """Number of new acquirer shares needed to pay (all-stock deal)."""
    raise NotImplementedError("TODO Illia")


def pro_forma_eps(acquirer_income: float, target_income: float,
                  acquirer_shares: float, new_shares: float) -> float:
    """EPS of the combined company after the deal."""
    raise NotImplementedError("TODO Illia")


def accretion_dilution(eps_before: float, eps_after: float) -> float:
    """Change in EPS in decimal form. +0.004 = +0.4 % (accretive)."""
    raise NotImplementedError("TODO Illia")


def break_even_premium(acquirer: dict, target: dict) -> float:
    """Highest premium (decimal) at which the deal is not dilutive."""
    raise NotImplementedError("TODO Illia (week 2)")
