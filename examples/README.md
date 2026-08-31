# Examples

## 1. Analyze a file

```python
from api.client import KV14Client
client = KV14Client()
print(client.analyze_file("examples/vulnerable.py"))
```

## 2. Run swarm on a repo

```python
repo = {"app.py": open("app.py").read(), "utils.py": open("utils.py").read()}
print(client.swarm(repo, goal="fix all critical bugs and add tests"))
```

## 3. CLI

```bash
kv14 analyze examples/vulnerable.py
kv14 fix examples/vulnerable.py --apply
kv14 swarm . --goal "modernize to python3"
```
