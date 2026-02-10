from .openclaw_base import OpenClawBaseAdapter


class OpenClawToolAdapter(OpenClawBaseAdapter):
    adapter_id = "openclaw-tool"

    ROLE_PROMPT = """
You are TOOL AGENT.

Rules:
- Focus on actions and steps
- Prefer bullet points or JSON
- No storytelling
- Output must be machine-usable
"""