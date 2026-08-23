from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class CreditState(TypedDict):
    customer_id: int
    monthly_income: float
    requested_amount: float
    debt_to_income: float
    risk: str
    decision: str

def calculate_debt_to_income(state: CreditState):
        debt_to_income = (
              state["requested_amount"] / state["monthly_income"]
        )
        return {
              "debt_to_income": round(debt_to_income, 2)
        }

builder = StateGraph(CreditState)

builder.add_node(
      "calculate_debt_to_income",
      calculate_debt_to_income
)

builder.add_edge(
      START,
      "calculate_debt_to_income"
)

builder.add_edge(
      "calculate_debt_to_income"
    END
)

graph = builder.compile()
