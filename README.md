# data-scientist-assessment-Bot
Telegram RAG Bot 
#  Mini-RAG Telegram Bot

A lightweight Retrieval-Augmented Generation (RAG) bot built with Python. This bot uses a local vector database to answer questions based on a specific set of documents provided in the `data/` folder.

##  Features
* **Local RAG:** Uses `sqlite-vec` for fast, local vector search.
* **Privacy-First:** Powered by **Ollama**, so your data and queries stay on your machine.
* **Smart Retrieval:** Finds the most relevant document snippets before answering.
* **Source Citation:** Tells the user which file it used to generate the answer.

---

##  Prerequisites

Before running the bot, ensure you have the following installed:

1.  **Python 3.9+**
2.  **Ollama:** [Download here](https://ollama.com).
3.  **Local Models:** Run these commands in your terminal:
    ```bash
    ollama pull llama3.2
    ollama pull snowflake-arctic-embed
    ```
4.  **Telegram Bot Token:** Create one via [@BotFather](https://t.me/botfather).

---

## 📂 Installation & Setup

1. **Clone or create the project directory:**
   ```bash
https://github.com/syedpmsa/data-scientist-assessment-Bot.git

pip install -r requirements.txt
Run the ingestion script to create embeddings:

python rag/ingest.py

Run the Bot
python bot.py
