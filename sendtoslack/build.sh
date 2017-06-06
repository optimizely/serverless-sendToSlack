#!/bin/bash -e

IMAGE=amazonlinux:latest
CONTAINER=sendtoslack_builder

# Run a docker container to use during builds of this project
if [[ "$(docker inspect -f '{{.State.Running}}' $CONTAINER)" = "false" ]]; then
  docker start $CONTAINER > /dev/null
else
  docker run --name $CONTAINER --tty --detach --workdir /build --volume $(pwd):/build $IMAGE /bin/cat > /dev/null
fi

shopt -s expand_aliases
alias RUN="docker exec --tty $CONTAINER"

# Install build dependencies into the docker container
RUN yum install -y \
      python27-devel \
      python27-setuptools
RUN easy_install pip

# Install runtime dependencies onto the mounted filesystem path
RUN mkdir -p vendored/
RUN pip install -t vendored/ -U -r requirements.txt

# Stop the container, but leave it around for reuse
docker stop $CONTAINER > /dev/null
