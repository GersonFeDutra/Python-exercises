# Run instructions

### Option 1: manually

```bash
# Deprecated: use buildx instead
docker build -t webserver-test .

# Check the sizes
docker images

# runs the server
docker run -it --rm -p 80:80 webserver-test
# Kill it with Ctrl+C

# Use:
#docker rmi <IMAGE_ID>
# to kill the created images

# or:
docker rmi webserver-test:latest

# Delete all images not being used:
docker image prune -a

docker ps -a # list containers
```

### Option 2: using Docker Compose

```bash
# Starts and runs the server in the port 80
docker-compose up

# Stops the server
docker-compose down

# You still needs to remove the image
docker image prune -a # deletes all
```
