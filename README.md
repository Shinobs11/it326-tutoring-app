# IT 326 Tutor web app
### Setup
---
First, you'll need to download some software and install it on your machines.

Docker Desktop: https://docs.docker.com/desktop/
Git: https://git-scm.com/downloads
Git Credential Manager(MAYBE, idk yet): https://github.com/GitCredentialManager/git-credential-manager

Next, clone the repo (or if you REALLY don't want to use git, you can always download a zip of the repo and extract it).

```
//in your respective command line
cd /where/ever/your/work/folder/is
git clone https://github.com/Shinobs11/it326-tutoring-app
```

After cloning the repo do
```
cd ./it326-tutoring-app
```
There's two docker-compose files for setting up the containers. One is for prod, one is for dev, take a guess which is which.

Before we can start the containers, we need to build the containers.
```
docker compose -f ./docker-compose.dev.yml build
```
You shouldn't need to rebuild the containers in theory, though sometimes it can be useful for debugging when you have nothing else to try and need a bit to think after bashing your head against a keyboard for a few hours. It probably won't fix anything though.

After building your containers you can now start them!
```
docker compose -f ./docker-compose.dev.yml start
```

All the containers are hosted on your PC and will use the localhost ip address (127.0.0.1)

NextJs(Frontend) server: 127.0.0.1:3000

Django(Backend) server: 127.0.0.1:8000

Postgres(Database) server: 127.0.0.1:5432

