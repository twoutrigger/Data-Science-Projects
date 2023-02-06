Common Docker Commands

Cheat sheet also available here: https://docs.docker.com/get-started/docker_cheatsheet.pdf

- docker build -t <tag name> .
    - To build an Docker image
    - Example: docker build -t testimage .

- docker run --name <container name> -p <port:port> <image name>
    - To create and run a Docker container
    - Example: docker run --name testcontainer -p 5000:5000 testimage

- docker images --all
    - To see all Docker images

- docker ps
    - To see information on running containers

- docker exec --help
    - Help menu

- docker logs --help
    - Various log options for a container

- docker rm <container name>
    - Remove a stopped container

- docker rmi <image name>
    - Remove an image

- docker login
    - Login to push and pull images from Docker Hub
