import streamlit as st
import pandas as pd
from datetime import date

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="Concorso PNRR3 - A028 Sicilia",
    page_icon="📚",
    layout="wide"
)

# --- FUNZIONI DI UTILITÀ ---
def load_data():
    # In un caso reale, qui caricheresti un CSV o un Database
    # Simuliamo dei dati per la graduatoria provvisoria
    data = {
        'Posizione': [1, 2, 3, 4, 5],
        'Protocollo': ['X123', 'Y456', 'Z789', 'A001', 'B002'],
        'Punteggio Totale': [180.5, 178.0, 175.5, 170.0, 168.5],
        'Titoli': [50, 48, 45, 40, 38],
        'Prova Scritta': [90, 92, 88, 90, 85],
        'Prova Orale': [40.5, 38, 42.5, 40, 45.5]
    }
    return pd.DataFrame(data)

# --- SIDEBAR (NAVIGAZIONE) ---
st.sidebar.title("Navigazione")
scelta = st.sidebar.radio("Vai a:", ["Home", "News & Avvisi", "Graduatorie A028", "Risorse Utili"])

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Info App:**
    Questa app è non ufficiale.
    Tutti i dati devono essere verificati sul sito USR Sicilia.
    """
)

# --- PAGINA HOME ---
if scelta == "Home":
    st.title("📚 Concorso Scuola PNRR3 - Sicilia")
    st.subheader("Classe di Concorso A028 (Matematica e Scienze)")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_Repubblica_Italiana.svg/1200px-Logo_Repubblica_Italiana.svg.png", width=100)
    
    st.markdown("""
    Benvenuto nel portale informativo dedicato ai candidati della **CdC A028 per la regione Sicilia**.
    
    Qui potrai trovare rapidamente:
    * 📅 **Calendari** delle prove orali.
    * 📍 **Sedi** di esame estratte.
    * 🏆 **Graduatorie** (non appena pubblicate).
    * 📢 **Avvisi** dell'USR Sicilia.
    
    > **Nota Bene:** Questa piattaforma aggrega informazioni per facilitare la consultazione. Fai sempre riferimento a [USR Sicilia](https://www.usr.sicilia.it/).
    """)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Posti Disponibili (Stimati)", "XXX", "In aggiornamento")
    col2.metric("Candidati Ammessi Orale", "1.250", "+50 rispetto a ieri")
    col3.metric("Giorni alla fine prove", "15", "-1")

# --- PAGINA NEWS ---
elif scelta == "News & Avvisi":
    st.header("📢 Ultime Notizie USR Sicilia")
    
    # Esempio di news
    news_list = [
        {"data": "2024-05-20", "titolo": "Pubblicazione Calendario Prova Orale (Turno 3)", "dettagli": "Disponibile il calendario per i cognomi dalla M alla P."},
        {"data": "2024-05-15", "titolo": "Estrazione Lettera Alfabetica", "dettagli": "La lettera estratta per l'inizio delle prove orali A028 è la 'R'."},
        {"data": "2024-05-10", "titolo": "Griglie di Valutazione", "dettagli": "Pubblicate le griglie di valutazione per la prova pratica."}
    ]
    
    for news in news_list:
        with st.expander(f"{news['data']} - {news['titolo']}"):
            st.write(news['dettagli'])

# --- PAGINA GRADUATORIE ---
elif scelta == "Graduatorie A028":
    st.header("🏆 Graduatorie e Simulazioni")
    st.write("Esempio di visualizzazione dati (Simulazione):")
    
    df = load_data()
    
    # Filtri interattivi
    min_score = st.slider("Filtra per punteggio minimo totale:", 100.0, 200.0, 160.0)
    df_filtered = df[df['Punteggio Totale'] >= min_score]
    
    st.dataframe(df_filtered, use_container_width=True)
    
    st.download_button(
        label="Scarica Dati in CSV",
        data=df_filtered.to_csv(index=False).encode('utf-8'),
        file_name='graduatoria_simulata_a028.csv',
        mime='text/csv',
    )

# --- PAGINA RISORSE ---
elif scelta == "Risorse Utili":
    st.header("🔗 Link e Materiali")
    
    st.markdown("""
    ### Siti Ufficiali
    * [Ministero dell'Istruzione e del Merito](https://www.miur.gov.it/)
    * [USR Sicilia - Sezione Concorsi](https://www.usr.sicilia.it/)
    * [Portale InPA](https://www.inpa.gov.it/)
    
    ### Gruppi di Studio
    * Canale Telegram A028 Sicilia (Esempio)
    * Gruppo Facebook Concorso PNRR
    
    ### Materiali Didattici
    Qui puoi caricare PDF o link a drive condivisi.
    """)
    
    # Esempio form di contatto
    st.markdown("---")
    st.subheader("Segnala una notizia")
    with st.form("segnalazione"):
        nome = st.text_input("Il tuo nome")
        msg = st.text_area("Messaggio/Notizia")
        submitted = st.form_submit_button("Invia Segnalazione")
        if submitted:
            st.success("Grazie! La tua segnalazione è stata ricevuta.")