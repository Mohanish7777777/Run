# Navigate to the directory containing your Dockerfile
docker build -t yourusername/alpine-terminal:latest .

# Log in to Docker Hub
docker login

# Push the image to Docker Hub
docker push yourusername/alpine-terminal:latest
