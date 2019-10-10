<img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Twelve_Labours_Altemps_Inv8642.jpg" height="300px"/>

# Heracles: Pleo's Test Engineer Challenge - Pablo's Work

[![CircleCI](https://circleci.com/gh/pjcalvo/heracles/tree/master.svg?style=svg)](https://circleci.com/gh/pjcalvo/heracles/tree/master)

## The challenge: Money Formatting

Given an amount of money as a number, format it as a string. Add associated tests for the functionality and for the user interface. 

```js
formatMoney(2310000.159897); // '2 310 000.16'
formatMoney(1600); // '1 600.00'
```

## My approach:
I tried to make each piece of the system as defensive as possible to avoid miss-behavios, this means that even if the backend is able to handle "special" scenarios the frontend will never send them because it is also validated.
* First I added a backend small project using Python Flask.
* I added CI support with CircleCI in order to run the tests
* I added some unit tests for the "core" functionality which actually make find a problem with negatives
* I fixed the backend problems 
* Added the API tests to add coeverage at an api acceptance level
* I added a small FrontEnd project using Python Flask as well.
* I added NodeJS to support webdriverIO to use for the e2e tests.
* I ammended everything on the README file.

###### Tech Stack
* Python3
* NodeJS
* Flask (Frontend and backend)
* Pytest (unit testing)
* Behave (bbd framework for the api testing)
* webdriverIO (e2e tests)
* CircleCI (CI/CT)

## Setting up the environment:
In order to be able to run and test the project you will first need easy setup:

###### Python3
It is used to run and test the API as well as to run the front end app.

* If you are in a mac simple: `brew install python3`
* If not or you don't have brew installed follow this [Python3](https://www.python.org/downloads/)

###### NodeJs
It is used to execute the UI tests (WebDriverIO)

* If you are in a mac simple: `brew install nodeJs`
* If you are in a mac simple: `brew install npm`
* If not or you don't have brew installed follow this [NodeJs](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

## Setting up the project
Once we have the environment ready we need to install the project dependecies:
*Here I am assumming you cloned the repo already if not: `git clone https://github.com/pjcalvo/heracles`*

**Python** recommendation is to use a virtual env when installing dependecies to avoid conflict with OS libraries
`python3 -m venv venv` create the virtual env
`. venv/bin/activate` source to the virtual env, you will see (venv) in the terminal
`pip install -r requirements.txt` install project dependencies

**NodeJs** doesn't need a virtual env because the libraries are installed inside the node_modules project
`npm install`

**Selenium** will be the webdriver to connect to the browser and execute UI tests:
* *Recommended*: Check this line `services: ['selenium-standalone'],` on the `wdio.conf.js` file. This will make selenium start for you seemlesly.
* If you want you can start selenium on your own and download the corresponding browserDrivers or use a remote selenium grid,

## Running the project
I decided to split the frontend and backend in two separate projects to have a more real life context of isolation between these two.
This means that you will need to run them separately in order to work.

###### Backend
The backend is located under *src/api*
Open a new terminal
In order to spin the backend just run: `FLASK_APP=src/api/app.py flask run`
Check the (app)[http://localhost:5000]

###### WebAPP
The frontend is located under *src/web*
Open another new terminal 
In order to spin the frontend just run: `FLASK_RUN_PORT=5001 FLASK_APP=src/api/app.py flask run`
In this case we need to indicate a different port for the server to avoid conflict with the backend
Check the (app)[http://localhost:5001]


## Running tests
This solution contains 3 levels of testing:
###### Unit testing
The unit tests make sure the acceptance criteria is met at its granular level:
```python
formatMoney(2310000.159897); // '2 310 000.16'
formatMoney(1600); // '1 600.00'
```
As this function was created on the backend the tests are also part of this project under *src/api/core/money_test.py* 

* Make sure you are in the virtual env all the time`. venv/bin/activate`
* To execute the tests simple run `pytest` which will find all the pytest methods under the folder and run them.
* Also you can use the `pytest --html=pytest-report/report.html` if you want a nice html report

###### Integration Testing
You can call these guys *integration testing* or *api acceptance testing*, or whatever seems right on the context, they are meant to test the behavior of the API given a set of specified requests. 
I feel like this guys should belong to the specific api that they are testing, in a microservice approach this will provide testability in isolation so I added the tests under *src/api/core/features/
They follow a kind of POM (Page Object Model so Controller Object Model??) design but for api requests.

In this case I decided to use [Behave](https://behave.readthedocs.io/en/latest/) which is the Cucumber version for python testing. In case the team decide to follow a BDD approach this library provides all the capabilities to do so in terms of testing.

To run the acceptance tests we need a working api, so:
* In a terminal: Move to the virtual env: `. venv/bin/activate` then spin up the backend `FLASK_APP=src/api/app.py flask run`
* In a second terminal: Move to the virtual env: `. venv/bin/activate` then run the tests `behave src/api/features/`
* No nice HTML report for this guy.

###### E2E Tests | Acceptance Tests | UI Tests
You can call these guys *e2e tests*, *acceptance tests*, *ui tests* or whatever seems right on the context, they are the last level of testing that I added, like the cherry on the cake.
I feel like this guys should belong either to the front end project or in an isolate project. In this case because there is a strong dependecy between front and backedn to be able to test the overall flow I decided to write them on a different technology and keep the project separate, so I added the tests under *src/e2e/

In this case I decided to use [WebdriverIO](https://webdriver.io/) because it is a very updated framework with tons of support for plugins and services that just make e2e testing very simple. For example it provides a nice standalone service that runs selenium in case it is not running. 

To run the acceptance tests we need a working api and a working frontend, so:
* In a terminal: Move to the virtual env: `. venv/bin/activate` then spin up the backend `FLASK_APP=src/api/app.py flask run`
* In a second terminal: Move to the virtual env: `. venv/bin/activate` then spin up the backend `FLASK_RUN_PORT=5001 FLASK_APP=src/web/app.py flask run`
* In a third terminal (no more virtual env): Just run `npm run test`

That is it for the testing.

## Continues Integration and Testing
This solution includes support for CI/CT but is not deployed anywhere.
For the CI pipeline I decided to use [CircleCI](https://circleci.com/) which is really easy to integrate with github and provides a yaml style to configure the pipeline. 

Check the configuration on *.circleci/config.yml* Also this is the current running pipeline [pjcalvo/heracles](https://circleci.com/gh/pjcalvo/heracles/)

The pipeline is structered to:

* First spin up the building environment
* Then checkout the code
* Configure the environment (setup Python, setup NodeJS, setup Selenium)
* Run the Unit Tests first (if it brokes at this level I don't want to proceed)
* Spin the apps
* Run the integration tests
* Run the UI tests
* Attach the unit tests report to the CI artifacts

Also, this runs over every commit that is done to *Master*. In a better process I will split the process differently, we need to consider a pipeline for each one of the microservices and also a different pipeline to tests UI tests on top of everything maybe after each service is deployed to Staging environment we need to identify if at this level the machine is still running.


## Notes on what I didn't do? What I would do different? What would I like to include if I had more time!?
**What I didn't do?**
I didn't consider to add any *performance or load testing*. I consider load testing as a driven context effort and in this case the context of having a single page hiting a single endpoint with no real customes is not worth the effort. Performance testing is meant to find software, infraesructure, network and db bottlenecks, but this app is not even deployed so performance testing will make not a lot on sense.

I didn't add visual UI verification because the application is just a button; but if we wanted it we could have done that using Applitools or other JS image processing library to record baselines and compare against new tests.

I didin't add any automated security testing, same as performance testing there is a big effort that needs to be invested here but no security at all on the site so i didn't think it was worth it.

**What I would do different?**
I think the number #1 thing to improve here is to have isolation between projects, which means each project should be able to be tested independently managing its own dependecies on the pipeline, and not relying on the backedn to also be spinned (in the case of the front end). This will bring a more testable and deployable environment. Each project should have it's own pipeline that builds it, test in and deploy it. And then add an extra layer of coverage for the full system integration tests once it is deployed to a testable environment.

Also, I only have a single branch which is a bad practice, in a more collaborative environment it would be nice to follow a Pull Request approach, where every PR builds and run tests and provide instant feedback before merging to master.

Also, I used flask for the frontend, but I think using a javscript framework for the front end makes more sense, this will also bring unit and component tests for the frontend layer and not just rely on the UI tests.

**What would I like to include if I had more time!?**
* More coverage for negative tests on the front end. What happens if the backend is not reachable? What happends if it is too slow?
* Better reporting and logging tools for the tests, right now it is mostly console reports, but this does not provide an easy way to debug or trobleshoot in case of errors. Including attached screenshots and logs to the execution.
* The e2e tests include a very repetitive process of enter value, submit and check result, this can be summarized on a *flows* library.


Happy reviewwing! 🚀
