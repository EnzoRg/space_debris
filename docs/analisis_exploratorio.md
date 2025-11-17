# 2. Análisis Exploratorio y Curación de Datos

La segunda parte estará enfocada en realizar un análisis más profundo de los datos en los distintos archivos con el objetivo de saber entender y explicar los datos con los que estan trabajando. Se busca poder identificar valores faltantes, duplicados o inconsistentes y se definirán estrategias para su tratamiento.

Se evaluará si todas las variables son relevantes para los objetivos del proyecto, o si algunas pueden descartarse para luego crear un **unico dataset**. También se explorará la generación de nuevas variables que aporten mayor valor. Asimismo, se buscará detectar valores atípicos y analizar si son errores o fenómenos significativos que deben conservarse. Se sugiere utilizar complementos que ayuden al analisis de datos como [Ydata-profiling](https://docs.profiling.ydata.ai/latest/getting-started/quickstart/) o [Sweetviz](https://pypi.org/project/sweetviz/).

Sugerencias para el análisis:
- El tipo de dato a utilizar (o convertir) en las variables `int`, `float`, `datetime`, etc.
- ¿Es `.json` la mejor forma de guardar los datos?
- Segun los datos ¿Conviene usar `StandardScaler`, `MinMaxScaler` u otro método para escalar?
-  ¿Cuando utilizar `OneHotEncoder`, `OrdinalEncoder` y/o `LabelEncoder` para las variables categoricas? 
- Elegir y comparar el mejor metodo de imputacion según los datos faltantes.
- Determinar como van a separar los datos en *entrenamiento*, *evaluacion* y *test*.
- **Comparar los datos antes y despues de realizar EDA**.


Se sugiere utilizar las siguientes categorias para agrupor los satelites según su propósito: 
1. Communications:
    - Communications
    - Navigation/Global Positioning
    - Surveillance
    - Communications/Maritime Tracking
    - Communications/Technology Development 
    - Communications/Navigation
    - Satellite Positioning

2. Earth Observation:
    - Earth Observation
    - Earth Science
    - Earth Observation/Navigation
    - Earth/Space Observation
    - Earth Observation/Communications
    - Earth Observation/Communications/Space Science
    - Earth Science/Earth Observation 
    - Earth Observation/Space Science
    - Earth Observation/Earth Science   

3. Technology Development:
    - Technology Development
    - Space Science
    - Technology Demonstration
    - Unknown
    - Space Observation 
    - Earth Observation/Technology Development 
     - Meteorological
    - Mission Extension Technology
    - Technology Development/Educational   
    - Space Science/Technology Development
    - Educational
    - Platform
    - Space Science/Technology Demonstration

Lectura recomendada:
- [Dataset transformations](https://scikit-learn.org/stable/data_transforms.html)
- [Encoding categorical features](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features)
- [IO tools (text, CSV, HDF5, …)](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)


##
<p align="right">Siguiente | <b><a href="aprendizaje.md">Aprendizaje Supervisado y/o No Supervisado</a></b>
<br/>
Atrás | <b><a href="analisis_y_visualizacion.md">Análisis y Visualización</a></p>

</b><p align="center"><sup> EnzoRg | </sup><a href="../README.md"><sup>Contenidos</sup></a></p>