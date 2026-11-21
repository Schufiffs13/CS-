# AI citation: file skeleton (function names, inputs, docstrings) generated with
# Claude (Anthropic), 20.11.2026, prompted and reviewed by Laura Niklaus.
# Test cases and reference example also generated with Claude.
"""Automatic checks of the deal formulas — owner: Laura.

Run with:  pytest
Reference example (calculated by hand):
  Acquirer: net income 1000, 500 shares, price 40  -> EPS 2.00
  Target:   net income 200, 100 shares, price 30
  Premium 30 %  -> price paid 3900 -> 97.5 new shares
  Pro forma EPS 1200 / 597.5 = 2.008 -> +0.4 % (accretive)
  Break-even premium = 33.3 %
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from finance import (acquisition_price, new_shares_issued,
                     pro_forma_eps, accretion_dilution)


def test_acquisition_price():
    assert acquisition_price(30, 100, 0.30) == pytest.approx(3900)


def test_new_shares_issued():
    assert new_shares_issued(3900, 40) == pytest.approx(97.5)


def test_pro_forma_eps():
    assert pro_forma_eps(1000, 200, 500, 97.5) == pytest.approx(2.008, abs=0.001)


def test_accretion_dilution():
    assert accretion_dilution(2.00, 2.008) == pytest.approx(0.004, abs=0.0005)
