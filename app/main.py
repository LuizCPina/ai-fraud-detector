from fastapi import FastAPI
from app.schemas.transaction import Transaction
from app.services.fraud import engine
from fastapi.responses import FileResponse

app = FastAPI(title="AI Fraud Detector")

@app.get("/")
def home():
    return FileResponse("app/frontend/index.html")

@app.post("/analyze")
def analyze(transaction: Transaction):
    return engine.analyze_transaction(transaction)