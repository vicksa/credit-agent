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

def calculate_risk(state: CreditState):
      debt_to_income = state["debt_to_income"]
      if debt_to_income <= 2:
            risk =  "low"
      elif debt_to_income <= 4:
            risk = "medium"
      else:
            risk = "high"
      return {
            "risk" : risk
      }
      
def make_decision(state: CreditState):
      risk = state["risk"]
      if risk == "low":
            decision = "approved"
      elif risk == "medium":
             decision = "review"
      else:
            decision = "denied"
      return {
            "decision": decision
      }

builder = StateGraph(CreditState)

builder.add_node(
      "calculate_debt_to_income",
      calculate_debt_to_income
)
builder.add_node(
      "calculate_risk",
      calculate_risk
)

builder.add_edge(
      START,
      "calculate_debt_to_income",

)


builder.add_edge(
      "calculate_debt_to_income",
      "calculate_risk",
)

builder.add_edge(
      "calculate_risk",
 
   END
)







graph = builder.compile()

