# Docker To-Do App (learning project)

## Build and run with plain Docker
    docker build -t todo-app .
    docker run -d -p 5000:5000 --name todo todo-app

## Or with Docker Compose
    docker compose up --build

## Test it
    curl http://localhost:5000/
    curl -X POST http://localhost:5000/todos -H "Content-Type: application/json" -d '{"title": "Learn Docker"}'
    curl http://localhost:5000/todos
    curl -X DELETE http://localhost:5000/todos/1

## Useful Docker commands
    docker ps                 # running containers
    docker logs todo          # view logs
    docker exec -it todo sh   # shell inside the container
    docker stop todo && docker rm todo
    docker images             # list images
