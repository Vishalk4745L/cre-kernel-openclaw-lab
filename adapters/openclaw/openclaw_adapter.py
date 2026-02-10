import os
import subprocess
import json
from typing import Dict, Any
from adapters.adapter_interface import AgentAdapter


class OpenClawAdapter(AgentAdapter):
    """
    OpenClaw Adapter (NON-INTERACTIVE, EMBEDDED MODE)

    Design:
    - Uses npx openclaw
    - Embedded mode (no gateway dependency)
    - Parses JSON safely
    - Returns ONLY clean text to Kernel
    """

    adapter_id = "openclaw"
    adapter_type = "agent"

    def capabilities(self) -> Dict[str, Any]:
        return {
            "reasoning": True,
            "tools": True,
            "confidence": 0.6,
            "mode": "embedded",
        }

    def send(self, message: Dict[str, Any]) -> Dict[str, Any]:
        prompt = message.get("content", "")

        npx_cmd = "npx.cmd" if os.name == "nt" else "npx"

        try:
            result = subprocess.run(
                [
                    npx_cmd,
                    "openclaw",
                    "agent",
                    "--agent",
                    "main",
                    "--message",
                    prompt,
                    "--local",
                    "--json",
                ],
                cwd=os.path.expanduser("~/MyAITeam/openclaw"),
                capture_output=True,
                text=True,
                timeout=40,
            )

            if result.returncode != 0:
                return {
                    "reply": result.stderr.strip(),
                    "confidence": 0.0,
                }

            # 🔥 CLEAN PARSING STARTS HERE
            raw = result.stdout.strip()

            try:
                data = json.loads(raw)

                payloads = data.get("payloads", [])
                if payloads and "text" in payloads[0]:
                    clean_text = payloads[0]["text"]
                else:
                    clean_text = raw

            except json.JSONDecodeError:
                clean_text = raw

            return {
                "reply": clean_text,
                "confidence": 0.55,
            }

        except subprocess.TimeoutExpired:
            return {
                "reply": "OpenClaw adapter timeout",
                "confidence": 0.0,
            }

        except Exception as e:
            return {
                "reply": f"OpenClaw adapter exception: {e}",
                "confidence": 0.0,
            }

    def health(self) -> Dict[str, Any]:
        return {"status": "ok"}