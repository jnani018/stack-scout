from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()

TOOLS = [
    {"id":"t1","name":"OpenRouter","category":"genai","website":"https://openrouter.ai","has_credit":False},
    {"id":"t2","name":"Qdrant","category":"vector-db","website":"https://qdrant.tech","has_credit":True},
    {"id":"t3","name":"Railway","category":"compute","website":"https://railway.app","has_credit":True},
    {"id":"t4","name":"Neon","category":"database","website":"https://neon.tech","has_credit":True},
    {"id":"t5","name":"Cloudflare R2","category":"storage","website":"https://developers.cloudflare.com/r2","has_credit":False},
]

@router.get("")
def list_tools(category: Optional[str] = Query(None), has_credit: Optional[bool] = Query(None)):
    items = TOOLS
    if category:
        items = [t for t in items if t["category"] == category]
    if has_credit is not None:
        items = [t for t in items if (t["has_credit"] is True) == has_credit]
    return {"items": items, "count": len(items)}