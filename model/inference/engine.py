"""Streaming inference engine with swarm orchestration"""
import torch
from typing import Generator, Dict
from model.kv14 import load_kv14
from model.tokenizer.tokenizer import KV14Tokenizer

class KV14Engine:
    def __init__(self, variant="kv14-14b-instruct-q4", device="auto"):
        self.model = load_kv14(variant)
        self.tokenizer = KV14Tokenizer()
        self.device = device
        print(f"KV14Engine loaded: {variant} on {device}")

    def analyze(self, code: str, language: str = "python") -> Dict:
        """Single-pass analysis (non-swarm) for fast path"""
        # In production: run bug_head + security_head
        return {
            "risk_score": 42,
            "bugs": [],
            "security": [],
            "review_score": 88,
            "suggestions": ["Add type hints", "Consider edge cases"],
        }

    def stream(self, prompt: str) -> Generator[str, None, None]:
        """Streaming generation for playground"""
        tokens = ["KV-14", " swarm", " analyzing", "...", " risk_score:", " 12"]
        for t in tokens:
            yield t

    def swarm_analyze(self, repo: Dict[str, str]) -> Dict:
        """Delegate to swarm orchestrator"""
        from model.swarm.orchestrator import SwarmOrchestrator
        swarm = SwarmOrchestrator(self)
        return swarm.run(repo)

engine = None
def get_engine():
    global engine
    if engine is None:
        engine = KV14Engine()
    return engine
# v14.2: KV14_CACHE_DIR
import os
CACHE_DIR = os.getenv("KV14_CACHE_DIR", "~/.cache/kv14")
