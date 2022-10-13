# ThompsonBot
Coding Cartel bot that enables us to manage discord.

## Installation

### Bare-metal
To run, this bot requires python modules to be installed. This task
is partially managed by a requirements.txt file.
To install required modules, use ```pip install -r requirements.txt``` inside a command prompt.

### Docker

To run ThompsonBot in a docker container :
1) Go to the root directory of the project
2) Build the image
> docker build . -t thompsonbot
3) Run the image
> docker run --name thompson -d thompsonbot

