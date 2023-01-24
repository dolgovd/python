Here is an example how a great development environment can be established with help of Docker

1. Build an image with required dependencies
```Dockerfile
docker build -t fastapi-image .
```
2. Start a container and mount a volume with our codebase
```Dockerfile
docker run --rm --name fastapi-container -p 80:80 -d -v $(pwd):/code fastapi-image
```
3. Install two extention for VSCODE
- Dev Containers
- Python
4. Open a remote window (button in left-bottom corner)
5. Select "Attach to Running Container ..."
6. Select the container started on step #2