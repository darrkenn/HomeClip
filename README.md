# What is HomeClip?
Homeclip is a performant, self-hosted link manager that lets you create links and organise them with folders.

## Requirements
**Docker** is required to run HomeClip.
Install it via your package manager or follow a guide [here](https://docs.docker.com/engine/install/)

## Setup
1. Clone repo:
```bash
git clone https://github.com/darrkenn/HomeClip
cd HomeClip
```
2. Change database location:
```yaml
      - type: bind
        source: /var/lib/homeclip/ #Destination of database file.
        target: /app/db/
```
3. Build container:
```bash
docker compose build
```
4. Run container:
```bash
docker compose up -d
```
5. Open browser and visit http://localhost:3119/


![HackaTime Badge](https://hackatime-badge.hackclub.com/U092R8UPA6L/HomeClip)

