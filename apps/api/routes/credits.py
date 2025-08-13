from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()

class CheckReq(BaseModel):
    tool_id: str
    user_claims: Dict[str, Any] = {}

CREDITS = {
    "t2": {"amount": 0, "currency": "USD", "requires": {"student_email": False}},
    "t3": {"amount": 5, "currency": "USD", "requires": {"student_email": False}},
    "t4": {"amount": 0, "currency": "USD", "requires": {"student_email": False}},
}

@router.post("/check")
def check(req: CheckReq):
    rule = CREDITS.get(req.tool_id)
    if not rule:
        return {"eligible": False, "reason": "No credit program found"}
    needs = rule["requires"]
    ok = all(req.user_claims.get(k, needs[k]) == needs[k] for k in needs)
    return {"eligible": ok, "amount": rule["amount"], "currency": rule["currency"], "requires": needs}