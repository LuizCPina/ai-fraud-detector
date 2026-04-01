from . import rules
from .rules_config import RULES
from app.repositories.transaction_repository import save_transaction

REGRA_MAP = {
    "valor_alto": rules.regra_valor,
    "localizacao_suspeita": rules.regra_localizacao,
    "horario_incomum": rules.regra_horario,
    "dispositivo_novo": rules.regra_dispositivo,
    "historico_suspeito": rules.regra_historico
}

def analyze_transaction(transaction, threshold):
    risco_total = 0
    motivos = []

    for nome_regra, config in RULES.items():

        regra_func = REGRA_MAP[nome_regra]
        if not regra_func:
            continue

        risco, motivo = regra_func(transaction, config)

        risco_total += risco
        risco_total = min(risco_total, 1)

        if motivo:
            motivos.append(motivo)

#    ##salvar no registro de transações
#     transaction_data = transaction.model_dump()
#     transaction_data["horario"] = transaction.horario.strftime("%H:%M")       

#     record = {
#         "transaction": transaction_data,
#         "fraude": risco_total > 0.5,
#         "risco": round(risco_total, 2),
#         "motivos": motivos}
    
#     save_transaction(record)

    return {
        "fraude_estimada": risco_total > threshold,
        "risco_estimado": round(risco_total, 2),
        "motivos": motivos
    }