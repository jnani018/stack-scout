StackScout.AI

Your AI-powered stack advisor for budget-conscious builders

One prompt → Full, cost-optimized tech stack with free credits, quotas, and setup steps.
StackScout.AI helps students, researchers, and indie developers find the best combination of tools, APIs, and services they can use for free or at minimal cost, backed by a verified and regularly updated database.

⸻

What It Does
	1.	Natural language to actionable plan
	•	Type your goal, e.g., “I want to build a video summarization app”.
	•	Our LLM-powered planner breaks it into required components (hosting, database, AI models, storage, etc.).
	•	Suggests a low-budget stack using free tiers, academic credits, and open-source alternatives.
	2.	Cost optimization under constraints
	•	Uses a cost minimization algorithm to find the optimal mix of free credits and low-tier plans.
	•	Flags tools that exceed your budget or usage limits.
	3.	Credits & eligibility tracking
	•	Database of free tier offers, student discounts, and startup credits.
	•	Verifies eligibility (student email, GitHub Student Pack, accelerator membership).
	4.	Tool discovery & filtering
	•	Search 500+ tools by category, pricing model, credit offers, and geography.
	•	Each tool entry includes tested data (MCP-verified freshness).
	5.	Evidence & transparency
	•	Every recommendation includes citations (official docs, offer pages, verified experiments).
	•	Admin dashboard to check “freshness” of each entry, powered by MCP background workers.

⸻

How It Works

Architecture
	•	Frontend → apps/web (Next.js + Tailwind)
	•	Backend API → apps/api (FastAPI)
	•	Database → PostgreSQL
	•	Background Workers → Celery + Redis (scraping & MCP freshness checks)
	•	CI/CD → GitHub Actions with automated tests & linting

⸻

MCP (Model Context Protocol) Usage

We use MCP to:
	•	Automatically test if listed tools are still active, their free credits are valid, and the signup process is unchanged.
	•	Collect metadata like API limits, latency, and last verification date.
	•	Keep our recommendation engine updated in real-time without manual intervention.

⸻

GenAI Integration
	•	LLM Planner: Uses OpenAI’s GPT-4 (configurable) to turn a plain-text goal into a component-by-component plan.
	•	Citations Engine: Enforces retrieval-augmented generation (RAG) to attach evidence from our database and external sources.
	•	Prompt Refinement: User queries are auto-clarified via follow-up questions to produce a more accurate plan.

⸻

Data Science Components
	•	Optimization Model: Runs cost vs. performance trade-off analysis using Linear Programming (PuLP).
	•	Usage Simulation: Predicts when free credits will expire based on projected usage patterns.
	•	Tool Ranking Algorithm: Weighted score based on reliability, credit value, ease of setup, and performance benchmarks.

⸻

Features

✅ Prompt → Plan with citations
✅ Cost optimization under constraints
✅ Tool directory with advanced filters
✅ Credits eligibility checker
✅ Repo scaffold dry-run generator
✅ Admin evidence freshness view
✅ CI pipeline with automated tests
