\# EXPERIMENTAL ZONE — CRE Kernel Lab



⚠️ \*\*WARNING: THIS IS NOT CANONICAL CODE\*\*



This repository (`cre-kernel-lab`) is an \*\*experimental sandbox\*\* for the CRE Kernel project.

All changes here are \*\*non-authoritative\*\*, \*\*non-final\*\*, and \*\*may be discarded\*\*.



---



\## Purpose



The purpose of this lab is to:



\- Run controlled experiments using AI coding agents (Codex, Jules, etc.)

\- Test refactors, security ideas, and architectural alternatives

\- Validate hypotheses before proposing changes to the canonical kernel

\- Generate Pull Requests (PRs) for review — \*\*not direct merges\*\*



---



\## Canonical Source of Truth



\- \*\*Authoritative repository:\*\* `cre-kernel`

\- \*\*Authoritative branch:\*\* `main`

\- \*\*Design authority:\*\* DESIGN\_v\*.md files in the canonical repo



Nothing in this lab is considered truth until:

1\. A PR is created

2\. The PR is reviewed

3\. The PR is manually merged into `cre-kernel`



---



\## Rules of Engagement



\### 1. No Direct Authority

\- Code in this repo has \*\*zero authority\*\*

\- Security guarantees here are \*\*not trusted\*\*

\- Bugs are expected



\### 2. AI Agents Are Tools, Not Deciders

\- Codex may refactor, restructure, or optimize

\- Jules may audit, review, and propose fixes

\- \*\*Neither agent has merge authority\*\*



\### 3. All AI Changes Must Go Through PRs

\- Codex output → PR

\- Jules output → PR

\- No silent or automatic merges



\### 4. Explicit Experiment Labeling

All experimental changes must be clearly labeled as:

\- `experimental`

\- `unsafe`

\- `draft`

\- or `research-only`



---



\## Planned Workflow



1\. Establish experimental boundaries (this document)

2\. Run Codex to generate structured change PRs

3\. Run Jules for review-only or security-audit PRs

4\. Manually evaluate PRs

5\. Cherry-pick or rewrite changes for `cre-kernel`



---



\## What This Repo Is NOT



\- ❌ Not production code

\- ❌ Not security-hardened

\- ❌ Not backward compatible

\- ❌ Not guaranteed to persist



---



\## Mental Model



> \*\*CRE Kernel Lab is a wind tunnel.  

> CRE Kernel is the aircraft.\*\*



Break things here so the real system survives.



---



\_Last updated: Feb 2026\_

