from app.schemas.transaction import Transaction,DispositivoEnum, HistoricoEnum
import random
from datetime import time

def generate_normal_transaction():
    return {
        "transaction": Transaction(
            valor=random.uniform(1, 3000),
            localizacao=random.choice(['BR', 'US']),
            horario=time(
                hour=random.randint(6, 23),
                minute=random.randint(0, 59)
            ),
            dispositivo=DispositivoEnum.conhecido,
            historico_usuario=random.choice([HistoricoEnum.padrao, HistoricoEnum.alto])
        ),
        "fraude": False
    }

def generate_fraud_transaction():
    return {
        "transaction": Transaction(
            valor=random.uniform(3000, 10000),
            localizacao=random.choice(['IN', 'CN', 'RU']),
            horario=time(
                hour=random.randint(0, 5),
                minute=random.randint(0, 59)
            ),
            dispositivo=DispositivoEnum.desconhecido,
            historico_usuario=HistoricoEnum.baixo
        ),
        "fraude": True
    }

def generate_dataset_transaction():
    if random.random() < 0.2:
        return generate_fraud_transaction()
    return generate_normal_transaction()