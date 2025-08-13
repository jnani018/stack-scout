from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from ..services.planner import plan_from_prompt

router = APIRouter()

class Constraints(BaseModel):
    budget: Optional[float] = Field(default=25.0)
    region: Optional[str] = None
    no_card: Optional[bool] = True
    gpu: Optional[bool] = None
    pii: Optional[bool] = None

class PlanRequest(BaseModel):
    prompt: str = Field(..., example="Build a RAG app under $0 for 30 days, no card")
    constraints: Constraints = Constraints()

class PlanItem(BaseModel):
    role: str
    tool: str
    cost: float
    citations: List[str]

class PlanResponse(BaseModel):
    plan_id: str
    items: List[PlanItem]
    totals: Dict[str, float]
    tradeoffs: List[str]

@router.post("", response_model=PlanResponse)
def create_plan(req: PlanRequest):
    out = plan_from_prompt(req.prompt, req.constraints.model_dump())
    items = [PlanItem(**i) for i in out["items"]]
    return {
        "plan_id": "plan-" + req.prompt[:12].replace(" ", "-"),
        "items": items,
        "totals": {"monthly": out["total"]},
        "tradeoffs": out["tradeoffs"],
    }