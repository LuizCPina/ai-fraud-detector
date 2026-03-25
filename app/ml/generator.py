from app.schemas.transaction import Transaction,DispositivoEnum, HistoricoEnum
import random
from datetime import time

def generate_transaction():
    return Transaction( 
            valor=random.uniform(1, 10000),
            localizacao=random.choice(['BR', 'US','IN', 'CN', 'RU']),
            horario=time(
                hour=random.randint(0, 23),
                minute=random.randint(0, 59)
            ),
            dispositivo=random.choice([DispositivoEnum.conhecido, DispositivoEnum.desconhecido]),
            historico_usuario=random.choice([HistoricoEnum.padrao, HistoricoEnum.alto, HistoricoEnum.baixo])
        )


def calculate_fraud_probability(transaction):
    chance = 0.0

    if transaction.valor > 3000:
        chance += 0.4

    if transaction.localizacao in ['IN', 'CN', 'RU']:
        chance += 0.2
    
    if transaction.horario.hour < 6:
        chance += 0.1

    if transaction.dispositivo == DispositivoEnum.desconhecido:
        chance += 0.2

    if transaction.historico_usuario == HistoricoEnum.baixo:
        chance += 0.3

    return min(chance, 1.0)

def generate_dataset_record():
    transaction = generate_transaction()
    chance = calculate_fraud_probability(transaction)
    fraude  = random.random() < chance

    return {
        "transaction": transaction,
        "chance": chance,
        "fraude": fraude,
    }