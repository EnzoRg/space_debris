# 2. Análisis Exploratorio y Curación de Datos

La segunda parte, estará enfocada en realizar un análisis profundo de la calidad de los datos en los distintos archivos con el objetivo de saber entender y explicar los datos con los que estan trabajando. Se busca poder identificar valores faltantes, duplicados o inconsistentes y se definirán estrategias para su tratamiento.

Se sugiere utilizar complementos que ayuden al analisis de datos como [Ydata-profiling](https://docs.profiling.ydata.ai/latest/getting-started/quickstart/) o [Sweetviz](https://pypi.org/project/sweetviz/)

Se evaluará si todas las variables son relevantes para los objetivos del proyecto, o si algunas pueden descartarse para luego crear un **unico dataset**. También se explorará la generación de nuevas variables que aporten mayor valor predictivo.

Asimismo, se buscará detectar valores atípicos y analizar si son errores o fenómenos significativos que deben conservarse. 

Sugerencias para el análisis:
- Determinar como separar los datos en *entrenamiento*, *evaluacion* y *test*
- El tipo de dato a utilizar (o convertir) en las variables (int, float, datetime)
- ¿Con que extension guardaran los dataframes
- Segun los datos ¿Conviene usar `StandardScaler`, `MinMaxScaler` y otro método para escalar?
- ¿Que tipo de encoder utilizar? 
- Determinar el metodo de imputacion para los datos faltantes

Es recomendable leer la documentacion de Scikit-Learn relacionada a [Dataset transformations](https://scikit-learn.org/stable/data_transforms.html)

| Communications                                | Earth Observation                                | Technology Development                      |
|-----------------------------------------------|--------------------------------------------------|--------------------------------------------|
| Communications                                | Earth Observation                                | Technology Development                      |
| Navigation/Global Positioning                 | Earth Science                                    | Space Science                               |
| Surveillance                                  | Earth Observation/Navigation                    | Technology Demonstration                    |
| Communications/Maritime Tracking              | Earth/Space Observation                          | Unknown                                     |
| Communications/Technology Development         | Earth Observation/Communications                 | Space Observation                           |
| Communications/Navigation                     | Earth Observation/Communications/Space Science   | Earth Observation/Technology Development    |
| Satellite Positioning                         | Earth Science/Earth Observation                  | Meteorological                              |
|                                               | Earth Observation/Space Science                  | Mission Extension Technology                |
|                                               | Earth Observation/Earth Science                  | Technology Development/Educational          |
|                                               |                                                  | Space Science/Technology Development        |
|                                               |                                                  | Educational                                 |
|                                               |                                                  | Platform                                    |
|                                               |                                                  | Space Science/Technology Demonstration      |


##
<p align="right">Siguiente | <b><a href="aprendizaje.md">Aprendizaje Supervisado y/o No Supervisado</a></b>
<br/>

Atrás | <b><a href="analisis_y_visualizacion.md">Análisis y Visualización</a></p>

</b><p align="center"><sup> EnzoRg | </sup><a href="../README.md"><sup>Contenidos</sup></a></p>