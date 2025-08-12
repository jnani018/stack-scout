from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from core_store import credits_for, TOOLS

router = APIRouter()

class CheckReq(BaseModel):
    tool_id: str
    user_claims: Dict[str, Any] = {}

@router.post("/check")
def check(req: CheckReq):
    if req.tool_id not in TOOLS:
        raise HTTPException(404, "tool not found")
    options = credits_for(req.tool_id)
    verdicts = []
    for c in options:
        elig = c.get("eligibility", {})
        ok = True
        for k, v in elig.items():
            if k in req.user_claims and req.user_claims[k] != v:
                ok = False
        verdicts.append({"amount": c["amount"], "currency": c["currency"], "ok": ok, "link": c["link"], "steps": c["steps"]})
    return {"tool": TOOLS[req.tool_id]["name"], "verdicts": verdicts}
