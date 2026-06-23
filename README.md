# test-repo

A minimal FastAPI application for exercising the CI/CD pipeline (build, test, containerize, deploy).

## Endpoints

| Method | Path      | Description            |
|--------|-----------|------------------------|
| GET    | `/`       | Hello payload          |
| GET    | `/health` | Liveness/readiness `{"status":"ok"}` |

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 8080
# http://localhost:8080  and  http://localhost:8080/health
```

## Test

```bash
pip install -r requirements-dev.txt
pytest
```

## Docker

```bash
docker build -t test-repo:latest .
docker run --rm -p 8080:8080 test-repo:latest
```

## Deploy (Kubernetes)

```bash
kubectl apply -f k8s/deployment.yaml
```

The container listens on port `8080` and exposes `/health` for readiness/liveness probes.
