"""Model package - tolerant to missing torch for CI without GPU"""
try:
    from .kv14 import KV14Model, KV14Config, load_kv14
except Exception as e:
    KV14Model = None
    KV14Config = None
    load_kv14 = lambda *a, **kw: None
    print(f"Warning: KV14 model not loaded ({e}) - running in offline mode")
