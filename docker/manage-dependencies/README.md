# Purpose
This demonstrates how to package dependencies in a Docker container. The source code using the dependencies are mounted to the container. By mounting, we prevent rebuilding the container every time the source code changes.

# To Run
```
docker build \
    --tag manage-dependencies-img \
    --file Dockerfile \
    .

docker run \
    --interactive \
    --tty \
    --rm \
    --name manage-dependencies \
    --volume `pwd`/manage-dependencies:/opt/manage-dependencies \
    manage-dependencies-img
```
