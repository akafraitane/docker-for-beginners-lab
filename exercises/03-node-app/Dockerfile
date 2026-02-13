# Use official Node.js LTS image
FROM node:20-alpine

# Create app directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy application source
COPY server.js .

# Expose port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
