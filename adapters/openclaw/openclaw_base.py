import os
import subprocess
import json
from typing import Dict, Any
from adapters.adapter_interface import AgentAdapter


class OpenClawBaseAdapter(AgentAdapter):
    """
    OpenClaw Base Adapter (NON-INTERACTIVE, EMBEDDED MODE)

    Design guarantees:
    - No gateway dependency
    - No TUI / stdin
    - Kernel-controlled execution
    - Windows + Linux safe
    - Unicode-safe (emojis, Gemini output)
    """

    adapter_id = "openclaw-base"
    adapter_type = "agent"

    AGENT_NAME = "main"  # overridden by subclasses

    def capabilities(self) -> Dict[str, Any]:
        return {
            "reasoning": True,
            "tools": True,
            "confidence": 0.6,
            "mode": "embedded",
        }

    def send(self, message: Dict[str, Any]) -> Dict[str, Any]:
        prompt = (message.get("content") or "").strip()
        if not prompt:
            return {"reply": "Empty prompt", "confidence": 0.0}

        # Windows-safe npx
        npx_cmd = "npx.cmd" if os.name == "nt" else "npx"

        cmd = [
            npx_cmd,
            "openclaw",
            "agent",
            "--agent", self.AGENT_NAME,
            "--message", prompt,
            "--local",
            "--json",
        ]

        try:
            result = subprocess.run(
                cmd,
                cwd=os.path.expanduser("~/.openclaw"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",      # 🔑 CRITICAL FIX
                errors="ignore",       # 🔑 CRITICAL FIX
                timeout=40,
            )

            stdout = (result.stdout or "").strip()
            stderr = (result.stderr or "").strip()

            if result.returncode != 0:
                return {
                    "reply": stderr or stdout or "OpenClaw execution failed",
                    "confidence": 0.0,
                }

            if not stdout:
                return {
                    "reply": "OpenClaw returned empty output",
                    "confidence": 0.0,
                }

            # ---- JSON extraction (robust) ----
            reply_text = stdout

            try:
                data = json.loads(stdout)
                if isinstance(data, dict):
                    payloads = data.get("payloads")
                    if isinstance(payloads, list) and payloads:
                        reply_text = payloads[0].get("text") or stdout
            except Exception:
                # Non-JSON output (warnings, logs, etc.)
                reply_text = stdout

            return {
                "reply": reply_text.strip(),
                "confidence": 0.6,
            }

        except subprocess.TimeoutExpired:
            return {
                "reply": "OpenClaw timeout exceeded",
                "confidence": 0.0,
            }

        except Exception as e:
            return {
                "reply": f"OpenClaw adapter exception: {e}",
                "confidence": 0.0,
            }

    def health(self) -> Dict[str, Any]:
        return {"status": "ok"}