# backend/aws/config.py
import os
from dotenv import load_dotenv
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
# =========================
# AWS CORE CONFIG
# =========================
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# =========================
# BEDROCK MODELS
# =========================
BEDROCK_TEXT_MODEL = "amazon.nova-premier-v1:0"
BEDROCK_EMBED_MODEL = "amazon.titan-embed-text-v2:0"

# =========================
# BEDROCK AGENTS
# =========================
FISHERIES_AGENT_ID = os.getenv("FISHERIES_AGENT_ID")
FISHERIES_AGENT_ALIAS_ID = os.getenv("FISHERIES_AGENT_ALIAS_ID")

OVERFISHING_AGENT_ID = os.getenv("OVERFISHING_AGENT_ID", "placeholder")
OVERFISHING_AGENT_ALIAS_ID = os.getenv("OVERFISHING_AGENT_ALIAS_ID", "placeholder")

# =========================
# SAFETY CHECK (for judges)
# =========================
def validate_config():
    missing = []
    if not FISHERIES_AGENT_ID:
        missing.append("FISHERIES_AGENT_ID")
    if not FISHERIES_AGENT_ALIAS_ID:
        missing.append("FISHERIES_AGENT_ALIAS_ID")

    if missing:
        print(f"[WARN] Missing env vars: {missing}")