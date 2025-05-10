#!/usr/bin/env python3
import docker

def ensure_image(client, name, tag="latest"):
    try:
        client.images.get(f"{name}:{tag}")
    except docker.errors.ImageNotFound:
        print(f"Pulling {name}:{tag}…")
        client.images.pull(name, tag)

def backup_volume(volume_name: str, output_path: str):
    client = docker.from_env()
    ensure_image(client, "busybox", "latest")

    container = client.containers.create(
        image="busybox:latest",
        command="true",  # no-op
        volumes={volume_name: {'bind': '/data', 'mode': 'ro'}}
    )
    try:
        stream, stat = container.get_archive('/data')
        with open(output_path, 'wb') as f:
            for chunk in stream:
                f.write(chunk)
        print(f"✅ Backup complete: {output_path}")
    finally:
        container.remove()

if __name__ == "__main__":
    backup_volume("mc_data", "mc_data_backup.tgz")
