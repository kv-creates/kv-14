"""Model tests"""
from model.kv14 import KV14Config, KV14Model

def test_config():
    cfg = KV14Config()
    assert cfg.hidden_size == 5120
    assert cfg.num_hidden_layers == 42

def test_model_forward():
    cfg = KV14Config()
    # Use small config for fast test
    cfg.hidden_size = 64
    cfg.num_hidden_layers = 2
    cfg.num_attention_heads = 4
    cfg.intermediate_size = 128
    model = KV14Model(cfg)
    import torch
    ids = torch.randint(0, cfg.vocab_size, (1, 8))
    out = model(ids)
    assert out.shape == (1, 8, cfg.vocab_size)

def test_bug_head():
    cfg = KV14Config(hidden_size=32, num_hidden_layers=1, num_attention_heads=2, intermediate_size=64)
    model = KV14Model(cfg)
    import torch
    ids = torch.randint(0, cfg.vocab_size, (1, 4))
    score = model(ids, task="bug")
    assert 0 <= score.item() <= 1
