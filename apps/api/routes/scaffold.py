from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Req(BaseModel):
    plan_id: str
    template: str = "rag-app"
    language: str = "python"
    dry_run: bool = True

@router.post("/scaffold")
def scaffold(req: Req):
    diff = (
        "diff --git a/app.py b/app.py\n"
        "+ from fastapi import FastAPI\n"
        "+ app = FastAPI()\n"
        "+ @app.get('/')\n"
        "+ def hi(): return {'ok':True}\n"
    )
    return {"diff": diff, "repo_url_if_applied": None}
