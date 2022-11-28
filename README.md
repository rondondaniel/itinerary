# Vacations itinerary

The objective of the project is the creation of an application able to suggest a route according to certain criteria.

## Description

The user of the application chooses areas / places and the duration of the stay and the app suggests a detailed itinerary optimizing his travel and stay time.

## Getting Started

### Dependencies

* Python3.8
* MongoDB: pymongo 

### Installing

#### Docker
* Clone this repository
```bash
git clone git@github.com:rondondaniel/itinerary.git
```
* Build docker container using the edockerfile
```bash
docker build -t project/itinerary .
```

#### From source
* Clone this repository
```bash
git clone git@github.com:rondondaniel/itinerary.git
```
* Install requirements
```bash
python -m pip install requirements.txt
```

### Executing program

#### Docker
* Create a .env file at root of the project

* Run docker-compose file
```bash
docker-compose up -d
```
#### From source
* Run using python
```bash
python -m main.y
```

## Detailed documentation

* [Stage 1: Collecting data](/doc/etape1.md)
* [Stage 2: Data architecture](/doc/etape2.md)
* [Stage 3: Data consumption](/doc/etape3.md)
* [Stage 4: Automation of data flow](/doc/etape4.md)

## Authors

Contributors names and contact info

* Laeticia Malingre *laeticia.malingre@gmail.com*
* Marylis Rubrice
* Daniel Rondon - *rondondaniel@gmail.com*

## Version History

* 0.3 ...
* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, source data, etc.

* [Datascientest](https://wwww.datascientest.com)
* [Citymapper](https://www.citymapper.com)
* [DataTourisme](https://www.datatourisme.fr/)
* ...
