# Vacations itinerary

The objective of the project is the creation of an application allowing to propose a route according to certain criteria.

## Description

The user of the application chooses areas / places and the duration of the stay and the app proposes a detailed itinerary optimizing his travel and stay time.

## Getting Started

### Dependencies

* Python3.8
* SQL: SQLAlchemy
* MongoDB: pymongo
* Neo4j
* 

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
* Run the built container
```bash
docker run --name itinerary -p 5000:5001
```
#### From source
* Run using python
```bash
python -m main.y
```

## Documentation

Detailed documentation
* Phase 1 
    * fr: [Etape 1](/doc/fr/etape1.md)
    * en: ...
* Phase 2
    * fr: [Etape 2](/doc/fr/)
    * en: ...

## Authors

Contributors names and contact info

* Laeticia Malingre
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
