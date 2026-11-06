from fastapi import FastAPI, status
from pydantic import BaseModel

app =FastAPI(
    title="FinRisk_AI_Backend",
    description="Изолированный контур оценки кредитных рисков банка",
    version="1.0.0"
)
#Модель входящих данных для транзакции:
class Transaction(BaseModel):
    user_id:int
    amount:float
    currency_gap_days:int
@app.get("/readyz", status_code=status.HTTP_200_OK)
async def readiness_check():
    """Эндпоинт для проверки готовности сервиса докер_компоузом"""
    return {"status":"ready", "database_connection":"online"}
@app.post("/api/v1/predict")
async def predict_risk(tx:Transaction):
    """Будущая точка для входа модели LightGBM"""
    return {
        "user_id":tx.user_id,
        "fraud_probability":0.042,
        "decision":"APPROVED"
    }
    
