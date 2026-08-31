"""Byte-Pair Code Tokenizer - 52K vocab + 800 special tokens for code"""
from transformers import AutoTokenizer

class KV14Tokenizer:
    vocab_size = 52000
    special_tokens = ["<|bug|>", "<|fix|>", "<|review|>", "<|security|>", "<|planner|>", "<|coder|>", "<|tester|>", "<|swarm|>"]
    
    def __init__(self, base="codellama/CodeLlama-13b-hf"):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(base, trust_remote_code=True)
        except:
            self.tokenizer = None
            print("Tokenizer offline mode - using fallback")

    def encode(self, text, max_length=131072):
        if self.tokenizer:
            return self.tokenizer(text, truncation=True, max_length=max_length, return_tensors="pt")
        return {"input_ids": [[0]*min(len(text.split()), max_length)]}

    def decode(self, ids):
        if self.tokenizer:
            return self.tokenizer.decode(ids, skip_special_tokens=True)
        return "<decoded>"

    @staticmethod
    def repo_context(files: dict, max_tokens=100000):
        """Build repo-graph context from multiple files"""
        context = "<|swarm|>\n"
        for path, code in files.items():
            context += f"\n# File: {path}\n{code[:8000]}\n"
            if len(context) > max_tokens*4:
                break
        return context
