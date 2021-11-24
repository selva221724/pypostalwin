# pypostalwin 


[<img src="https://img.shields.io/pypi/v/pypostalwin">](https://pypi.org/project/pypostalwin/)
[<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green">](https://opensource.org/licenses/MIT)
<img src="https://img.shields.io/pypi/wheel/pypostalwin">
<img src = "https://img.shields.io/pypi/pyversions/pypostalwin">
<img src = "https://img.shields.io/github/commit-activity/w/selva221724/pypostalwin">
<img src = "https://img.shields.io/github/languages/code-size/selva221724/pypostalwin">

pypostalwin is the Un-Official Python wrapper to [libpostal](https://github.com/openvenues/libpostal) only for Windows, a fast statistical parser/normalizer for street addresses anywhere in the world.


## About libpostal
libpostal is a C library for parsing/normalizing street addresses around the world using statistical NLP and open data. The goal of this project is to understand location-based strings in every language, everywhere.

## Installation

### 1. Build the libpostal in windows
- Before usign the Python wrapper, you need to build the libpostal C library as a bundle which can be accessed by the python package. (still under development) 

(OR)

- You can use the prebuild bundle zipped file [Download here](https://drive.google.com/file/d/1fZUlyLFCGYD7l_PDM0NzD8pAo-ICrVVd/view?usp=sharing)  
- Unpack the zip to C:\Workbench\libpostal\
- If you dont have **Workbench** folder in C Drive, then create one. 
- Copy the zip inside the **Workbench** and unzip using [7zip](https://www.7-zip.org/download.html) 

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
output
```sh
[
  {'house': 'the white house'}, 
  {'house_number': '1600'},
  {'road': 'pennsylvania avenue nw'}, 
  {'city': 'washington'}, 
  {'state': 'dc'}, 
  {'postcode': '20500'}, 
  {'country': 'usa'}
]

```
**Note:** In a single runtime, the first-time parser.runParser() will take a few seconds to run since it is loading the models from libpostal in the backend process. Once it is loaded, the recurrent runs will be faster as usual. You need to use the same object instance to get the results faster.

for eg:

```python
parser = pypostalwin.AddressParser()
parsedAddress1 = parser.runParser("The White House 1600") #only first time will take few seconds to load
parsedAddress2 = parser.runParser("Washington, DC 20500, USA") #will be faster as usual
parsedAddress3 = parser.runParser(" 20500, USA") #will be faster as usual
parsedAddress4 = parser.runParser("Pennsylvania Avenue NW, Washington,") #will be faster as usual
```

### 2. Terminate Address Parser Object
```python
parser.terminateParser()
```

