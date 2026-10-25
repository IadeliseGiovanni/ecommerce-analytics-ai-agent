import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# 1. Configurazione della connessione al database PostgreSQL
# Formato: postgresql+psycopg2://utente:password@host:porta/nome_database
DB_USER = "postgres"
DB_PASSWORD = "root"  # Sostituisci con la tua password di postgres
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce_analytics"

# Creiamo l'engine di connessione
connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

try:
    print("Connessione al database stabilita con successo! 🚀")

    # 2. Estrazione (Extract): Leggiamo la query con la JOIN che hai testato prima
    query = """
        SELECT 
            o.id_ordine,
            c.nome || ' ' || c.cognome AS cliente,
            c.citta,
            p.nome_prodotto,
            p.categoria,
            o.quantita,
            o.prezzo_totale,
            o.data_ordine
        FROM ordini o
        JOIN clienti c ON o.id_cliente = c.id_cliente
        JOIN prodotti p ON o.id_prodotto = p.id_prodotto;
    """

    # Carichiamo i dati direttamente in un DataFrame Pandas
    df = pd.DataFrame(pd.read_sql(query, con=engine))

    print("\n--- DATI ESTRATTI NEL DATAFRAME PANDAS ---")
    print(df.head())

    # 3. Trasformazione (Transform) - Esempio pratico con Pandas
    # Calcoliamo ad esempio il totale delle vendite per categoria
    print("\n--- TOTALE VENDITE PER CATEGORIA ---")
    vendite_per_categoria = df.groupby("categoria")["prezzo_totale"].sum().reset_index()
    print(vendite_per_categoria)

except Exception as e:
    print(f"Errore durante l'esecuzione: {e}")