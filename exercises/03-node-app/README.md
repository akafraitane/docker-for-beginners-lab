# Exercise 03: Node.js App

Build a Node.js Express application container.

## Steps

1. Build the image:
```bash
docker build -t node-app:v1 .
```

2. Run the container:
```bash
docker run -d -p 3000:3000 --name my-node-app node-app:v1
```

3. Test the API:
```bash
curl http://localhost:3000
curl http://localhost:3000/health
```

## Challenge

Add a `/memory` endpoint that returns memory usage information using `os.freemem()` and `os.totalmem()`.
