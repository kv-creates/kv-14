"""Batch analyze folder."""
import pathlib
print(sorted(p.name for p in pathlib.Path('.').glob('*.py'))[:5])
