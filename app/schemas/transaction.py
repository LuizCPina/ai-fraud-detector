from pydantic import BaseModel, Field
from enum import Enum
from datetime import time

class DispositivoEnum(str, Enum):
    conhecido =  "conhecido"
    desconhecido =  "desconhecido"

class HistoricoEnum(str, Enum):
    baixo = "baixo"
    padrao = "padrao"
    alto = "alto"

class Transaction(BaseModel):
    valor: float = Field(..., ge=0)
    localizacao: str
    horario: time
    dispositivo: DispositivoEnum
    historico_usuario: HistoricoEnum    

