def analyze_credit(
    monthly_income: float,
    requested_amount: float,
) -> dict:
    debt_to_income = requested_amount / monthly_income

    if debt_to_income <= 2:
        risk = "low"
        decision = "approved"
    elif debt_to_income <=4:
         risk = "medium"
         decision = "review"
    else:
        risk = "high"
        decision = "denied"

    return {
    "debt_to_income": round(debt_to_income, 2),
    "risk": risk,
    "decision": decision,
}