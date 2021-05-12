#!/usr/bin/env python3

import argparse
import docker

def main(args):
    print("Hello world")

    if args.build:
        print("Building container")
        client = docker.from_env()
        client.images.build(
            path="./" + args.name + "/", tag=args.name + ":Dockerfile"
        )

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', action='store_true', help='Builds docker file before running', default=False)
    parser.add_argument('--stop', action='store_true', help='Stop docker image', default=False)
    parser.add_argument('--name', type=str, default="foundry", choices=['foundry'], help='Choose container to control')

    main(parser.parse_args())
