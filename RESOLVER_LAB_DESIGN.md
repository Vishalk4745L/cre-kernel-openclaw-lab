🧠 CRE Kernel Lab — Resolver Design



> The Resolver is the brainstem of the Kernel Lab.

Agents think. The Resolver decides.









---



1\. What Is the Resolver?



The Resolver is a deterministic orchestration component that:



Dispatches a single claim to multiple agents



Collects independent responses



Applies confidence \& policy rules



Produces a final, kernel-safe result





It is not an agent.

It is not a model.

It is not a memory store.



> The Resolver is a decision funnel, not a thinker.









---



2\. Resolver Design Goals



The Resolver must:



✅ Be agent-agnostic

✅ Be LLM-agnostic

✅ Support N agents

✅ Prevent cross-agent contamination

✅ Produce auditable decisions

✅ Fail safely (silence > hallucination)





---



3\. Resolver Placement in Architecture



User / System

&nbsp;     ↓

┌──────────────────────────┐

│        Resolver          │  ← This document

│   (Kernel Lab – Public)  │

└─────┬───────────┬────────┘

&nbsp;     ↓           ↓

┌──────────┐ ┌──────────┐

│ Adapter  │ │ Adapter  │   … N adapters

└──────────┘ └──────────┘



The Resolver:



Knows which adapters exist



Does not know how they work internally







---



4\. Canonical Message Contract



Every resolution starts with a canonical message.



{

&nbsp; "source": "user | system | agent",

&nbsp; "type": "claim | question | task",

&nbsp; "content": "string",

&nbsp; "confidence": 0.0 – 1.0

}



Design Rules



Resolver never mutates input message



Message is passed verbatim to all adapters



Adapters may interpret, but not rewrite







---



5\. Adapter Contract



Each adapter must return:



{

&nbsp; "reply": "string",

&nbsp; "confidence": 0.0 – 1.0

}



Optional (future):



metadata



latency



cost



trace id





If an adapter fails:



Resolver records failure



Resolution continues







---



6\. Resolver Execution Flow



Step-by-Step



1\. Receive message





2\. Validate schema





3\. Load adapter registry





4\. Dispatch message to adapters





5\. Collect responses





6\. Apply resolution policy





7\. Return final result + trace









---



Pseudocode (Conceptual)



responses = \[]



for adapter in adapters:

&nbsp;   try:

&nbsp;       r = adapter.send(message)

&nbsp;       responses.append({

&nbsp;           "agent": adapter.id,

&nbsp;           "reply": r.reply,

&nbsp;           "confidence": r.confidence

&nbsp;       })

&nbsp;   except Exception as e:

&nbsp;       responses.append({

&nbsp;           "agent": adapter.id,

&nbsp;           "error": str(e),

&nbsp;           "confidence": 0.0

&nbsp;       })



final = resolve(responses)

return final





---



7\. Resolver Output Structure



{

&nbsp; "final\_reply": "string | null",

&nbsp; "confidence": 0.0 – 1.0,

&nbsp; "all\_responses": \[

&nbsp;   {

&nbsp;     "agent": "openclaw-junior",

&nbsp;     "reply": "...",

&nbsp;     "confidence": 0.6

&nbsp;   }

&nbsp; ]

}



Why include all responses?



Auditability



Debugging



Research



Kernel trust evolution (private)







---



8\. Resolution Strategies (Lab Version)



Current Strategy: Consensus-First



Rules:



Prefer answers that match across agents



Ignore outliers



Break ties by confidence



If no consensus → abstain







---



Example



Agents reply:



Agent	Reply	Confidence



Junior	A	0.6

Senior	A	0.8

Tool	B	0.7





Result:



Final = A (confidence ≈ 0.7)





---



9\. Why Agents Cannot See Each Other



Critical safety rule:



> Agents are blind to peers.







Why?



Prevent collusion



Prevent echo chambers



Prevent prompt poisoning



Preserve independence





Resolver is the only aggregation point.





---



10\. Failure Handling Matrix



Scenario	Resolver Action



Agent timeout	Skip

Agent crash	Skip

Empty reply	Ignore

Low confidence	Downweight

All fail	Return null

Conflicting replies	Abstain





The Resolver never fabricates answers.





---



11\. Why Resolver Is Stateless



The Resolver:



Does not store memory



Does not learn



Does not adapt





Why?



> State belongs to the Kernel Core, not the Lab.







This keeps:



Experiments safe



Public code harmless



Core logic protected







---



12\. Resolver vs Agent Comparison



Aspect	Resolver	Agent



Talks to LLM	❌	✅

Holds memory	❌	⚠️

Makes decisions	✅	❌

Trust-aware	⚠️ (limited)	❌

Replaceable	❌	✅







---



13\. Scaling Properties



Infinite Agents



Resolver loops dynamically



Adapter list is config-driven



No code changes required





Infinite Memory



Resolver does not store memory



Kernel Core handles persistence







---



14\. Security Properties



The Resolver prevents:



✅ Prompt injection persistence

✅ Cross-agent poisoning

✅ Tool escalation

✅ Silent drift



It is a containment layer.





---



15\. What the Resolver Is NOT



❌ Not an AI

❌ Not a chatbot

❌ Not a planner

❌ Not an agent



It is a judge, not a thinker.





---



16\. Extension Points (Future)



Planned but not in lab:



Weighted trust graphs



Agent reputation decay



Historical accuracy scoring



Temporal confidence adjustment







---



17\. Why This Design Matters



Without a resolver:



Agents hallucinate unchecked



Memory becomes corrupted



Systems drift silently





With a resolver:



Beliefs are earned



Truth is negotiated



Errors are contained







---



18\. Summary (One Line)



> The Resolver turns many opinions into one belief — safely.









---



🧠 End of Resolver Design Document







