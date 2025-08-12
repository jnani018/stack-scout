from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional
from core_store import list_tools, docs_for

router = APIRouter()

class Constraints(BaseModel):
    budget: Optional[float] = Field(default=25.0)
    region: Optional[str] = None
    no_card: Optional[bool] = True

class PlanReq(BaseModel):
    prompt: str
    constraints: Constraints = Constraints()

@router.post("")
def create(req: PlanReq):
    role_map = {"llm":"genai","vector-db":"vector-db","compute":"compute","database":"database","storage":"storage"}
    pool = list_tools(region=req.constraints.region)
    items = []
    for role, cat in role_map.items():
        cands = [t for t in pool if t["category"] == cat]
        if not cands:
            continue
        t = cands[0]
        citations = [d["src_url"] for d in docs_for(t["id"])]
        items.append({"role":role,"tool":t["name"],"cost":0,"citations":citations[:2]})
    total = sum(i["cost"] for i in items)
    return {"plan_id":"plan-"+req.prompt[:12].replace(" ","-"),"items":items,"totals":{"monthly":total},"tradeoffs":["Free tiers have quotas","Latency may vary on free compute"]}
