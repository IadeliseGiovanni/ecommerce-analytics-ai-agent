# 🛒 Local AI-Powered E-Commerce Data & Analytics Platform

Un progetto pratico end-to-end che unisce **Data Engineering** e **AI Engineering**, progettato con un approccio 100% locale, gratuito e orientato alla privacy, sfruttando **PostgreSQL**, **Python (Pandas/SQLAlchemy)** e un Large Language Model locale tramite **Ollama**.

---

## 🏗️ Architettura del Progetto

Il sistema si compone di due moduli principali:
1. **Pipeline ETL (Extract, Transform, Load):** Estrae dati di e-commerce simulati, li modella in Dataframe Pandas e li carica su un database relazionale **PostgreSQL**.
2. **Agent AI Text-to-SQL Locale:** Permette a un utente di fare domande in linguaggio naturale (es. *"Qual è il totale delle vendite per categoria?"*). Un LLM locale (**Llama 3**) traduce la richiesta in una query SQL sicura, che viene eseguita in tempo reale sul database per restituire l'analisi strutturata.

---

## 🛠️ Stack Tecnologico
* **Linguaggio:** Python 3.x
* **Database:** PostgreSQL & SQLAlchemy
* **Data Manipulation:** Pandas
* **AI & LLM:** Ollama (Llama 3) in esecuzione locale
* **Infrastruttura:** 100% Locale & Open Source (Zero costi API / Cloud)

---

## 📁 Struttura dei File
* `etl_pipeline.py` - Script per la creazione dello schema relazionale su PostgreSQL e il popolamento dei dati di test tramite ETL.
* `ai_agent.py` - Agente Text-to-SQL basato su LLM locale che interroga il database in linguaggio naturale.

---

## 🚀 Come Eseguirlo in Locale

1. **Clona o scarica il repository** e assicurati di avere PostgreSQL attivo.
2. **Configura il database** nel file di configurazione (`ecommerce_analytics`).
3. **Installa le dipendenze Python:**
   ```bash
   pip install pandas psycopg2-sqlalchemy ollama

   Avvia Ollama sul tuo PC con il modello Llama 3 attivo:

Bash
ollama run llama3
Esegui la pipeline ETL:

Python
python etl_pipeline.py
Esegui l'agente AI:

Python
python ai_agent.py
