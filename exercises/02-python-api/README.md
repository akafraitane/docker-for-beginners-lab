# Exercise 02: Python API

Build a Python Flask API container.

## Steps

1. Build the image:
```bash
docker build -t python-api:v1 .
```

2. Run the container:
```bash
docker run -d -p 5000:5000 --name my-python-api python-api:v1
```

3. Test the API:
```bash
curl http://localhost:5000
curl http://localhost:5000/health
curl http://localhost:5000/info
```

4. Run with custom environment variables:
```bash
docker run -d -p 5000:5000 -e APP_VERSION=2.0.0 --name my-python-api-v2 python-api:v1
```

## Challenge

Add a new endpoint `/time` that returns just the current time!
