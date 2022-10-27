# IT 326 Tutor web app
### Project Setup
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


### Environment setup
Because of Docker, it's possible to write this code without installing any packages from pip or npm/yarn,
but I wouldn't reccomend it. 

So here's a tutorial to setting up your dev environment to be pretty similar to what I (Jared) have going
on. I'm going to be assuming you're using VSCode and Windows, but if you need help setting it up with another IDE/OS I'm more than willing to be of assistance.

#### Necessities
There's a few things we'll need to install before doing anything with Python or JS/TS.
Latest Python(duh): https://www.python.org/downloads/windows/
Latest NodeJS: https://nodejs.org/en/download/

Install both of these and restart your machine.

#### Package managers
##### Yarn
Yarn is the package manager we're using for the frontend subproject. It is an alternative to the npm package manager that I prefer using. Simpler commands and is faster in my experience.

Once logged in, open up your terminal of choice. You may need to open up the terminal as an Administrator depending on your setup.
```
npm install -g yarn
cd {your project directory}/it326-tutoring-app/frontend
yarn install
```
This will install the npm packages for the frontend subproject using a package manager called Yarn.

##### Pip(take a look at pipenv section first)
Pip is the default package manager for Python, it is installed alongside the Python interpreter and is okay to use on its own.

```
cd {your project directory}/it326-tutoring-app/backend
pip install -r ./requirements.txt
```
This will install the packages in the requirements.txt file.

##### Pipenv(not mandatory, but helpful)
Pip modules installed without a virtual environment are installed globally. This isn't ideal if working on multiple projects with different packages for two reasons(that I know of).
1. Pollutes IDE suggestions and hints with unnecessary or undesireable packages.
2. Forces you to manually create requirements.txt files since all the packages for a project are lumped together.

Pipenv is by far the most convenient solution to this problem that I've found (venv is cumbersome to use and conda might as well be malware)
Its installation process is simple.
```
pip install --user pipx
pipx install pipenv
```
From there it's simple to use.
```
cd {your project directory}/it326-tutoring-app
pipenv install //to install the pip modules stored in the
pipenv shell //opens your terminal with the virtual environment(not necessary unless you're running backend outside of docker)
```



#### Extensions
Oo boy do I have a list of extensions for you.
I'll rate them on a scale of 1 to 5 based on their necessity/helpfulness.

##### Backend
Python Extension Pack (5): https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack
Pylance (3): https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
Python Type Hint (4): https://marketplace.visualstudio.com/items?itemName=njqdev.vscode-python-typehint

##### Frontend
JS and TS Nightly (2): https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next
Move TS (2): https://marketplace.visualstudio.com/items?itemName=stringham.move-ts
##### Misc.
Git Graph (4): https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph
Live Share (? we'll see how much it's needed): https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack
Path Intellisense (1): https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense
Better Comments (3): https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments



