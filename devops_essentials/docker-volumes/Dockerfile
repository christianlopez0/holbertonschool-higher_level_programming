# Use the Alpine base image
FROM alpine

# Install curl package
RUN apk add --no-cache curl

# Copy config.txt to /app/config.txt in the container
COPY config.txt /app/config.txt

# Set up a volume for data persistence
VOLUME /data