from . import rules
from .rules_config import RULES

REGRA_MAP = {
    "valor_alto": rules.regra_valor,
    "localizacao_suspeita": rules.regra_localizacao,
    "horario_incomum": rules.regra_horario,
    "dispositivo_novo": rules.regra_dispositivo,
    "historico_suspeito": rules.regra_historico
}

def analyze_transaction(transaction):
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

    return {
        "fraude": risco_total > 0.5,
        "risco": round(risco_total, 2),
        "motivos": motivos
    }