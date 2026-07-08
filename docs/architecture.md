# System Architecture

# AI Research Assistant

---

# High-Level Architecture

```text
                 User
                   │
                   ▼
          Research Agent
                   │
      ┌────────────┴────────────┐
      ▼                         ▼
   Planner               Tool Executor
      │                         │
      ▼                         ▼
 Gemini Client            Registered Tools
      │
      ▼
Report Generator
```

---

# Core Components

## Research Agent

The central orchestrator responsible for managing the research workflow.

Responsibilities:

- Receive user requests
- Coordinate planning
- Execute tools
- Collect observations
- Generate reports

---

## Planner

Responsible for transforming a research request into a structured execution plan.

---

## LLM Client

Responsible for communicating with the Large Language Model.

Initially:

- Gemini API

Future:

- OpenAI
- Anthropic
- Local Models

---

## Tool Executor

Executes available tools requested by the planner.

Examples:

- Search
- Calculator
- Python
- File Writer

---

## Report Generator

Transforms observations into a structured research report.

---

# Data Flow

User

↓

Research Agent

↓

Planner

↓

LLM

↓

Execution Plan

↓

Tool Executor

↓

Observations

↓

Report Generator

↓

Final Report

---

# Architectural Principles

- Separation of Concerns
- Dependency Injection
- Clean Architecture
- Low Coupling
- High Cohesion
- Single Responsibility Principle