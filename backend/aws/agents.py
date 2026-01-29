# backend/aws/agents.py

import uuid
from backend.aws.bedrock_client import get_bedrock_agent_runtime
from backend.aws.config import (
    FISHERIES_AGENT_ID,
    FISHERIES_AGENT_ALIAS_ID,
)

def invoke_fisheries_agent(user_input: str) -> str:
    """
    Invoke Fisheries Bedrock Agent (NO internal KB).
    Retrieval handled externally if needed.
    """

    if not FISHERIES_AGENT_ID or not FISHERIES_AGENT_ALIAS_ID:
        raise RuntimeError("Fisheries Agent env vars not set")

    client = get_bedrock_agent_runtime()
    session_id = str(uuid.uuid4())

    response = client.invoke_agent(
        agentId=FISHERIES_AGENT_ID,
        agentAliasId=FISHERIES_AGENT_ALIAS_ID,
        sessionId=session_id,
        inputText=user_input,
    )

    final_text = []

    for event in response.get("completion", []):
        if "chunk" in event:
            final_text.append(
                event["chunk"]["bytes"].decode("utf-8")
            )

    return "".join(final_text)
# backend/aws/agents.py

import uuid
from backend.aws.bedrock_client import get_bedrock_agent_runtime
from backend.aws.config import (
    FISHERIES_AGENT_ID,
    FISHERIES_AGENT_ALIAS_ID,
    OVERFISHING_AGENT_ID,
    OVERFISHING_AGENT_ALIAS_ID,
)

def _invoke_agent(agent_id: str, alias_id: str, user_input: str) -> str:
    """
    Shared internal helper to invoke any Bedrock Agent.
    """
    client = get_bedrock_agent_runtime()
    session_id = str(uuid.uuid4())

    response = client.invoke_agent(
        agentId=agent_id,
        agentAliasId=alias_id,
        sessionId=session_id,
        inputText=user_input,
    )

    output_chunks = []
    for event in response.get("completion", []):
        if "chunk" in event:
            output_chunks.append(
                event["chunk"]["bytes"].decode("utf-8")
            )

    return "".join(output_chunks)


def invoke_fisheries_agent(user_input: str) -> str:
    """
    Invoke Fisheries Bedrock Agent.
    """
    if not FISHERIES_AGENT_ID or not FISHERIES_AGENT_ALIAS_ID:
        raise RuntimeError("Fisheries Agent env vars not set")

    return _invoke_agent(
        FISHERIES_AGENT_ID,
        FISHERIES_AGENT_ALIAS_ID,
        user_input,
    )


def invoke_overfishing_agent(user_input: str) -> str:
    """
    Invoke Overfishing Bedrock Agent.
    """
    if not OVERFISHING_AGENT_ID or not OVERFISHING_AGENT_ALIAS_ID:
        raise RuntimeError("Overfishing Agent env vars not set")

    return _invoke_agent(
        OVERFISHING_AGENT_ID,
        OVERFISHING_AGENT_ALIAS_ID,
        user_input,
    )