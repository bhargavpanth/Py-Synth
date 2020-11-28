# PySynth

> PySynth is a python based synthetic testing framework. Underneath, PySynth uses Selenium to spin up headless or UI based browser (webkit and gecko support available). To invoke an instance of the browser window pass in the `-g` or `-gui` flag along with `-c` or `-chrome` for Chrome, or `-f` or `-firefox` for Firefox

## How to get started
Requirements
* Python3
* Docker

Get started
* `$ git clone https://github.com/bhargavpanth/Py-Synth.git`
* Run `docker-compose up`
* Install the requirements from `requirements.txt`
* Add an episode in the `./episodes` folder

## How to define an episode
Every episode consists of the following properties `title` `seed_url` `steps`. `steps` in turn is an array of objects where each object consists of `name`, `operation`, `DOM_element`.

`name` accepts a string property
`operation` accepts one of `click` or `input`
