<p align="center">
  <img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/sql_logo_smaller.png" width="70%" height="70%" >
  <br><br>
</p>

[<img src="https://img.shields.io/pypi/v/edaSQL">](https://pypi.org/project/edaSQL/)
[<img src="https://img.shields.io/readthedocs/edasql">](https://edasql.readthedocs.io/en/latest/)
[<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green">](https://opensource.org/licenses/MIT)
<img src="https://img.shields.io/pypi/wheel/edaSQL">
<img src = "https://img.shields.io/pypi/pyversions/edaSQL">
<img src = "https://img.shields.io/github/commit-activity/w/selva221724/edaSQL">
<img src = "https://img.shields.io/github/languages/code-size/selva221724/edaSQL">

## SQL Bridge Tool to Exploratory Data Analysis  


**edaSQL** is a library to link SQL to **Exploratory Data Analysis** and further more in the Data Engineering. This will solve many limitations in the SQL studios available in the market. Use the SQL Query language to get your Table Results. 

## Installation
Install dependency Packages before installing edaSQL
```shell
pip install pyodbc
pip install ipython
```
Optional dependency for better visualization - [Jupyter Notebook](https://jupyter.org/install) 
```shell
pip install notebook
```

**Now Install using pip** . [Offical Python Package Here!!](https://pypi.org/project/edaSQL/)
```shell
pip install edaSQL
```

(OR)

Clone this Repository. Run this from the root directory to install

```shell
python setup.py install
```

## Documentation

<img src="https://blog.readthedocs.com/_static/logo-opengraph.png"  width="20%" height="20%">

[Read the detailed documentation in readthedocs.io](https://edasql.readthedocs.io/en/latest/)


## edaSQL Jupyter NoteBook Tutorial

### Import Packages
```python
import edaSQL
import pandas as pd
```

### 1. Connect to the DataBase
```python
edasql = edaSQL.SQL()
edasql.connectToDataBase(server='your server name', 
                         database='your database', 
                         user='username', 
                         password='password',
                         sqlDriver='ODBC Driver 17 for SQL Server')
```

<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/db_connected.png">

### 2. Query Data 
```python
sampleQuery = "select  * from INX"
data = pd.read_sql(sampleQuery, edasql.dbConnection)
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/data_sample.png">

### 3. Data Overview
```python
insights =  edaSQL.EDA(dataFrame=data,HTMLDisplay=True)
dataInsights =insights.dataInsights()
```

<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/1.png">

```python
deepInsights = insights.deepInsights()
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/2.png">

### 4. Correlation
```python
eda = edaSQL.EDA(dataFrame=data)
eda.pearsonCorrelation()
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/3.png">

```python
eda.spearmanCorrelation()
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/4.png">

```python
eda.kendallCorrelation()
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/5.png">

### 5. Missing Values

```python
eda.missingValuesPlot(plot ='matrix')
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/6.png">

```python
eda.missingValuesPlot(plot ='bar')
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/7.png">

```python
eda.missingValuesPlot(plot ='heatmap')
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/8.png">

```python
eda.missingValuesPlot(plot ='dendrogram')
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/9.png">

### 6. Outliers 

```python
eda.outliersVisualization(plot = 'box')
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/10.png">

```python
eda.outliersVisualization(plot = 'scatter')
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/11.png">

```python
outliers = eda.getOutliers()
```
<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/12.png">
