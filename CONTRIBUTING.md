\# Contributing to CRE Kernel



Thank you for your interest in contributing to \*\*CRE Kernel\*\*.



CRE Kernel is not a typical application project.

It is a \*\*kernel-level reasoning infrastructure\*\* where stability, trust, and correctness matter more than speed.



Please read this document carefully before contributing.



---



\## 1. Project Philosophy



CRE Kernel follows three core principles:



1\. \*\*Kernel logic must remain stable\*\*

2\. \*\*Trust and authority are first-class concepts\*\*

3\. \*\*Memory and reasoning must be auditable\*\*



This means:

\- Not all changes are acceptable

\- Refactors are not always improvements

\- Convenience is never prioritized over correctness



---



\## 2. Repository Structure



\### Stable Core

Files under:



kernel/core/



are considered \*\*kernel core\*\*.



These files:

\- Change slowly

\- Require careful review

\- Must preserve invariants



\### Adapters \& Experiments

Files under:



kernel/adapters/ agents/ cre-kernel-lab/



are more flexible and experimental.



---



\## 3. Contribution Types



\### ✅ Accepted Contributions



\- Bug fixes (with clear explanation)

\- Security patches

\- Documentation improvements

\- Adapter implementations

\- Test coverage

\- Performance improvements (measured)



\### ❌ Not Accepted Without Discussion



\- Large refactors of kernel/core

\- Removing safety checks

\- Simplifying logic by removing trust / authority handling

\- Changing consensus semantics

\- Replacing kernel logic with model output



If in doubt — \*\*open an issue first\*\*.



---



\## 4. Pull Request Rules



Every Pull Request MUST:



\- Have a clear title

\- Explain \*\*why\*\* the change is needed

\- Explain \*\*what invariant is preserved\*\*

\- State whether it is:

&nbsp; - Bug fix

&nbsp; - Security fix

&nbsp; - Refactor

&nbsp; - Feature

\- Include tests if logic is changed



PRs without explanation may be rejected.



---



\## 5. AI-Assisted Contributions (IMPORTANT)



This project \*\*allows AI-assisted development\*\*, including:



\- OpenAI Codex

\- Google Jules

\- Other code analysis tools



However:



\- Contributors are \*\*fully responsible\*\* for AI-generated code

\- AI output must be reviewed by a human

\- AI tools must NOT:

&nbsp; - Remove security checks

&nbsp; - Change trust semantics silently

&nbsp; - Bypass authority validation

&nbsp; - Introduce hidden behavior



If AI was used, mention it in the PR description.



---



\## 6. Experimental vs Stable Code



\- Experimental changes belong in:

&nbsp; - `cre-kernel-lab`

&nbsp; - Feature branches

\- Stable kernel changes require:

&nbsp; - Extra review

&nbsp; - Clear justification

&nbsp; - Compatibility consideration



Do not mix experimental logic into stable kernel paths.



---



\## 7. Coding Standards



\- Prefer clarity over cleverness

\- Explicit > implicit

\- Avoid magic constants

\- Add comments where reasoning is non-obvious

\- No silent failure paths



Kernel code should be readable by another engineer \*\*without context\*\*.



---



\## 8. Security Reporting



If you find a security issue:



\- \*\*Do NOT open a public issue\*\*

\- Follow `SECURITY.md`

\- Provide reproduction steps

\- Provide impact assessment



Security fixes take priority over features.



---



\## 9. Licensing



By contributing, you agree that:



\- Your contributions are licensed under the project’s MIT License

\- You have the right to submit the code

\- You are not violating third-party licenses



---



\## 10. Final Note



CRE Kernel is infrastructure.

It is closer to an operating system than an app.



Contribute carefully.

Design thoughtfully.

Break things only when absolutely necessary.



---



Maintainer: Vishal  

CRE Kernel Project





---





