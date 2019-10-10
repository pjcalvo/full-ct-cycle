<img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Twelve_Labours_Altemps_Inv8642.jpg" height="300px"/>

# Heracles: Pleo's Test Engineer Challenge - Pablo's Work

[![CircleCI](https://circleci.com/gh/pjcalvo/heracles/tree/master.svg?style=svg)](https://circleci.com/gh/pjcalvo/heracles/tree/master)

## The challenge: Money Formatting

Given an amount of money as a number, format it as a string. Add associated tests for the functionality and for the user interface. 

```js
formatMoney(2310000.159897); // '2 310 000.16'
formatMoney(1600); // '1 600.00'
```

## This is what i did:
* First I added a backend small project using Python Flask.
* I added CI support with CircleCI in order to run the tests
* I added some unit tests for the "core" functionality which actually make find a problem with negatives
*

## Setting up the environment:
In order to be able to run and test the project you will first need easy setup:

### Python3
It is used to run and test the API as well as to run the front end app.

* If you are in a mac simple: `brew install python3`
* If not or you don't have brew installed follow this (Python3)[https://www.python.org/downloads/]

### NodeJs
It is used to execute the UI tests (WebDriverIO)

* If you are in a mac simple: `brew install nodeJs`
* If you are in a mac simple: `brew install npm`
* If not or you don't have brew installed follow this (NodeJs)[https://docs.npmjs.com/downloading-and-installing-node-js-and-npm]

## Setting up the project
Once we have the environment ready we need to install the project dependecies:
*Here I am assumming you cloned the repo already if not: `git clone https://github.com/pjcalvo/heracles`

Python recommends you to use a virtual env when installing dependecies to avoid conflict with OS libraries
`python3 -m venv venv` create the virtual env
`. venv/bin/activate` source to the virtual env, you will see (venv) in the terminal
`pip install -r requirements.txt` install project dependencies

NodeJs doesn't need a virtual env because the libraries are installed inside the node_modules project
`npm install`

Selenium will be the webdriver to connect to the browser and execute UI tests:
* (Recommended) Uncomment this line `// services: ['selenium-standalone'],` on the `wdio.conf.js` file which will make selenium start for you seemlesly.
* If you want to download and spin selenium on your own do `sh selenium.sh`. It is a small script that downloads and spins selenium.

## Spinning up the webapp and api:
I decided to split the frontend and backend in two separate projects to have a more real life context of isolation between these two.
This means that you will need to run them separately in order to work.

### Backend
The backend is located under src/api
Open a new terminal
In order to spin the backend just run: `FLASK_APP=src/api/app.py flask run`
Check the (app)[http://localhost:5000]

### WebAPP
The frontend is located under src/web
Open another new terminal 
In order to spin the frontend just run: `FLASK_RUN_PORT=5001 FLASK_APP=src/api/app.py flask run`
In this case we need to indicate a different port for the server to avoid conflict with the backend
Check the (app)[http://localhost:5001]


## Running tests
This solution contains 3 levels of testing:
### Unit testing

Happy reviewwing! 🚀
