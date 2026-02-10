import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from kernel.resolver import Resolver

resolver = Resolver()

tests = [
    "Is it safe to store API keys in a public GitHub repo?",
    "Is blockchain always required for trust?",
    "How should a leaked API key be handled?"
]

for t in tests:
    print("\n==============================")
    print("QUESTION:", t)

    msg = {
        "source": "user",
        "type": "claim",
        "content": t,
        "confidence": 0.8
    }

    result = resolver.resolve(msg)

    print("\nFINAL ANSWER:")
    print(result["final_reply"])

    print("\nAGENT RESPONSES:")
    for r in result["all_responses"]:
        print("-", r["agent"], ":", r["reply"])