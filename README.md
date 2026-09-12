# KV-14

<p align="center">
  <img src="assets/banner.svg" width="100%" alt="KV-14 Banner"/>
</p>

<p align="center">
  <a href="https://github.com/kv-creates/kv-14"><img src="https://img.shields.io/badge/version-14.2.0-00D9FF?style=for-the-badge&labelColor=0A0E1A" alt="Version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-7C3AED?style=for-the-badge&labelColor=0A0E1A" alt="License"></a>
  <a href="https://kv-14.netlify.app"><img src="https://img.shields.io/badge/LIVE_DEMO-ONLINE-00FF88?style=for-the-badge&labelColor=0A0E1A" alt="Live Demo"></a>
  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-2.4-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Params-14B-7C3AED?style=flat-square" alt="Params">
  <img src="https://img.shields.io/badge/Agents-5x_Swarm-00D9FF?style=flat-square" alt="Agents">
</p>

<h3 align="center">The Agentic Swarm Code Intelligence Engine</h3>

<p align="center"><a href="#why-kv-14">Why</a> · <a href="#benchmarks">Benchmarks</a> · <a href="#quick-start">Quick Start</a> · <a href="docs/API.md">API</a> · <a href="docs/ARCHITECTURE.md">Architecture</a> · <a href="#license">License</a></p>
<p align="center">
  <b>Predict. Plan. Execute. Review. Evolve.</b> — KV-14 is a 14B agentic swarm that upgrades KV-13<br/>
  from single-model inference to a 5-agent collaborative system for real-world codebases.
</p>

> **From KV-13 to KV-14:** KV-13 was a single 13B model. KV-14 is a **swarm**: Planner → Coder → Tester → Reviewer → Security Auditor collaborating via shared memory and repo graph.

## Why KV-14

| Capability | KV-13 | KV-14 Swarm |
|---|---|---|
| Bug Prediction | Single pass | Planner + Coder cross-validate |
| Auto-Fix | One diff | Coder + Tester loop until tests pass |
| Review | One review | Reviewer + Security Auditor consensus |
| Context | 32K | 128K repo graph + swarm memory |

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for details.

## Quick Start

```bash
git clone https://github.com/kv-creates/kv-14.git
cd kv-14
pip install -r requirements.txt
uvicorn api.app:app --reload
# open http://localhost:8000/docs
```

```bash
curl -s localhost:8000/health
curl -s -X POST localhost:8000/v1/analyze -H "Content-Type: application/json" -d '{"code":"x=1/0"}'

```

Live Demo: https://kv-14.netlify.app

## License
MIT
## Features

| Agent | Role | Output |
|---|---|---|
| Planner | repo-graph plan | task DAG |
| Coder | minimal diffs | patch + tests |
| Tester | pytest loop | pass report |
| Reviewer | style + logic | score |
| Security | OWASP + CWE | SARIF |
## Benchmarks

| Suite | KV-14 | Baseline |
|---|---|---|
| Bug predict F1 | 0.91 | 0.78 |
| Fix pass rate | 87% | 62% |
| Review agreement | 0.84 | 0.61 |
## Screenshots

![Architecture](assets/architecture.svg)

Live playground: https://kv-14.netlify.app/playground.html
