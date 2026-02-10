import os
import subprocess
import json
from typing import Dict, Any
from adapters.adapter_interface import AgentAdapter


class OpenClawBaseAdapter(AgentAdapter):
    """
    OpenClaw Base Adapter (Kernel-safe, OpenRouter-safe)

    Guarantees:
    - Never crashes the Kernel
    - Works with OpenRouter / Gemini / Groq
    - Does NOT rely on stopReason (unreliable)
    - Payload-first parsing (correct OpenClaw behavior)
    - Windows-safe encoding
    """

    adapter_id = "openclaw-base"
    adapter_type = "agent"

    # Overridden by subclasses (junior / senior / tool / allrounder)
    AGENT_NAME = "main"

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

        npx = "npx.cmd" if os.name == "nt" else "npx"

        cmd = [
            npx,
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
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=90,
            )

            raw = (result.stdout or result.stderr or "").strip()
            if not raw:
                return {
                    "reply": "⚠️ OpenClaw returned empty output",
                    "confidence": 0.0,
                }

            # -------------------------------
            # JSON parsing (best-effort)
            # -------------------------------
            try:
                data = json.loads(raw)
            except Exception:
                # Non-JSON but valid text → still return
                return {
                    "reply": raw,
                    "confidence": 0.4,
                }

            # -------------------------------
            # ✅ PRIMARY SUCCESS PATH
            # OpenClaw success = payloads exist
            # -------------------------------
            payloads = data.get("payloads")
            if isinstance(payloads, list) and payloads:
                text = payloads[0].get("text")
                if text:
                    return {
                        "reply": text.strip(),
                        "confidence": 0.6,
                    }

            # -------------------------------
            # Explicit error block (rare)
            # -------------------------------
            if "error" in data:
                err = data.get("error", {})
                msg = err.get("message", "Unknown OpenClaw error")
                return {
                    "reply": f"⚠️ OpenClaw error: {msg}",
                    "confidence": 0.0,
                }

            # -------------------------------
            # Fallback — valid JSON but no text
            # -------------------------------
            return {
                "reply": "⚠️ OpenClaw returned no usable text payload",
                "confidence": 0.0,
            }

        except subprocess.TimeoutExpired:
            return {
                "reply": "⚠️ OpenClaw timeout",
                "confidence": 0.0,
            }

        except Exception as e:
            return {
                "reply": f"⚠️ OpenClaw exception: {e}",
                "confidence": 0.0,
            }

    def health(self) -> Dict[str, Any]:
        return {"status": "ok"}