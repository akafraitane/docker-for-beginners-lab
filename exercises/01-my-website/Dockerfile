# Use nginx alpine as base image (small footprint)
FROM nginx:alpine

# Add metadata labels
LABEL maintainer="your-email@example.com"
LABEL version="1.0"
LABEL description="A simple static website container"

# Copy our website files to nginx's default directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 (documentation purposes)
EXPOSE 80

# Default command (inherited from nginx image)
# CMD ["nginx", "-g", "daemon off;"]
