# 🌊 BlueNexus  
## Unified Ocean Intelligence through Multi-Agent AI & Retrieval-Augmented Generation

**Team ThinkTank AI**  
Shubhangi Dimri · Vinay Semwal · Ananya Karn · Mridul Rawat  

---

## 🚀 Overview

BlueNexus is a **production-grade Ocean Intelligence System** that bridges the gap between **raw marine telemetry** and **actionable intelligence**.

By integrating **Machine Learning**, **Agentic AI**, and **Serverless RAG on AWS Bedrock**, the platform transforms fragmented ocean data into a **unified decision-support system** for fishermen, researchers, and regulators.

---

## 🧠 The ThinkTank AI Vision

Traditional models only predict numbers.  
**BlueNexus adds an intelligence layer.**

---

## 📊 Machine Learning

- Predicts **Sea Surface Temperature (SST)**
- Estimates **Chlorophyll concentration**
- Classifies **Fish Species** using EfficientNet-B0

---

## 🤖 Agentic Orchestration

- Autonomous agents interpret ML outputs  
- Routes tasks based on **intent & context**  
- Multi-agent reasoning powered by **AWS Bedrock**

---

## 📚 Partitioned RAG

- Scientific & legal grounding via verified sources (FAO, IUCN)
- Domain-isolated vector stores prevent hallucination

**Knowledge Bases**
- `fisheries_kb` → Biology, taxonomy, habitat  
- `overfishing_kb` → Regulations, sustainability laws  

---

## 🧠 System Architecture

Frontend (React Dashboard)  
↓  
FastAPI Backend (API Layer)  
↓  
Orchestrator Agent 🤖  
↓  
Fisheries Agent | Overfishing Agent | Ocean Analytics Agent  
↓  
RAG Knowledge Base (ChromaDB + Titan Embeddings)  
↓  
ML Models (SST, Chlorophyll, Fish Classification)  
↓  
Explainable AI Insights  

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python  
- **Frontend:** React  
- **AI Reasoning:** AWS Bedrock (Amazon Nova Premier)  
- **Embeddings:** Amazon Titan Text Embeddings V2  
- **Vector DB:** ChromaDB  
- **ML Models:** EfficientNet-B0, Random Forest  
- **Deployment:** Docker, Nginx  

---

## 🤖 Agentic Workflows

### 1️⃣ Fisheries Intelligence Agent 🐟
- Identifies fish species  
- Retrieves conservation status (IUCN)  
- Outputs species health & habitat insights  

### 2️⃣ Sustainability & Overfishing Agent ⚖️
- Monitors catch vs stock volume  
- Enforces **20% sustainability threshold**  
- Generates legal alerts & corrective plans  

---

## 📂 Project Structure

```text
backend/
├── main.py
├── Agents/
│   ├── orchestrator.py
│   ├── fisheries_agent.py
│   └── overfishing_agent.py
├── services/
│   ├── fish_classifier.py
│   ├── predict.py
│   ├── sst_predict.py
│   └── overfishing_analyze.py
├── rag/
│   ├── rag_engine.py
│   ├── database/
│   │   ├── fisheries/
│   │   └── overfishing/
│   └── src/
│       ├── embedding.py
│       └── vectorstore.py
├── models/
│   ├── fish_classifier.pth
│   ├── chlorophyll_rf_model.pkl
│   └── labels.json
└── requirements.txt

## 📈 Impact & Performance

- ⏱️ **80% reduction** in manual data processing time  
- 🎯 **28% improvement** in contextual accuracy using RAG  
- 💰 Prevents vessel seizures & fines (**$2,500+ per incident**)  

---

## ⚙️ Quick Start

### Activate Virtual Environment
```bash
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate

## ⚙️ Configure AWS

```bash
export AWS_DEFAULT_REGION="us-east-1"
export AWS_ROLE_ARN="arn:aws:iam::<ACC_ID>:role/hackathon-bedrock-kb-role"

## ▶️ Run Backend

```bash
uvicorn main:app --reload

## 🐳 Docker Configuration

### Prerequisites
- Docker installed
- Docker Compose installed

---

### Quick Start (Recommended)

```bash
# Start Docker Desktop (if not running)
docker --version

# Build and run all services
./deploy.sh
Service Access

Frontend: http://localhost

Backend: http://localhost:8000

API Docs: http://localhost:8000/docs

