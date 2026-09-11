install:
	pip install -r requirements.txt
test:
	pytest -q
lint:
	ruff check .
run:
	uvicorn api.app:app --reload
