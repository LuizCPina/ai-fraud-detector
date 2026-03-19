RULES = {
    "valor_alto": {
        "limite": 3000,
        "peso": 0.3,
        "mensagem": "valor alto"
    },
    
    "localizacao_suspeita": {
        "locais": ["BR", "US"],
        "peso": 0.2,
        "mensagem": "localização suspeita"

    },

    "horario_incomum": {
        "limite": 6,
        "peso": 0.3,
        "mensagem": "horário incomum"
    },

    "dispositivo_novo": {
        "peso": 0.2,
        "mensagem": "dispositivo novo"
    },

    "historico_suspeito": {
        "peso": 0.2,
        "mensagem": "histórico suspeito"
    }

}