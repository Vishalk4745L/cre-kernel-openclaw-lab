from .openclaw_base import OpenClawBaseAdapter


class OpenClawSeniorAdapter(OpenClawBaseAdapter):
    adapter_id = "openclaw-senior"

    ROLE_PROMPT = """
You are SENIOR AGENT.

Rules:
- Be precise and critical
- Structured reasoning
- Call out ambiguities
- No fluff
"""