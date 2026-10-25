import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import ollama

# 1. Configurazione Database PostgreSQL
DB_USER = "postgres"
DB_PASSWORD = "root"  # La tua password di PostgreSQL
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce_analytics"

connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

# Schema del database da dare in pasto all'AI come contesto
db_schema = """
Il database PostgreSQL ha tre tabelle:
1. clienti (id_cliente, nome, cognome, email, citta, data_registrazione)
2. prodotti (id_prodotto, nome_prodotto, categoria, prezzo, stock)
3. ordini (id_ordine, id_cliente, id_prodotto, quantita, prezzo_totale, data_ordine)
"""

def domanda_al_database(domanda_utente):
    print(f"\nDomanda in linguaggio naturale: '{domanda_utente}'")
    
    # 2. Prompt Engineering: istruiamo il modello locale a generare SOLO codice SQL valido
    prompt_sistema = f"""
    Sei un Data Analyst esperto di PostgreSQL. 
    Dato il seguente schema di database:
    {db_schema}
    
    Traduci la domanda dell'utente in una query SQL PostgreSQL valida.
    REGOLE FONDAMENTALI:
    - Restituisci unicamente il codice SQL puro, senza blocchi di codice markdown (senza ```sql o ```), senza spiegazioni, senza testo introduttivo.
    - Usa i nomi corretti delle tabelle e delle colonne dello schema.
    """

    try:
        # Chiamata al modello locale tramite Ollama (usiamo llama3)
        response = ollama.chat(
            model='llama3',
            messages=[
                {'role': 'system', 'content': prompt_sistema},
                {'role': 'user', 'content': domanda_utente}
            ],
            options={'temperature': 0}
        )
        
        query_sql = response['message']['content'].strip()
        print(f"Query SQL generata dall'AI locale:\n{query_sql}\n")

        # 3. Esecuzione della query SQL sul database PostgreSQL
        df_risultato = pd.read_sql(query_sql, con=engine)
        
        print("--- RISULTATO DELL'ANALISI ---")
        print(df_risultato)
        return df_risultato

    except Exception as e:
        print(f"Errore durante l'elaborazione: {e}")

# --- TEST DEL SISTEMA ---
if __name__ == "__main__":
    domanda_al_database("Qual è il totale delle vendite raggruppate per categoria di prodotto?")