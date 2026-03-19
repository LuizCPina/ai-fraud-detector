from fastapi import FastAPI
from app.schemas.transaction import Transaction
from app.services.fraud import engine

app = FastAPI(title="AI Fraud Detector")

@app.get("/")
def home():
    return {"message": "API de Detecção de Fraudes rodando 🚀"}

@app.post("/analyze")
def analyze(transaction: Transaction):
    return engine.analyze_transaction(transaction)