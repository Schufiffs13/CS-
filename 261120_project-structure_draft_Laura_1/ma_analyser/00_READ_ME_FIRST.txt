M&A ANALYSER - WHO WORKS ON WHICH FILE
=======================================

Each person has ONE file. Open your file and fill in the places marked "TODO".
Do not change the function names or inputs - otherwise the parts won't fit together.


FILE                     PERSON     WHAT GOES IN IT
----------------------   --------   ------------------------------------------
finance.py               Illia      Deal calculations (purchase price, pro forma
                                    EPS, accretion/dilution, break-even premium)

data.py                  Noelle     Getting company data from yfinance + saving
                                    a CSV backup in the "data" folder

ml_model.py              Ivan       Training the regression and calculating the
                                    fair P/E and fair share price

app.py                   Flurin     The Streamlit interface (selectors, sliders,
                                    charts, result table)

tests/test_finance.py    Laura      Checks that the calculations give the right
README.md                           results; project description and instructions
requirements.txt                    (Laura puts everything together at the end)


HOW TO WORK ON YOUR FILE
------------------------
1. Open your file (e.g. finance.py).
2. Find the line that says  raise NotImplementedError("TODO ...")
3. Delete that line and write your code in its place.
4. Save, rename the file with our naming rule, upload it to Teams.
   Example: 261122_finance_current_Illia.py
5. Laura collects the latest version of each file, renames it back to the
   fixed name (finance.py etc.) and puts the app together.


RULES SO EVERYTHING FITS TOGETHER
---------------------------------
- Keep the function names exactly as they are.
- Percentages are always decimals: 30 % = 0.30
- The full list of functions and what they return is in README.md.
