from adapters.openclaw.openclaw_junior import OpenClawJuniorAdapter
from adapters.openclaw.openclaw_senior import OpenClawSeniorAdapter
from adapters.openclaw.openclaw_tool import OpenClawToolAdapter
from adapters.openclaw.openclaw_allrounder import OpenClawAllRounderAdapter


class Resolver:
    def __init__(self):
        self.agents = [
            OpenClawJuniorAdapter(),
            OpenClawSeniorAdapter(),
            OpenClawToolAdapter(),
            OpenClawAllRounderAdapter(),
        ]

    def resolve(self, message: dict) -> dict:
        responses = []

        for agent in self.agents:
            result = agent.send(message)
            responses.append({
                "agent": agent.adapter_id,
                "reply": result.get("reply"),
                "confidence": result.get("confidence", 0.0),
            })

        # 🔹 Simple confidence-weighted resolver (v0)
        best = max(responses, key=lambda r: r["confidence"])

        return {
            "final_reply": best["reply"],
            "selected_agent": best["agent"],
            "all_responses": responses,
        }