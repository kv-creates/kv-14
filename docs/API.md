# API Reference

Base: `http://localhost:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | /health | Health |
| POST | /v1/analyze | Bugs + risk + security |
| POST | /v1/fix | Auto-fix diff |
| POST | /v1/review | Swarm review |
| POST | /v1/swarm | Full 5-agent run |
| POST | /v1/modernize | Legacy modernize |
| POST | /v1/test-gen | Test generation |
| POST | /v1/security | Security scan |
| GET | /docs | OpenAPI |

## Example

```bash
curl -X POST http://localhost:8000/v1/analyze \
 -H "Content-Type: application/json" \
 -d "{\"code\":\"def foo(x): return x/0\", \"language\":\"python\"}"
```
