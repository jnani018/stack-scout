# StackScout.AI

Type a goal.
Get a verified low‑budget stack with free credits, quotas, and setup steps.
Full web + API + workers + tests.
Demo data included.

## Features
- Prompt → Plan with citations
- Cost optimization under constraints
- Tool directory with filters
- Credits eligibility checker
- Repo scaffold dry‑run
- Admin evidence freshness view
- CI pipeline and tests

## Quickstart
```bash
docker compose up -d db
# API
cd apps/api && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && uvicorn main:app --reload
# Web
cd ../../apps/web && npm i -g pnpm && pnpm install && pnpm dev
```

## Screens
- Home (prompt, popular goals)
- Plan detail with cost table and citations
- Tools catalog with filters
- Credits catalog with eligibility
- Admin review with freshness flags

## Tests
Run `pytest` in `apps/api`.

## Status
MVP complete with demo data and deterministic planner.
