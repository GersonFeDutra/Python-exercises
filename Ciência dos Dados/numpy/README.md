# Instructions

After running the container with `docker compose up`:

```bash
# Attach to the environment:

# Enter the container with bash
docker exec -it anaconda-dev /bin/bash

# List the running sessions
jupyter server list

# Copy the token provided after:
?token=<token>
# to attach the interpreter in VsCode as
http://localhost:8888/?token=<token>

# Or load Jupyter lab in the browser at <http://localhost:8888/>.
```
