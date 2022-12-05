# Vacations itinerary

The objective of the project is the creation of an application able to suggest a route according to certain criteria.

## Description

The user of the application chooses areas / places and the duration of the stay and the app suggests a detailed itinerary optimizing his travel and stay time.

## Getting Started

### Dependencies

* Python3.10
* FastAPI
* Scikit-Learn
* Open Route Service
* Dash, Dash-Leaflet
* Pandas
* Dotenv
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

#### Create a .env file at root of the project
```bash
ORS_API_KEY="YOUR_OPENROUTESERVICE_KEY_HERE"
CONNECTION_STRING="mongodb://localhost:27017/"
```

### Executing program

#### Docker
* Run docker-compose file
```bash
docker-compose up -d
```
#### From source
* Run API using uvicorn
```bash
./src/api/uvicorn main:api --reload
```
* Run Dash App using python
```bash
./src/dashapp/python main.py
```

## Detailed documentation

* [Stage 1: Collecting data](/doc/etape1.md)
* [Stage 2: Data architecture](/doc/etape2.md)
* [Stage 3: Data consumption](/doc/etape3.md)
* [Stage 4: Automation of data flow](/doc/etape4.md)

## Authors

Contributors names and contact info

* Laeticia Malingre - *laeticia.malingre@gmail.com*
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
