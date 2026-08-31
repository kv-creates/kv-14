"""Weight downloader from HuggingFace Hub"""
import os

def download(variant="kv14-14b-instruct-q4", dest="checkpoints/"):
    print(f"Downloading kv-creates/KV-14:{variant} to {dest}")
    print("Size: ~8.2GB (Q4) | 28GB (FP16)")
    print("hf hub: https://huggingface.co/kv-creates/KV-14")
    # from huggingface_hub import snapshot_download
    # snapshot_download(repo_id="kv-creates/KV-14", allow_patterns=[f"{variant}/*"], local_dir=dest)
    os.makedirs(dest, exist_ok=True)
    print("Download placeholder - use: python model/inference/download.py --variant kv14-14b-instruct-q4")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--variant", default="kv14-14b-instruct-q4")
    p.add_argument("--dest", default="checkpoints/")
    args = p.parse_args()
    download(args.variant, args.dest)
