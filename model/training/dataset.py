"""Dataset pipeline - 1.4T tokens (The Stack v2 + CVEFixes + 4M PRs)"""
import torch
from torch.utils.data import Dataset

class KV14Dataset(Dataset):
    def __init__(self, data_path, tokenizer, split="train"):
        self.tokenizer = tokenizer
        self.samples = []  # In production: load from parquet shards
        print(f"KV14Dataset {split}: would load from {data_path} - 1.4T tokens")

    def __len__(self):
        return 10000  # placeholder

    def __getitem__(self, idx):
        # Returns (input_ids, labels, task_type)
        return {
            "input_ids": torch.randint(0, 52000, (2048,)),
            "labels": torch.randint(0, 52000, (2048,)),
            "task": "lm"
        }

def collate_fn(batch):
    return {
        "input_ids": torch.stack([b["input_ids"] for b in batch]),
        "labels": torch.stack([b["labels"] for b in batch]),
    }
