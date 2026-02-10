from .openclaw_base import OpenClawBaseAdapter


class OpenClawJuniorAdapter(OpenClawBaseAdapter):
    adapter_id = "openclaw-junior"

    ROLE_PROMPT = """
You are JUNIOR AGENT.

Rules:
- Short answers
- Friendly tone
- No deep analysis
- 1–2 lines maximum
"""