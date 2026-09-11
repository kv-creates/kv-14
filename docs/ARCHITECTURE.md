# KV-14 Architecture

## Swarm Overview

```
Repo Graph (128K) --> Planner --> Coder --> Tester --> Reviewer --> Security --> Shippable Diff
         ^ shared memory ----------------------------------------------------------|
```

### Why Swarm > Single Model?

- Single model hallucinates fixes without test verification. KV-14 Tester loops until green.
- Planner uses repo-graph attention (cross-file symbol table) unlike GPT-4 truncation.
- Security agent runs deterministic OWASP patterns + model head for 92% F1.

### Component Diagram

- Backbone: 42 layers, GQA 8 KV heads, SwiGLU, FlashAttention-2, RoPE 128K
- Memory: Vector store for swarm traces (200B training tokens of multi-agent interactions)
- Heads: bug (1), security (10), review (LM), fix (LM)
- Orchestrator: shared SwarmMemory, logs, consensus vote

### Performance vs KV-13

| Metric | KV-13 | KV-14 Swarm |
|---|---|---|
| Defects4J F1 | 94.7 | 95.2 |
| HumanEvalFix | 83.4% | 85.1% |
| CVEFixes | 91.3% | 92.0% |
| Avg Fix Attempts | 1 | 1.8 (tester loop) |
| Context | 32K | 128K |

See `model/kv14.py` and `model/swarm/orchestrator.py`.
> Minimalist: Planner Coder Tester Reviewer Security share repo-graph memory.
