#!/usr/bin/env python3

import argparse
import docker

def main(args):

    tag = args.name + ":Dockerfile"
    client = docker.from_env()

    if args.stop:
        print("Stopping container")
        containers = client.containers.list()
        for container in containers:
            if tag in container.image.tags:
                container.stop()
                break
        print("Finished stopping container")
    else:
        if args.build:
            print("Building container")
            client = docker.from_env()
            client.images.build(
                path="./" + args.name + "/", tag=tag
            )
            print("Finished building container")

        print("Starting container")
        mount = docker.types.Mount(
            target="/root/app/foundry/foundrydata",
            source="foundrydata"
        )

        container = client.containers.run(
            tag,
            detach=True,
            mounts=[mount]
        )


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', action='store_true', help='Builds docker file before running', default=False)
    parser.add_argument('--stop', action='store_true', help='Stop docker image', default=False)
    parser.add_argument('--name', type=str, default="foundry", choices=['foundry'], help='Choose container to control')

    main(parser.parse_args())
