# Exercise 01: My Website

Build your first Docker image - a simple static website served by Nginx.

## Steps

1. Build the image:
```bash
docker build -t my-website:v1 .
```

2. Run the container:
```bash
docker run -d -p 8080:80 --name my-website-container my-website:v1
```

3. Open http://localhost:8080 in your browser

4. Stop and remove when done:
```bash
docker stop my-website-container
docker rm my-website-container
```

## Challenge

Modify the `index.html` file and rebuild the image to see your changes!
