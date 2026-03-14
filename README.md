- uv sync

# Grok Prompt:
Provide me a Prompt for Claude for a project with the following details. Prompt should be detailed enough to guide each and every thing to the claude about my requirements. I will be attaching the attached image of my required workflow in the claude along with prompt. Prompt should include the tech stack, structure, flow details, and anything else which is necessary. Here are the project details:

# Advanced Production Grade Agentic AI RAG System
A FAANG-level, production-grade Agentic RAG system that integrates advanced retrieval strategies, autonomous AI agents, and scalable system design to solve complex knowledge-intensive queries. Built with industry-grade architecture including indexing pipelines, hybrid retrieval, reasoning agents, evaluation, monitoring, and real-time deployment.
- My initial and proposed tech stack: use uv as a python manager, fastapi for rest api's, Openai agents sdk or langchain or langgraph or a combination of the three, Multiple llm options Openai LLM, gemini, openrouter and also have a option to connect to locally ollama model, Use the best tools (free tools would be a good choice but they should be best enough). 
- EVAL: A method to score the performamce of rag by time, like it accuracy and other metrics score should be updated with the answer to user. Those metrics should be save somewhere and when i needed i will make a graph using that data to see the historical performance of the model. Similarly the cost and latency per query. I will make a dashboard of these metrics. Add any other necessary metrics also.
Flow of the project (as describe in the image):
- Data Sources: Documents, pdfs, images, code, spreadsheets
- Data Preprocessing: Data  Restructuring (document parser, structure analyzer), Structure aware chunking (table preserver, heading detector, boundary detector), Meta Data Creation (Summary generator, keyword extractor, question generator)
- Database Layer: Vector DB, relational db

- User Query
- Reasoning engine: Planner agent (Decide whether to goto rag or search the web), Tool execution.
- Mutli agent rag (mutiple agents)
- Evaluation: LLM Judges, Precision recall, latency and cost



Note: You can also add any necessary details you want. You can ask any question to me if needed.



# Claude Prompt:
You are an expert FAANG-level AI systems architect and full-stack engineer specializing in production-grade Agentic RAG systems. Your code must be clean, modular, production-ready, fully typed (Pydantic v2 + type hints), extensively commented, and follow best practices for scalability, security, observability, and maintainability.

I am attaching a screenshot of the exact workflow diagram I want the system to follow 100%. You MUST implement the architecture, components, data flow, and every labeled box exactly as shown in the image. Do not deviate from the diagram. Reference it constantly while building.

### PROJECT GOAL
Build a complete, production-grade Advanced Agentic AI RAG system called "AetherRAG" that can handle complex knowledge-intensive queries using:
- Advanced multi-stage data ingestion & preprocessing
- Structure-aware chunking + rich metadata
- Hybrid vector + relational storage
- Intelligent Reasoning Engine with planner + conditional routing
- Multi-Agent RAG collaboration
- Full evaluation, monitoring, cost/latency tracking, LLM-as-Judge auditing, and simulation
- Stress testing and human validation loops
- Simulation layer for cost/latency prediction
- Real-time FastAPI REST API + future dashboard-ready metrics

The system must support both synchronous and asynchronous operation and be ready for Docker/Kubernetes deployment.

### MANDATORY TECH STACK (do not change unless I approve)
- Python package manager: **uv** (use uv init, uv add, uv sync)
- Web framework: **FastAPI** (all endpoints, background tasks, WebSocket if needed)
- Agent orchestration: **LangGraph** (primary) + **LangChain** (for loaders, chains, tools, callbacks). You may use OpenAI Agents SDK (Swarm) only where it adds clear value; prefer LangGraph for stateful multi-agent graphs and conditional routing.
- LLM abstraction: Use **LiteLLM** (best free + paid router) so we can seamlessly switch between:
  - OpenAI (gpt-4o, o1, etc.)
  - Google Gemini (via LiteLLM)
  - OpenRouter (any model)
  - Local Ollama (llama3.1, gemma2, etc.) — full support with streaming and tool calling
  Create a config file (YAML + Pydantic settings) so any model can be selected per-agent or globally via environment variable or API header.
- Vector DB: **Qdrant** (self-hosted or cloud, best free + production features) with hybrid search + reranking
- Relational DB: **PostgreSQL** with **pgvector** extension (for metadata, user feedback, metrics, query logs). Use SQLAlchemy 2.0 + Alembic for migrations. Fallback to SQLite for local dev only.
- Other best free tools (you choose the absolute best open-source options):
  - Document parsing: Unstructured (local mode) + PyMuPDF4 + pdfplumber + python-docx + pandas + openpyxl + any recommended tool.
  - Images: Tesseract OCR + LLaVA or GPT-4o vision when needed
  - Code parsing: tree-sitter + LangChain code splitters
  - Chunking & metadata: Custom structure-aware logic + LLM calls (see diagram)
  - Evaluation: **Ragas** + custom LLM-as-Judge prompts + DeepEval where beneficial
  - Web search tool: Tavily (if paid ok) or free DuckDuckGo + Serper (via LangChain tools)
  - Observability: Structlog + Prometheus metrics exporter (for future dashboard) + LangSmith optional
  - Testing: pytest + locust for stress testing

### PROJECT STRUCTURE (create exactly this)
Create the full folder structure first and show it to me before writing any code:
aetherrag/
├── pyproject.toml
├── uv.lock
├── .env.example
├── config/
├── src/
│   ├── core/               # config, llm_router, utils
│   ├── ingestion/          # all data pipeline
│   │   ├── parsers/
│   │   ├── chunkers/       # structure aware + table/heading/boundary
│   │   └── metadata/       # summary, keyword, question generators
│   ├── db/                 # Qdrant + Postgres CRUD
│   ├── agents/             # LangGraph graphs
│   │   ├── reasoning_engine/   # Planner + Conditional Router
│   │   ├── multi_agent_rag/    # Agent 1,2,3 collaboration
│   │   └── tools/              # web search, calculator, etc.
│   ├── evaluation/         # Ragas + LLM Judge + metrics
│   ├── monitoring/         # cost, latency, token tracking, Prometheus
│   ├── simulation/         # latency & cost simulator
│   ├── stress_testing/     # load tests
│   └── api/                # FastAPI routers
├── tests/
├── docker/
└── docs/


### DETAILED IMPLEMENTATION REQUIREMENTS (follow diagram exactly)

1. **Data Processing Layer** (green box in diagram)
   - Support all data sources shown: Documents, PDFs, Images, Code, Spreadsheets, etc.
   - Data Restructuring → Document Parser + Structure Analyzer
   - Structure-Aware Chunking → Table Preserver, Heading Detector, Boundary Detector (must keep tables intact, respect headings, detect section boundaries)
   - Metadata Creation → Summary Generator, Keyword Extractor, Question Generator (use LLM for all three, store as JSON in metadata)
   - Create a background FastAPI endpoint + CLI command for batch ingestion.

2. **Database Layer**
   - Qdrant collections with rich metadata + hybrid search (dense + sparse + reranker)
   - PostgreSQL tables for: documents, chunks, metadata, query_logs, metrics, user_feedback, human_validation

3. **Reasoning Engine** (purple box)
   - Planner Agent (LangGraph node) that decides:
     - "RAG_ONLY"
     - "WEB_SEARCH_ONLY"
     - "HYBRID"
     - "MULTI_AGENT_RAG"
   - Conditional Router (exactly as in diagram)
   - Tool Execution node
   - Human-in-the-loop option when confidence low

4. **Multi-Agent RAG System** (teal box)
   - Three specialized agents (Agent 1, Agent 2, Agent 3) that collaborate exactly as shown
   - Supervisor or hierarchical graph in LangGraph
   - Each agent has specific role (retriever, critic, synthesizer, etc.)

5. **Evaluation & Monitoring** (top right boxes)
   - Every single query response MUST return:
     - Answer
     - Latency (ms)
     - Cost (USD, calculated via LiteLLM)
     - Accuracy / Faithfulness / Relevance / Context Precision scores (Ragas + LLM Judge)
     - Token usage
     - Retrieval metrics (precision@10, recall, etc.)
   - Save ALL metrics to PostgreSQL "metrics" table with timestamp, query_id, model_used, etc.
   - LLM Judges + Auditor agent (exactly as in diagram)
   - Precision & Recall calculation
   - Human Validation workflow (API endpoint to accept/reject answers and store feedback)

6. **Simulation & Stress Testing**
   - Simulation box: predict latency & cost before real run (use historical data + regression model or simple rules)
   - Stress Testing module with locust scripts (Based Option, Information Creation, Prompt Injection tests)

7. **FastAPI API Endpoints** (must include all)
   - POST /ingest (file upload or folder)
   - POST /query (main endpoint — returns answer + full metrics JSON)
   - GET /metrics (time-range query for dashboard)
   - POST /evaluate (batch evaluation)
   - POST /stress-test
   - WebSocket for streaming answers
   - Admin endpoints for human validation, simulation, etc.

### EVALUATION & DASHBOARD REQUIREMENTS
- Every response to the user must include a "metrics" object.
- All metrics saved permanently in Postgres.
- Additional metrics you must track (add any you think are necessary):
  - Faithfulness, Answer Relevancy, Context Precision, Context Recall (Ragas)
  - Hallucination score
  - Agent collaboration quality
  - Tool usage count
  - Human validation score over time
- I will later build Grafana/PowerBI dashboard on top of the metrics table — make the schema perfect for time-series analysis.

### DELIVERY INSTRUCTIONS (step-by-step)
Follow this exact order and wait for my confirmation after each step:
1. Output the full project directory structure with file names.
2. Generate pyproject.toml + all dependencies (with exact versions where possible) + uv sync command.
3. Generate .env.example and config YAML.
4. Implement the entire ingestion pipeline (parsers → chunkers → metadata → DB storage).
5. Set up DB connections and migrations.
6. Build the Reasoning Engine + Conditional Router in LangGraph.
7. Build the Multi-Agent RAG graph.
8. Implement evaluation, monitoring, cost/latency tracking, and metrics storage.
9. Build all FastAPI routers and main app.
10. Add simulation and stress-testing modules.
11. Provide Docker Compose (FastAPI + Qdrant + Postgres + Ollama).
12. Final README with run instructions, how to switch LLMs, how to ingest data, and how to view metrics.
13. Any files for claude code or vibe coding (like SKILL.md etc...)

Use async everywhere possible. Add comprehensive logging, error handling, retries (Tenacity), and rate-limit handling.

Start by confirming you have understood the diagram (describe the full flow in your own words to prove it) and then output Step 1 (project structure).

If anything in the diagram or requirements is unclear, ask me ONE question at a time before proceeding. Otherwise, begin building exactly as specified.



# Claude:
aetherrag/
├── pyproject.toml
├── uv.lock                          # auto-generated by uv
├── .env.example
├── .gitignore
├── Makefile                         # shortcuts for dev commands
│
├── config/
│   ├── settings.yaml                # global LLM, DB, feature flags
│   ├── agents.yaml                  # per-agent model config
│   ├── evaluation.yaml              # ragas thresholds, judge prompts
│   └── logging.yaml                 # structlog config
│
├── src/
│   ├── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py                # Pydantic Settings v2, loads YAML + .env
│   │   ├── llm_router.py            # LiteLLM wrapper, per-agent model selection
│   │   ├── exceptions.py            # custom exception hierarchy
│   │   └── utils.py                 # retry decorators, timing, token counting
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── pipeline.py              # orchestrates full ingestion flow (async)
│   │   │
│   │   ├── parsers/
│   │   │   ├── __init__.py
│   │   │   ├── base.py              # BaseParser ABC
│   │   │   ├── pdf_parser.py        # PyMuPDF + pdfplumber
│   │   │   ├── docx_parser.py       # python-docx
│   │   │   ├── image_parser.py      # Tesseract OCR + LLaVA/GPT-4o vision
│   │   │   ├── code_parser.py       # tree-sitter + LangChain code splitter
│   │   │   ├── spreadsheet_parser.py# pandas + openpyxl
│   │   │   └── unstructured_parser.py# Unstructured fallback
│   │   │
│   │   ├── chunkers/
│   │   │   ├── __init__.py
│   │   │   ├── base.py              # BaseChunker ABC
│   │   │   ├── structure_aware.py   # main orchestrator
│   │   │   ├── table_preserver.py   # keeps tables intact
│   │   │   ├── heading_detector.py  # heading-based splits
│   │   │   └── boundary_detector.py # semantic boundary detection
│   │   │
│   │   └── metadata/
│   │       ├── __init__.py
│   │       ├── base.py              # BaseMetadataGenerator ABC
│   │       ├── summary_generator.py # LLM summarization per chunk
│   │       ├── keyword_extractor.py # LLM + KeyBERT keyword extraction
│   │       └── question_generator.py# LLM generates hypothetical questions
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── qdrant_client.py         # Qdrant connection, collections, upsert, search
│   │   ├── postgres_client.py       # SQLAlchemy 2.0 async engine + session factory
│   │   ├── models.py                # SQLAlchemy ORM models (all tables)
│   │   ├── schemas.py               # Pydantic v2 schemas for DB I/O
│   │   ├── crud/
│   │   │   ├── __init__.py
│   │   │   ├── documents.py
│   │   │   ├── chunks.py
│   │   │   ├── query_logs.py
│   │   │   ├── metrics.py
│   │   │   └── human_validation.py
│   │   └── migrations/
│   │       ├── env.py               # Alembic env
│   │       └── versions/            # migration scripts
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   │
│   │   ├── reasoning_engine/
│   │   │   ├── __init__.py
│   │   │   ├── graph.py             # LangGraph StateGraph: Planner→ToolExec→Router
│   │   │   ├── planner.py           # Planner node: decides routing strategy
│   │   │   ├── tool_executor.py     # Tool execution node
│   │   │   ├── conditional_router.py# Router: RAG_ONLY/WEB/HYBRID/MULTI_AGENT
│   │   │   └── state.py             # ReasoningState TypedDict
│   │   │
│   │   ├── multi_agent_rag/
│   │   │   ├── __init__.py
│   │   │   ├── graph.py             # LangGraph multi-agent supervisor graph
│   │   │   ├── supervisor.py        # Supervisor node
│   │   │   ├── agent1_retriever.py  # Retrieval-specialist agent
│   │   │   ├── agent2_critic.py     # Critic/verification agent
│   │   │   ├── agent3_synthesizer.py# Synthesis/answer agent
│   │   │   └── state.py             # MultiAgentState TypedDict
│   │   │
│   │   └── tools/
│   │       ├── __init__.py
│   │       ├── qdrant_search.py     # vector search tool
│   │       ├── web_search.py        # DuckDuckGo + Tavily
│   │       ├── calculator.py        # safe math eval
│   │       └── code_executor.py     # sandboxed code execution
│   │
│   ├── human_validation/
│   │   ├── __init__.py
│   │   ├── gatekeeper.py            # quality gate: auto-accept/flag
│   │   ├── auditor.py               # audit trail, logs decisions
│   │   └── strategist.py            # routing strategy for flagged items
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── ragas_evaluator.py       # Ragas metrics pipeline
│   │   ├── llm_judge.py             # LLM-as-Judge prompts + scoring
│   │   ├── precision_recall.py      # retrieval precision@k, recall
│   │   └── aggregator.py            # combines all scores → EvalResult
│   │
│   ├── monitoring/
│   │   ├── __init__.py
│   │   ├── cost_tracker.py          # LiteLLM cost extraction
│   │   ├── latency_tracker.py       # async timing context manager
│   │   ├── token_tracker.py         # token usage per call
│   │   └── prometheus_exporter.py   # Prometheus metrics definitions
│   │
│   ├── simulation/
│   │   ├── __init__.py
│   │   ├── latency_simulator.py     # predict latency from historical data
│   │   └── cost_simulator.py        # predict cost before real run
│   │
│   ├── stress_testing/
│   │   ├── __init__.py
│   │   ├── locustfile.py            # Locust load test scenarios
│   │   ├── biased_opinion.py        # biased query generator
│   │   ├── information_erasure.py   # adversarial erasure tests
│   │   └── prompt_injection.py      # prompt injection test cases
│   │
│   └── api/
│       ├── __init__.py
│       ├── main.py                  # FastAPI app factory, lifespan, middleware
│       ├── dependencies.py          # shared FastAPI dependencies (DB sessions, etc.)
│       ├── routers/
│       │   ├── __init__.py
│       │   ├── ingest.py            # POST /ingest
│       │   ├── query.py             # POST /query, WS /query/stream
│       │   ├── metrics.py           # GET /metrics
│       │   ├── evaluate.py          # POST /evaluate
│       │   ├── stress_test.py       # POST /stress-test
│       │   ├── simulation.py        # POST /simulate
│       │   ├── human_validation.py  # POST /validate, GET /validate/queue
│       │   └── admin.py             # admin utilities
│       └── middleware/
│           ├── __init__.py
│           ├── logging_middleware.py
│           └── rate_limit.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # pytest fixtures (test DB, mock LLM)
│   ├── unit/
│   │   ├── test_parsers.py
│   │   ├── test_chunkers.py
│   │   ├── test_metadata.py
│   │   ├── test_reasoning_engine.py
│   │   └── test_evaluation.py
│   ├── integration/
│   │   ├── test_ingestion_pipeline.py
│   │   ├── test_query_pipeline.py
│   │   └── test_api_endpoints.py
│   └── stress/
│       └── locust_scenarios.py
│
├── docker/
│   ├── Dockerfile                   # multi-stage: builder + runtime
│   ├── docker-compose.yml           # FastAPI + Qdrant + Postgres + Ollama
│   ├── docker-compose.dev.yml       # dev overrides (hot reload)
│   └── nginx/
│       └── nginx.conf               # reverse proxy config
│
└── docs/
    ├── architecture.md              # diagram description + design decisions
    ├── api_reference.md             # all endpoints documented
    ├── deployment.md                # Docker/K8s instructions
    └── CLAUDE.md                    # for Claude Code / vibe coding context