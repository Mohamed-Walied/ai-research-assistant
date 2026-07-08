# Architecture Decision Records (ADR)

---

# ADR-001

## Title

Build the initial agent without frameworks.

## Status

Accepted

## Motivation

Understanding the internal implementation of agent systems provides deeper engineering knowledge than relying on abstractions from the beginning.

## Consequences

Pros

- Better understanding
- Easier debugging
- Framework-independent knowledge

Cons

- More implementation effort

---

# ADR-002

## Title

Use Gemini as the initial LLM provider.

## Status

Accepted

## Motivation

Gemini provides a capable API suitable for experimentation while allowing future replacement through an abstraction layer.

---

# ADR-003

## Title

Use Clean Architecture.

## Status

Accepted

## Motivation

Business logic should remain independent from external services and implementation details.

---

# ADR-004

## Title

Adopt Git Flow-inspired branching.

## Status

Accepted

## Strategy

- main
- develop
- feature/*
- bugfix/*
- docs/*
- refactor/*
- test/*