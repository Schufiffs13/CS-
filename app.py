# =====================================================================
# M&A Analyser - Streamlit-Oberflaeche (Grundgeruest)
# Rolle 4: Streamlit & Visualization
#
# KI-HINWEIS (gemaess HSG-Regeln zitieren!):
# Dieses Grundgeruest wurde mit Claude (Anthropic) erstellt, 17.11.2026.
# Prompt sinngemaess: "Grundgeruest fuer die Streamlit-Oberflaeche des
# M&A Analysers mit Platzhalter-Daten".
#
# Starten im Terminal:   streamlit run app.py
#
# ALLE ZAHLEN SIND PLATZHALTER. Die Funktionen im Abschnitt 1 werden
# spaeter durch die echten Funktionen der anderen ersetzt.
# =====================================================================

import streamlit as st
import pandas as pd


# ---------------------------------------------------------------------
# 1) PLATZHALTER - spaeter ersetzen
# ---------------------------------------------------------------------

# TODO: ersetzen durch die Firmenliste von Noelle (Daten & API)
FIRMEN = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]


# TODO: ersetzen durch Illias Deal-Berechnung (Finanzlogik)
def platzhalter_deal(kaeufer, ziel, praemie, anteil_aktien):
    """Fake-Berechnung. Gibt ein Dictionary mit den Deal-Resultaten zurück."""
    eps_vorher = 5.00
    veraenderung = 8 - praemie * 0.25          # erfundene Formel
    eps_nachher = eps_vorher * (1 + veraenderung / 100)
    return {
        "eps_vorher": eps_vorher,
        "eps_nachher": eps_nachher,
        "veraenderung_prozent": veraenderung,
        "breakeven_praemie": 32.0,             # dort wird veraenderung = 0
    }


# TODO: ersetzen durch Illias Sensitivitäts-Engine
def platzhalter_sensitivitaet(kaeufer, ziel, anteil_aktien):
    """Fake-Sensitivität: EPS-Veränderung für Prämien von 0 bis 100 %."""
    praemien = list(range(0, 101, 5))           # 0, 5, 10, ..., 100
    werte = [8 - p * 0.25 for p in praemien]    # gleiche erfundene Formel
    return pd.DataFrame({"Prämie in %": praemien,
                         "EPS-Veränderung in %": werte})


# TODO: ersetzen durch Ivans ML-Modell
def platzhalter_ml(ziel):
    """Fake-ML-Resultat: fairer P/E und fairer Preis der Zielfirma."""
    return {"fairer_pe": 22.5, "aktueller_pe": 20.0,
            "fairer_preis": 112.50, "aktueller_preis": 100.00}


# ---------------------------------------------------------------------
# 2) SEITE EINRICHTEN
# ---------------------------------------------------------------------
st.set_page_config(page_title="M&A Analyser", layout="wide")
st.title("M&A Analyser")


# ---------------------------------------------------------------------
# 3) SIDEBAR = die "Hebel" (Eingaben des Users)
# ---------------------------------------------------------------------
st.sidebar.header("Deal-Parameter")

kaeufer = st.sidebar.selectbox("Käufer", FIRMEN, index=1)
ziel = st.sidebar.selectbox("Zielfirma", FIRMEN, index=0)

praemie = st.sidebar.slider("Übernahmeprämie (%)", 0, 100, 30)

# TODO: mit Illia klären, ob seine Formeln diese Inputs brauchen
anteil_aktien = st.sidebar.slider(
    "Finanzierung in Aktien (%)", 0, 100, 50,
    help="Der Rest wird mit Cash bzw. neuen Schulden bezahlt.")
zinssatz = st.sidebar.number_input(
    "Zinssatz auf neue Schulden (%)", min_value=0.0, max_value=20.0,
    value=5.0, step=0.5)
steuersatz = st.sidebar.number_input(
    "Steuersatz (%)", min_value=0.0, max_value=50.0, value=20.0, step=1.0)


# ---------------------------------------------------------------------
# 4) FEHLER ABFANGEN
# ---------------------------------------------------------------------
if kaeufer == ziel:
    st.warning("Bitte zwei verschiedene Firmen auswählen.")
    st.stop()   # bricht hier ab, alles darunter wird nicht angezeigt


# ---------------------------------------------------------------------
# 5) BERECHNUNG AUFRUFEN (später: echte Funktionen)
# ---------------------------------------------------------------------
deal = platzhalter_deal(kaeufer, ziel, praemie, anteil_aktien)
sensitivitaet = platzhalter_sensitivitaet(kaeufer, ziel, anteil_aktien)
ml = platzhalter_ml(ziel)

st.caption(f"{kaeufer} übernimmt {ziel} mit {praemie} % Prämie, "
           f"davon {anteil_aktien} % in Aktien finanziert.")


# ---------------------------------------------------------------------
# 6) KENNZAHLEN (Metrics)
# ---------------------------------------------------------------------
if deal["veraenderung_prozent"] >= 0:
    ergebnis = "Accretive"
else:
    ergebnis = "Dilutive"

spalte1, spalte2, spalte3, spalte4 = st.columns(4)
spalte1.metric("EPS Käufer allein", f"{deal['eps_vorher']:.2f}")
spalte2.metric("EPS pro forma", f"{deal['eps_nachher']:.2f}",
               delta=f"{deal['veraenderung_prozent']:+.1f} %")
spalte3.metric("Ergebnis", ergebnis)
spalte4.metric("Break-even-Prämie", f"{deal['breakeven_praemie']:.1f} %")


# ---------------------------------------------------------------------
# 7) GRAFIKEN
# ---------------------------------------------------------------------
links, rechts = st.columns(2)

with links:
    st.subheader("EPS vorher vs. nachher")
    eps_daten = pd.DataFrame(
        {"EPS": [deal["eps_vorher"], deal["eps_nachher"]]},
        index=["Käufer allein", "Nach Deal (pro forma)"])
    st.bar_chart(eps_daten)

with rechts:
    st.subheader("Prämien-Sensitivität")
    st.line_chart(sensitivitaet, x="Prämie in %", y="EPS-Veränderung in %")
    st.caption("Wo die Linie die Null schneidet, liegt die Break-even-Prämie.")


# ---------------------------------------------------------------------
# 8) BERECHNUNGSTABELLE
# ---------------------------------------------------------------------
st.subheader("Berechnung Schritt für Schritt")
tabelle = pd.DataFrame({
    "Schritt": ["Kaufpreis Zielfirma",
                "Neu ausgegebene Aktien",
                "Kombinierter Gewinn",
                "Aktien nach dem Deal",
                "EPS pro forma"],
    "Wert": ["folgt (Illia)", "folgt (Illia)", "folgt (Illia)",
             "folgt (Illia)", f"{deal['eps_nachher']:.2f}"],
})
st.dataframe(tabelle, hide_index=True)


# ---------------------------------------------------------------------
# 9) MACHINE-LEARNING-RESULTAT
# ---------------------------------------------------------------------
st.subheader(f"Machine Learning: fairer P/E von {ziel}")

ml_links, ml_rechts = st.columns(2)
ml_links.metric("Vorhergesagter fairer P/E", f"{ml['fairer_pe']:.1f}",
                delta=f"{ml['fairer_pe'] - ml['aktueller_pe']:+.1f} vs. aktuell")
ml_rechts.metric("Fairer Aktienpreis", f"{ml['fairer_preis']:.2f}",
                 delta=f"{ml['fairer_preis'] - ml['aktueller_preis']:+.2f} vs. Kurs")
st.caption("Platzhalter – das echte Regressionsmodell folgt von Ivan.")