from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Credit Agent",
    description="API de analise de credito",
    version="0.1.0",
)

class CreditRequest(BaseModel):
    name: str
    age: int
    monthly_income: float
    request_amount: float
    employment_months: int

@app.get("/")
def root():
    return{
        "message": "Credit Agent esta online"
    }

@app.post("/credit/analyze")
def analyze_credit(request: CreditRequest):
    return {
        "message": "Solicitaçao recebida",
        "customer": request.name,
        "monthly_income": request.monthly_income,
        "requested_amount": request.request_amount
    }