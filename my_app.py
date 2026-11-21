import streamlit as st
## Startm for anaconda prompt: python -m streamlit run "C:\Users\fluri\OneDrive\Dokumente\GitHub\CS-\my_app.py"

# took this part from rock, papers, scissors 
st.set_page_config(
    page_title ="This is fun",
    page_icon =":shark:",
    layout ="centered",
)

# first titel and subtitel for steamlit
st.title("Mergers and Acquisitions Analyser")
st.header("Does the earnings of the share of the buyer rise (accretive) or fall (dilutive) after the takeover?")
st.write("""This application checks whether an acquisition increases or decreases the acquirer's earning per share (EPS). Select an acquirer and a target, 
then adjust the takeover premium and the financing mix. In addition, 
a machine learning model estimates the target's fair Price to Earning-Ratio (P/E) 
and shows whether its current share price looks cheap or expensive.""")

#List of the companies (placeholder until Data is ready)
companies = ["Apple", "Microsoft", "Google", "Aamazon", "Nvidia"]
st.sidebar.header("Deal Parameters") 
acquirer = st.sidebar.selectbox ("Acquirer", companies) #help with structure and this line of code 
target = st.sidebar.selectbox ("Target", companies, index = 1) #help for index by Anthropic Claude -->  Target starts with the 2nd company, so the default is not the same as the acquirer
premium = st.sidebar.slider ("Takeover Premium(%)", 0, 100, 25) #slider from streamlit cheat sheet 
premium_dec = premium/100
stock_finance = st.sidebar.slider ("Stock Financing(%)", 0, 100, 50)
stock_finance_dec = stock_finance/100
cash_share = 100- stock_finance
cash_share_dex = 1 - stock_finance_dec
interest_rate = st.sidebar.number_input ("Interest rate on new debt (%)", 0.0, 20.0, 5.0, step = 0.5) #needed help from Anthropic Claude for step = 
interest_rate_dec = interest_rate/100
tax_rate = st.sidebar.number_input ("Tax Rate (%)", 0.0 , 50.0, 20.0, step = 1.0)
tax_rate_dec = tax_rate/100
synergy = st.sidebar.number_input ("Synergies per year", min_value = 0.0, value = 0.0)


if acquirer == target:
    st.warning ("Please select another company for acquirer/target.")
    st.stop()

st.write(f"{acquirer} acquires {target} with a {premium}% premium, "f"financed {stock_finance}% in stock and {cash_share}% in cash.") #help from Anthropic Claude for errors and the f-string 

