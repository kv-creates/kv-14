# KV-14 Deployment

## Netlify (website)

1. Drag `website/` to https://app.netlify.com/drop
2. Or `netlify deploy --prod --dir website`

## HuggingFace

Model at `kv-creates/KV-14` - quantized Q4 8.2GB.

## Docker

```bash
docker compose up --build
# API http://localhost:8000/docs | Web http://localhost:3000
```

## Local

```bash
pip install -r requirements.txt
uvicorn api.app:app --reload
pytest
```
