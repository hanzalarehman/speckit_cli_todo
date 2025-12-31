---
id: "001"
title: "Create global constitution"
stage: "constitution"
date: "2026-01-01"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "master"
user: "human"
command: "/sp.constitution"
labels: ["constitution","governance","principles"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - ".specify/memory/constitution.md"
tests:
  - "null"
---

## Prompt

Create a single global constitution for the entire "Evolution of Todo" project covering Phase I through Phase V.

This constitution must define:

Spec-Driven Development as mandatory

No agent may write code without approved specs and tasks
All work must follow: Constitution → Specs → Plan → Tasks → Implement
Agent Behavior Rules

No manual coding by humans
No feature invention
No deviation from approved specifications
Refinement must occur at spec level, not code level
Phase Governance

Each phase is strictly scoped by its specification
Future-phase features must never leak into earlier phases
Architecture may evolve only through updated specs and plans
Technology Constraints

Python for backend
Next.js for frontend (later phases)
FastAPI, SQLModel, Neon DB
OpenAI Agents SDK, MCP
Docker, Kubernetes, Kafka, Dapr (later phases)
Quality Principles

Clean architecture
Stateless services where required
Clear separation of concerns
Cloud-native readiness
This constitution must remain stabl

## Response snapshot

Created initial project constitution at `.specify/memory/constitution.md` with version 1.0.0. Defined five core principles: Spec-Driven Development (MANDATORY), Agent Behavior Rules, Phase Governance, Technology Constraints, and Quality Principles. Included detailed Technology Stack section covering all five phases, Development Workflow with mandatory flow and artifact locations, and Governance section with amendment procedures and compliance requirements.

## Outcome

- ✅ Impact: New constitution establishes governance framework for entire Evolution of Todo project
- 📁 Files: `.specify/memory/constitution.md`
- 🔁 Next prompts: Begin Phase I specification creation with approved constitution as foundation
- 🧠 Reflection: Initial constitution provides authoritative source for all subsequent development decisions

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "null"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"
