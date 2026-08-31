# Training KV-14

```bash
python model/training/prepare.py --config model/training/config.yaml
torchrun --nproc_per_node=8 model/training/train.py --config model/training/config.yaml
python model/training/eval.py --checkpoint checkpoints/kv14-final
```
