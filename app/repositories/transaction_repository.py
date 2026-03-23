import json
import os

def save_transaction(record):

    try:
        os.makedirs("data", exist_ok=True)
        with open('data/transactions.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []

    dados.append(record)

    with open('data/transactions.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)