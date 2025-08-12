from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import tools, plan, credits, health, evidence, scaffold

app = FastAPI(title="StackScout API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["health"])
app.include_router(tools.router, prefix="/v1/tools", tags=["tools"])
app.include_router(credits.router, prefix="/v1/credits", tags=["credits"])
app.include_router(plan.router, prefix="/v1/plan", tags=["plan"])
app.include_router(scaffold.router, prefix="/v1/repo", tags=["repo"])
app.include_router(evidence.router, prefix="/v1/evidence", tags=["evidence"])
