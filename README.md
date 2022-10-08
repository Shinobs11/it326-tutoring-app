# IT 326 Tutor web app
### Setup
---
First, you'll need to download some software and install it on your machines.

Docker Desktop: https://docs.docker.com/desktop/ (You may want to go to task manager and disable this on start up(also any other junk you have enabled on start up too)) <br/>
Git: https://git-scm.com/downloads <br/>
Git Credential Manager(highly suggested): https://github.com/GitCredentialManager/git-credential-manager <br/>

After git is installed, you'll need to configure some stuff.

```
git config --global user.name *a name, doesn't have to be your real one*
git config --global user.email *an email, also doesn't have to be your real one*
git config --global core.autocrlf false  // THIS PART IS REALLY IMPORTANT FOR THIS PARTICULAR PROJECT, do this before cloning
```

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

Before we can start the containers, we need to build the containers. Depending on your machine and internet, it could take a bit. (My laptop takes around 45 seconds with ISU internet)

```
docker compose build
```
You shouldn't ever need to rebuild the containers in theory, though sometimes it can be useful for debugging when you have nothing else to try and need a bit to think after bashing your head against a keyboard for a few hours. It probably won't fix anything though.

After building your containers you can now start them!
```
docker compose up
```



All the containers are hosted on your PC and will use the localhost ip address (127.0.0.1)

NextJs(Frontend) server: 127.0.0.1:3000 or localhost:3000

Django(Backend) server: 127.0.0.1:8000 or localhost:8000

Postgres(Database) server: 127.0.0.1:5432 or localhost:5432

