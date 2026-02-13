# Exercise 04: Redis App (Container Networking)

Learn Docker networking by connecting a Flask app to Redis.

## Steps

1. Create a custom network:
```bash
docker network create app-network
```

2. Run Redis on the network:
```bash
docker run -d --name redis-db --network app-network redis:alpine
```

3. Build the Flask app:
```bash
docker build -t redis-app:v1 .
```

4. Run Flask app on the same network:
```bash
docker run -d --name flask-app --network app-network -p 5000:5000 -e REDIS_HOST=redis-db redis-app:v1
```

5. Test the app:
```bash
curl http://localhost:5000    # Visit multiple times!
curl http://localhost:5000/reset
```

## Key Concepts

- Containers on the same network can communicate using container names as hostnames
- Custom networks provide automatic DNS resolution
- No need to expose Redis port to host since only Flask needs to access it

## Challenge

Add a `/stats` endpoint that shows Redis connection info!
