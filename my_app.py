import streamlit as st

# set some configurations of our app
st.set_page_config(
    page_title="Mergers and Acquisitions Analyser",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="auto",
)

# first titel and subtitel for steamlit
st.title("Mergers and Acquisitions Analyser")
st.header("Does the earnings of the share of the buyer rise (accretive) or fall (dilutive) after the takeover?")
st.write("This application checks whether an acquisition increases or decreases the acquirer's earning per share (EPS). Select an acquirer and a target, then adjust the takeover premium and the financing mix. In addition, a machine learning model estimates the target's fair Price to Earning-Ratio (P/E) and shows whether its current share price looks cheap or expensive.")