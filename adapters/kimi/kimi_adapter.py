import os
import requests
from typing import Dict, Any
from adapters.adapter_interface import AgentAdapter


class KimiAdapter(AgentAdapter):
    """
    Kimi K2.5 Adapter (REST-based)

    Design notes:
    - No local model
    - No CLI
    - Pure HTTP (fast + stable)
    - Kernel-safe (returns clean text only)
    """

    adapter_id = "kimi"
    adapter_type = "agent"

    def __init__(self):
        # API key must be set as env variable
        self.api_key = os.getenv("KIMI_API_KEY")

        if not self.api_key:
            raise RuntimeError(
                "KIMI_API_KEY not set. "
                "Run: setx KIMI_API_KEY \"your_key_here\""
            )

        self.endpoint = "https://api.moonshot.cn/v1/chat/completions"

    def capabilities(self) -> Dict[str, Any]:
        return {
            "reasoning": True,
            "long_context": True,
            "confidence": 0.7,
            "mode": "rest",
        }

    def send(self, message: Dict[str, Any]) -> Dict[str, Any]:
        prompt = message.get("content", "")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "kimi-k2.5",
            "messages": [
                {"role": "system", "content": "Answer concisely."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.4,
        }

        try:
            resp = requests.post(
                self.endpoint,
                headers=headers,
                json=payload,
                timeout=30,
            )

            if resp.status_code != 200:
                return {
                    "reply": f"Kimi API error: {resp.text}",
                    "confidence": 0.0,
                }

            data = resp.json()
            text = data["choices"][0]["message"]["content"]

            return {
                "reply": text.strip(),
                "confidence": 0.65,
            }

        except requests.Timeout:
            return {
                "reply": "Kimi adapter timeout",
                "confidence": 0.0,
            }

        except Exception as e:
            return {
                "reply": f"Kimi adapter exception: {e}",
                "confidence": 0.0,
            }

    def health(self) -> Dict[str, Any]:
        return {"status": "ok"}