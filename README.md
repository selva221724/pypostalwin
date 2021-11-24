# pypostalwin 

[<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green">](https://opensource.org/licenses/MIT)

pypostalwin is the Un-Official Python wrapper to [libpostal](https://github.com/openvenues/libpostal), a fast statistical parser/normalizer for street addresses anywhere in the world.

<!---[<img src="https://img.shields.io/pypi/v/edaSQL">](https://pypi.org/project/edaSQL/)
[<img src="https://img.shields.io/readthedocs/edasql">](https://edasql.readthedocs.io/en/latest/)
<img src="https://img.shields.io/pypi/wheel/edaSQL">
<img src = "https://img.shields.io/pypi/pyversions/edaSQL">
<img src = "https://img.shields.io/github/commit-activity/w/selva221724/edaSQL">
<img src = "https://img.shields.io/github/languages/code-size/selva221724/edaSQL">--->

## About libpostal
libpostal is a C library for parsing/normalizing street addresses around the world using statistical NLP and open data. The goal of this project is to understand location-based strings in every language, everywhere.

## Installation

### 1. Build the libpostal in windows
Before usign the Python wrapper, you need to build the libpostal C library as a bundle which can be accessed by the python package. 

[Please follow the Instructions given in the Repository](https://pypi.org/project/pypostalwin/)

### 2 . Install the python wrapper 
**Install using pip** . [Offical Python Package Here!!](https://pypi.org/project/pypostalwin/)
```shell
pip install pypostalwin
```

(OR)

Clone this Repository. Run this from the root directory to install

```shell
python setup.py install
```

## Usage

### Import Package
```python
import pypostalwin
```

### 1. Initialize Address Parser Object
```python
parser = pypostalwin.AddressParser()
parsedAddress = parser.runParser("The White House 1600 Pennsylvania Avenue NW, Washington, DC 20500, USA")
print(parsedAddress)
```
```sh
{'house': 'the white house',
 'house_number': '1600',
 'road': 'pennsylvania avenue nw',
 'city': 'washington',
 'state': 'dc',
 'postcode': '20500',
 'country': 'usa'}
```

### 2. Terminate Address Parser Object
```python
parser.terminateParser()
```

