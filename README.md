# ThompsonBot
Coding Cartel bot that enables us to manage discord.

# Install & Run

## Bare-metal
In order to run, this bot requires python modules to be installed. This task is managed by a requirements.txt file.
To install required modules, go to your terminal an run: 
```
pip install -r requirements.txt
```

Then, being at the root of the project, run:
```
python3 main.py
```

## Container

To run ThompsonBot in a container :
1) Go to the root directory of the project
2) Build the image
3) Run the image

### Docker
```
docker build -t thompsonbot .
docker run --name thompson -d thompsonbot
```

### Podman
```
podman build -t thompsonbot .
podman run --name thompson -d thompsonbot
```