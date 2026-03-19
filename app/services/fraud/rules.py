def regra_valor(transaction, config):
    if transaction.valor > config["limite"]:
        return config["peso"], config["mensagem"]
    return 0, None

def regra_localizacao(transaction, config):
    if transaction.localizacao  not in config["locais"]:
        return config["peso"], config["mensagem"]
    return 0, None

def regra_horario(transaction, config):
    hora = transaction.horario.hour
    if hora < config["limite"]:
        return config["peso"], config["mensagem"]
    return 0, None

def regra_dispositivo(transaction, config):
    if transaction.dispositivo == "desconhecido":
        return config["peso"], config["mensagem"]
    return 0, None

def regra_historico(transaction, config):
    if transaction.historico_usuario == "baixo":
        return config["peso"], config["mensagem"]
    return 0, None