\# CRE Kernel — Open Source Policy



This document defines the \*\*open-source scope, ownership, and contribution model\*\*

for the CRE Kernel project.



It exists to remove ambiguity around:

\- what is open vs private

\- how AI tools were used

\- who owns the intellectual direction



---



\## 1. Project Structure \& Scope



CRE Kernel is developed in \*\*two related repositories\*\*:



\### 1.1 CRE Kernel (Core)



\- Purpose: foundational reasoning kernel

\- Status: \*\*private / restricted\*\*

\- Role: long-term research \& kernel invariants

\- Changes: conservative, infrequent, audited



The Core defines:

\- trust model

\- consensus rules

\- authority semantics

\- kernel invariants



---



\### 1.2 CRE Kernel Lab (This Repository)



\- Purpose: experimentation, hardening, validation

\- Status: \*\*open source\*\*

\- License: MIT

\- Role: proving correctness, safety, and extensibility



This repository contains:

\- experimental refinements

\- security hardening

\- adapter evolution

\- AI-assisted improvements

\- documentation and analysis artifacts



\*\*CRE Kernel Lab is safe to fork, study, and build upon.\*\*



---



\## 2. License \& Ownership



This repository is released under the \*\*MIT License\*\*.



This means:

\- You may use, modify, and distribute the code

\- You must preserve copyright and license notices

\- There is \*\*no warranty\*\*



\### Ownership Clarification



\- The \*\*original system architecture, kernel philosophy, and direction\*\*

&nbsp; are authored and maintained by the project owner.

\- MIT license \*\*does not transfer authorship or design intent\*\*.

\- Forks may diverge, but cannot claim original authorship.



---



\## 3. AI-Assisted Development Disclosure



This project \*\*intentionally uses AI tools\*\* as engineering assistants.



Tools used include (but are not limited to):

\- OpenAI Codex

\- Google Jules

\- Large language models for review, refactoring, and audit support



\### Important Clarification



\- AI tools \*\*do not own the code\*\*

\- AI tools \*\*do not make architectural decisions\*\*

\- AI tools \*\*do not define kernel invariants\*\*



All final decisions are:

\- reviewed by the maintainer

\- manually approved

\- committed by a human



AI assistance is treated the same way as:

\- static analyzers

\- linters

\- security scanners

\- code review tools



---



\## 4. Why AI Contributions Are Allowed Here



CRE Kernel Lab exists specifically to:



\- stress-test assumptions

\- surface edge cases

\- identify security gaps

\- validate correctness

\- harden APIs



AI tools are effective at:

\- finding inconsistencies

\- suggesting refactors

\- detecting missing checks

\- generating reproduction cases



They are \*\*not\*\* trusted with:

\- defining truth semantics

\- modifying kernel authority rules

\- changing trust math



---



\## 5. Contribution Rules



Contributions are welcome \*\*within scope\*\*.



Allowed:

\- bug fixes

\- security hardening

\- documentation improvements

\- adapter experiments

\- test coverage



Not allowed without explicit approval:

\- changing kernel invariants

\- redefining trust semantics

\- bypassing signature checks

\- weakening audit guarantees



Pull requests may be rejected if they violate kernel principles.



---



\## 6. Forking \& Commercial Use



Forking is allowed under MIT.



However:

\- claiming to be the “official CRE Kernel” is not permitted

\- misrepresenting experimental code as stable core is discouraged

\- removing attribution violates license terms



Commercial use is allowed under MIT,

but \*\*responsibility remains with the user\*\*.



---



\## 7. Why This Separation Exists



This separation protects:

\- long-term research integrity

\- architectural coherence

\- safety guarantees

\- public experimentation



It also ensures:

\- open collaboration where safe

\- controlled evolution where necessary



---



\## 8. Summary



\- \*\*CRE Kernel Core\*\* → private, stable, slow-moving

\- \*\*CRE Kernel Lab\*\* → open, experimental, fast-moving

\- MIT license applies to this repository

\- AI tools assisted, humans decide

\- Trust, authority, and memory are never compromised



---



Maintainer:

Vishal  

CRE Kernel Project

