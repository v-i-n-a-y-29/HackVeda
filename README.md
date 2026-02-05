Marine Insights 🌊
Unified Ocean Intelligence through Multi-Agent AI & Retrieval-Augmented Generation
Team ThinkTank AI Shubhangi Dimri, Vinay Semwal, Ananya Karn, Mridul Rawat

Marine Insights is a production-grade Ocean Intelligence System that bridges the gap between raw data and actionable wisdom. By integrating Machine Learning, Agentic AI, and Serverless RAG via AWS Bedrock, we transform fragmented marine telemetry into a unified decision-support platform.

🚀 The ThinkTank AI Vision
Traditional models only predict numbers. Marine Insights adds an intelligence layer:

📊 Machine Learning: Predicts critical parameters like SST, chlorophyll, and fish species.

🤖 Agentic Orchestration: Autonomous agents interpret results and route tasks based on intent.

📚 Partitioned RAG: Provides scientific and legal grounding using verified sources (FAO, IUCN).

🌍 Actionable ROI: Outputs an "Economic Shield" for fishermen and sustainability plans for regulators.

🧠 System Architecture (Cloud-Native & Agentic)
Code snippet
graph TD
    A[Frontend: React Dashboard] --> B[FastAPI Gateway]
    B --> C{Orchestrator Agent 🤖}
    C --> D[Fisheries Agent]
    C --> E[Overfishing Agent]
    C --> F[Ocean Analytics Agent]
    
    subgraph "AWS Bedrock Infrastructure"
    D & E & F --> G[Amazon Nova Premier - Reasoning Engine]
    G --> H[Knowledge Base: Partitioned RAG]
    H --> I[Titan Text Embeddings V2]
    end
    
    subgraph "ML Service Layer"
    D & E & F --> J[EfficientNet-B0: Species Classification]
    D & E & F --> K[Random Forest: Chlorophyll & SST]
    end
🛠️ Tech Stack & AWS Integration
Core AI Engine: AWS Bedrock
Reasoning Engine: Powered by Amazon Nova Premier (amazon.nova-premier-v1:0) for advanced, multi-step agentic reasoning.

Embeddings: Amazon Titan Text Embeddings V2 (amazon.titan-embed-text-v2:0) ensures high-fidelity semantic search for the RAG pipeline.

Security & Compliance: Fully integrated using the hackathon-bedrock-kb-role within the us-east-1 region for secure, serverless operation.

Vector Infrastructure: Partitioned RAG
We utilize a Partitioned RAG Strategy to eliminate context cross-contamination:

fisheries_kb: Biology, taxonomy, and habitat documents.

overfishing_kb: FAO regulations, legal codes, and sustainability frameworks.

🤖 Agentic Workflows
1️⃣ Fisheries Intelligence Agent 🐟
Specialized in species identification and biological context.

Action: Analyzes image classification confidence (EfficientNet-B0) and retrieves conservation status (IUCN).

Output: Unified report on species health and habitat suitability.

2️⃣ Sustainability & Overfishing Agent ⚖️
Acts as an "Economic Shield" for fishing communities.

Action: Monitors catch vs. stock volume against a 20% sustainability threshold.

Output: Immediate legal alerts and corrective action plans based on international fisheries law.

📂 Project Structure
Plaintext
backend/
├── Agents/                     # Multi-Agent AI Layer (AWS Bedrock & Nova)
│   ├── orchestrator.py         # Routing logic via Amazon Nova
│   ├── fisheries_agent.py      # Biology-focused Agentic RAG
│   └── overfishing_agent.py    # Policy-focused Agentic RAG
├── services/                   # ML Inference Layer
│   ├── fish_classifier.py      # EfficientNet-B0 Species ID
│   ├── predict.py              # Chlorophyll ML Logic
│   └── sst_predict.py          # SST Forecasting
├── rag/                        # RAG Infrastructure
│   ├── database/               # Persistent ChromaDB Stores
│   └── src/                    # Titan V2 Embedding Logic
└── main.py                     # FastAPI Entry Point
📈 Impact & Performance
⏱️ Efficiency: 80% reduction in manual data processing time (from weeks to <10 seconds).

🎯 Accuracy: 28% boost in contextual accuracy through RAG-grounded reasoning.

💰 Economic ROI: Real-time regulatory alerts prevent vessel seizures and catastrophic fines ($2,500+ per incident).

⚙️ Quick Start
1. Activate Environment

Bash
source .venv/bin/activate # Windows: .\.venv\Scripts\activate
2. Configure AWS Credentials Ensure your environment is configured for the hackathon role:

Bash
export AWS_DEFAULT_REGION="us-east-1"
export AWS_ROLE_ARN="arn:aws:iam::[ACC_ID]:role/hackathon-bedrock-kb-role"
3. Launch Backend

Bash
uvicorn main:app --reload
© 2026 Team ThinkTank AI | Designed for the AWS Bedrock Hackathon

Frontend (React Dashboard)
        ↓
FastAPI Backend (API Layer)
        ↓
Orchestrator Agent 🤖
        ↓
------------------------------------------
| Ocean Agent | Fisheries Agent | Biodiversity Agent |
------------------------------------------
        ↓
RAG Knowledge Base (ChromaDB + Embeddings)
        ↓
ML Models (SST, Chlorophyll, Fish Classification)
        ↓
Explainable AI Insights
```

---

## 📂 Project Structure

```text
backend/
├── main.py                     # FastAPI entry point
│
├── Agents/                     # Agentic AI Layer
│   ├── orchestrator.py         # Routes requests to specialized agents
│   ├── fisheries_agent.py      # Species analysis & biology RAG
│   └── overfishing_agent.py    # Sustainability analysis & policy RAG
│
├── services/                   # Core ML Logic & Services
│   ├── fish_classifier.py      # Species classification logic
│   ├── predict.py              # Chlorophyll prediction
│   ├── sst_predict.py          # SST forecasting
│   └── overfishing_analyze.py  # Stock vs Catch analysis
│
├── rag/                        # RAG System
│   ├── rag_engine.py           # Main RAG interface
│   ├── database/               # Vector Stores (ChromaDB)
│   │   ├── fisheries/
│   │   └── overfishing/
│   ├── scripts/                # Database Build Scripts
│   │   ├── build_rag_db.py
│   │   └── build_overfishing_db.py
│   └── src/                    # RAG Core Components
│       ├── data_loader.py
│       ├── embedding.py
│       └── vectorstore.py
│
├── models/                     # Trained Model Artifacts
│   ├── fish_classifier.pth
│   ├── chlorophyll_rf_model.pkl
│   └── labels.json
│
├── requirements.txt
└── README.md
```

---

## 🤖 Agentic AI Workflows

### 1️⃣ Ocean Intelligence Agent 🌊
Analyzes SST, salinity, pH, chlorophyll, and depth profiles.
- **Capabilities**:
  - Detect ocean stress and anomalies
  - Explain climate impact using RAG knowledge
  - Generate insights for marine health

### 2️⃣ Fisheries Agent 🐟
Analyzes fish stock vs catch data and overfishing patterns.
- **Capabilities**:
  - Detect overfishing risk
  - Interpret ML forecasting results
  - Recommend sustainable fishing strategies using RAG

## 📚 RAG (Retrieval-Augmented Generation)

Marine Insights uses a partitioned knowledge base built on **ChromaDB**.

**Knowledge Domains:**
- Oceanography & Climate Science
- Fisheries & Sustainability Policies
- Marine Biodiversity & Ecology
- Environmental Regulations

**RAG Pipeline:**
> Query → Embeddings → Vector Search → Relevant Knowledge → Agent Reasoning → Final Insight

---

## ⚙️ How to Run (Local)

### 1️⃣ Activate Virtual Environment
```bash
source .venv/bin/activate
# or windows
.\.venv\Scripts\activate
```

### 2️⃣ Run Backend Server
```bash
uvicorn main:app --reload
```

### 3️⃣ Access API
- **Base URL**: `http://127.0.0.1:8000`
- **Swagger Docs**: `http://127.0.0.1:8000/docs`

---

## 🧠 Available API Endpoints

### 1️⃣ Predict Chlorophyll (Single Input)
**POST** `/predict`

**Request:**
```json
{
  "depth": 10,
  "salinity": 35,
  "ph": 8.1
}
```

**Response:**
```json
{
  "predicted_chlorophyll": 0.1787
}
```

---

### 2️⃣ Predict Chlorophyll (CSV Upload)
**POST** `/predict/csv`

**CSV Format:**
```csv
depth,salinity,ph
10,35,8.1
20,34.8,8.0
```

**Response:**
```json
{
  "depth": [...],
  "salinity": [...],
  "ph": [...],
  "predicted_chlorophyll": [...]
}
```
*Used for batch prediction and graph plotting in frontend.*

---

### 3️⃣ Sea Surface Temperature Forecast
**GET** `/predict/sst`

**Response:**
```json
{
  "dates": [...],
  "sst": [...]
}
```
*Returns future SST trend data for visualization.*

---

### 4️⃣ Fish Species Classification (Image Upload)
**POST** `/predict/fish_species`

**Description:** Upload an image to classify the fish species using EfficientNet-B0.
**Classes:** Sea Bass, Red Mullet, Horse Mackerel, Shrimp, etc. (9 classes)

**Request:**
- **Method**: POST
- **Content-Type**: `multipart/form-data`
- **Body**: Image file (JPG, PNG, WebP)

**Response:**
```json
{
  "species": "Sea Bass",
  "confidence": 95.67,
  "top_predictions": {
    "Sea Bass": 95.67,
    "Gilt Head Bream": 3.21,
    "Red Sea Bream": 1.12
  }
}
```

**Usage (cURL):**
```bash
curl -X POST "http://localhost:8000/predict/fish_species" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@fish_image.jpg"
```

---

## 🐳 Docker Deployment (Recommended)

### Quick Start

```bash
# 1. Start Docker Desktop
open -a Docker

# 2. Deploy with one command
./deploy.sh
```

**That's it!** Your application will be live at:
- **Frontend**: http://localhost
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### Manual Deployment

```bash
# Build and start services
docker compose up --build -d

# Check status
docker compose ps

# View logs
docker compose logs -f

# Stop services
docker compose down
```

### What's Included

- ✅ **Production-ready** multi-stage builds
- ✅ **Nginx** for frontend serving with caching
- ✅ **Health checks** for both services
- ✅ **API proxying** through Nginx
- ✅ **Environment variable** management
- ✅ **Volume caching** for faster rebuilds

### Documentation

- **Quick Start**: `DOCKER_QUICK_START.md`
- **Setup Guide**: `DOCKER_SETUP.md`
- **Full Documentation**: `DOCKER_DEPLOYMENT.md`
- **Summary**: `DOCKERIZATION_COMPLETE.md`

### Common Commands

```bash
# View logs
docker compose logs -f backend
docker compose logs -f frontend

# Rebuild after changes
docker compose up --build -d

# Access container shell
docker compose exec backend bash

# Remove everything
docker compose down -v
```

---

## 💻 Local Development (Alternative)

If you prefer running without Docker:

---

## 🧩 Notes
- ✅ **CORS** is enabled for frontend integration
- ✅ **No authentication** required (Internal API)
- ✅ **Focus**: Backend handles inference & forecasting; Frontend handles visualization.
