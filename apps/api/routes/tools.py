from fastapi import APIRouter, Query
from typing import Optional
from core_store import list_tools, credits_for

router = APIRouter()

@router.get("")
def tools(category: Optional[str] = Query(None), region: Optional[str] = Query(None), has_credit: Optional[bool] = Query(None)):
    items = list_tools(category=category, region=region)
    if has_credit is not None:
        items = [t for t in items if (len(credits_for(t["id"])) > 0) == has_credit]
    return {"items": items, "count": len(items)}
