"""
CRE KERNEL × OPENCLAW
AUTONOMOUS MULTI-AGENT WEB RESEARCH DEMO

Scenario:
---------
A team of 4 role-based OpenClaw agents collaborates to answer
a complex research question using CRE Kernel consensus.

Agents:
- Junior Agent      → Simple explanation
- Senior Agent      → Deep analysis & risks
- Tool Agent        → Action-oriented / procedural view
- AllRounder Agent  → Balanced synthesis

Kernel:
- Collects all responses
- Resolves conflicts
- Produces a final trusted answer
"""

import sys
import os

# Ensure project root is in path
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from kernel.resolver import Resolver


def run_autonomous_research():
    print("=" * 70)
    print("CRE KERNEL × OPENCLAW — AUTONOMOUS WEB RESEARCH TEAM")
    print("=" * 70)

    resolver = Resolver()

    # High-level autonomous task
    task = {
        "source": "demo",
        "type": "research-task",
        "confidence": 0.95,
        "content": (
            "Research how companies use AI agents to automate web browsing "
            "and data collection. Identify real-world use cases, benefits, "
            "and potential risks. Answer in clear, concise terms."
        ),
    }

    print("\nTASK:")
    print(task["content"])
    print("\n---\n")

    # Kernel resolves using all connected agents
    result = resolver.resolve(task)

    print("FINAL ANSWER (Kernel Consensus):")
    print(result["final_reply"])

    print("\nAGENT CONTRIBUTIONS:")
    for response in result["all_responses"]:
        print(f"- {response['agent']} : {response['reply']}")

    print("\n---")
    print("✔ Autonomous multi-agent reasoning completed")
    print("✔ OpenClaw executed agents")
    print("✔ CRE Kernel resolved consensus")
    print("=" * 70)


if __name__ == "__main__":
    run_autonomous_research()