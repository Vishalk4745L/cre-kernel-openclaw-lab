"""
proof_multi_agent_consensus.py

This example demonstrates:
- 4 role-based OpenClaw agents (Junior, Senior, Tool, All-Rounder)
- All agents receive the SAME question
- CRE Kernel Resolver orchestrates them
- A single, deterministic final answer is produced

This proves:
- One OpenClaw install can power multiple agents
- Kernel controls consensus, not agents
- No infinite loops, no agent storms, no prompt chaos
"""

"""
proof_multi_agent_consensus.py

CRE Kernel × OpenClaw
Multi-Agent Consensus Proof
"""

import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from kernel.resolver import Resolver

def run_proof():
    resolver = Resolver()

    questions = [
        "Is it safe to store API keys in a public GitHub repo?",
        "Is blockchain always required for trust?",
        "How should a leaked API key be handled?",
    ]

    print("=" * 70)
    print("CRE KERNEL × OPENCLAW — MULTI-AGENT CONSENSUS PROOF")
    print("=" * 70)

    for q in questions:
        print("\nQUESTION:")
        print(q)

        msg = {
            "source": "proof-lab",
            "type": "claim",
            "content": q,
            "confidence": 0.9,
        }

        result = resolver.resolve(msg)

        print("\nFINAL ANSWER (Kernel Consensus):")
        print(result["final_reply"])

        print("\nAGENT RESPONSES:")
        for r in result["all_responses"]:
            print(f"- {r['agent']} : {r['reply']}")

        print("\n" + "-" * 70)


if __name__ == "__main__":
    run_proof()