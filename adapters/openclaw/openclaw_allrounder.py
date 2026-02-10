from .openclaw_base import OpenClawBaseAdapter


class OpenClawAllRounderAdapter(OpenClawBaseAdapter):
    adapter_id = "openclaw-allrounder"

    ROLE_PROMPT = """
You are ALL-ROUNDER AGENT.

Rules:
- Combine reasoning + execution
- Explain briefly, then act
- Balanced tone
"""