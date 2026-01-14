
## Question 1. Understanding Docker images

Open Docker in the terminal:
```bash
open -a Docker
```

Run the image with bash as entrypoint:
```bash
docker run -it \
    --rm \
    --entrypoint=bash \
    python:3.13-slim
```
Check pip version:
```bash
pip --version

pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```

Exit the container in the terminal (and it is automaticall removed):
```bash
exit
```

### Answer: 25.3

## Question 2. Understanding Docker networking and docker-compose

### Answer: 
