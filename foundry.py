#!/usr/bin/env python3

import argparse
import docker

    
def build(client, tag):
    print("Building container")
    client = docker.from_env()
    client.images.build(
        path="./" + args.name + "/", tag=tag
    )
    print("Finished building container")

def start(client, tag):
    print("Starting container")
    volumes = {'/root/app/foundry/foundrydata': {'bind': '/foundrydata', 'mode': 'rw'}}
    ports = {"80/tcp":80}

    container = client.containers.run(
        tag,
        detach=True,
        volumes=volumes,
        ports=ports
    )

def stop(client, tag):
    print("Stopping container")
    containers = client.containers.list()
    for container in containers:
        if tag in container.image.tags:
            container.stop()
            break
    print("Finished stopping container")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', action='store_true', help='Builds docker file before running', default=False)
    parser.add_argument('--stop', action='store_true', help='Stop docker image', default=False)
    parser.add_argument('--name', type=str, default="foundry", choices=['foundry'], help='Choose container to control')

    args = parser.parse_args()
    
    tag = args.name + ":Dockerfile"
    client = docker.from_env()
    if args.stop:
        stop(client, tag)
    else:
        if args.build:
            build(client, tag)
        start(client, tag)
