# Run instructions

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
