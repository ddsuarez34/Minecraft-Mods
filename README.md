# Minecraft-Mods

## Modpacks (Server & Client)

We are using packwiz MC mod manager. Helps with creating, downloading and distributing a modpack.

- [Guide](https://packwiz.infra.link/tutorials/creating/getting-started/)

- When pushed, .packwiz file is served at https://ddsuarez34.github.io/Minecraft-Mods/modpack/pack.toml.

## Local Development / Deployment

- Install docker
- Run `cd docker` and `docker compose-up`. Make sure to open connections to ports `25565` and `24454`. Use a VPN for the players, or router settings to redirect traffic from a public IP, to your server in those ports.
