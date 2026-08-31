"""Training pipeline - 14B with FlashAttention-2, ZeRO-3, 8x H100"""
import yaml
import torch
from .dataset import KV14Dataset

CONFIG_PATH = "model/training/config.yaml"

def load_config(path=CONFIG_PATH):
    with open(path) as f:
        return yaml.safe_load(f)

def train(config_path=CONFIG_PATH):
    cfg = load_config(config_path)
    print(f"Training KV-14 with {cfg['model']['params']} params")
    print(f"Tokens: {cfg['data']['tokens']} | GPUs: {cfg['training']['gpus']}")
    # torchrun --nproc_per_node=8 model/training/train.py --config model/training/config.yaml
    # DeepSpeed ZeRO-3 + FlashAttention-2 + bf16
    print("Training placeholder - run with 8x H100 for 5 days")

if __name__ == "__main__":
    train()
