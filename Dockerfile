# Dockerfile
FROM alpine:latest  # Use Alpine Linux as the base image

# Install Python, ttyd, and necessary packages
RUN apk add --no-cache python3 py3-pip ttyd bash

# Install any additional packages if needed (like curl, nano, etc.)
RUN apk add --no-cache nano curl

# Create a non-root user (recommended for security)
RUN adduser -D linuxuser

# Switch to the new user
USER linuxuser

# Set the working directory
WORKDIR /home/linuxuser

# Expose port 7681 for ttyd (you can change this if needed)
EXPOSE 7681

# Start ttyd with bash shell on container startup
CMD ["ttyd", "-p", "7681", "bash"]
