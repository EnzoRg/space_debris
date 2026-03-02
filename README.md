# Propuesta de Proyecto de Mentoría - DiploDatos 2026 

# 🛰🌎 **Predicciones en el Espacio: ¿Cuántos satélites y desechos podremos tener?**  

<img src="data/images/cover_image.png" alt="Portada desechos espaciales" width="500"/>  

## 📌 Descripción y objetivos del proyecto  
En la última década, el número de satélites en órbita ha crecido exponencialmente debido a los avances tecnológicos, la reducción de costos de lanzamiento y el surgimiento del paradigma [New Space](https://www.earthdata.nasa.gov/s3fs-public/2023-11/newspace_nasa.pdf). Este modelo promueve ciclos de desarrollo más cortos, plataformas más pequeñas y reemplazos frecuentes.

En febrero de 2026, había aproximadamente [14.000 satélites activos en órbita](https://celestrak.org/NORAD/elements/table.php?GROUP=active&FORMAT=tle). Además, diversos estudios estiman que [más de un millon de proyectos satelitales han sido propuestos y se encuentran en diversas etapas de desarrollo](https://outerspaceinstitute.ca/osisite/wp-content/uploads/Onemillionpapersatellites-AcceptedVersion.pdf).

Un fenómeno particularmente relevante es el despligue de grandes constelaciones, impulsados por la comercialización global del servicio ofrecido. Esta expansión intensifica la ocupación de determinadas orbitas y plantea un escenario de [creciente competencia](https://www.adslzone.net/noticias/internet/amazon-leo-competencia-starlink-tiendas-fisicas/).

Sin embargo, hay un problema que vino de la mano y que hasta hace poco tiempo no era considerado importante: [los desechos espaciales](https://www.argentina.gob.ar/sinagir/riesgos-frecuentes/chatarra-espacial). Estos desechos van desde satélites fuera de servicio hasta naves espaciales abandonadas y restos de misiones fallidas. Según la [NASA](https://svs.gsfc.nasa.gov/5258/) y [ESA](https://sdup.esoc.esa.int/discosweb/statistics/), actualmente hay más de 30.000 objetos rastreados en órbita, y tambien se lleva un [registro](https://spacesecurity.wse.jhu.edu/space-collisions/) de las colisiones a lo largo del tiempo. Se pronostica que, con el paso del tiempo, las dificultades se irán multiplicando. Es por esto que se necesita lograr dar una solución efectiva al asunto.

**El objetivo de este proyecto es predecir la vida útil real de un satélite antes de que quede fuera de servicio, con el fin de mejorar la comprensión y el control del entorno espacial. El modelado se llevará a cabo mediante técnicas de Aprendizaje Supervisado y/o No Supervisado.**

La propuesta busca analizar y correlacionar un conjunto de datos históricos que incluyen información sobre lanzamientos, satélites fuera de servicio, masa, tamaño, órbita, período orbital, tipo de misión y vida útil nominal, entre otras variables, para comprender su impacto en la cantidad total de objetos en órbita, tanto operativos como inactivos o fragmentados.

El proyecto busca responder las siguientes preguntas:  

- **¿Cómo ha evolucionado la cantidad de satélites y desechos espaciales en los últimos años?**  
- **¿Cuál es la vida útil real de un satélite y cómo difiere de la vida útil nominal?**  
- **¿Existen patrones en la distribución de basura espacial en diferentes órbitas?**  
- **¿Qué países u organizaciones generan más desechos en el espacio?**  
- **¿Podemos predecir la cantidad de desechos espaciales en los próximos años?**  
- **¿Cuál es la tendencia en el tamaño y características de los nuevos objetos que orbitan la Tierra?**

## 🗃 Datos  

El dataset propuesto `satellites_202602.csv` contiene datos actualizados hasta febrero del 2026 y está conformado por:

- Registro histórico de misiones exitosas, obtenido de [Space-Track.org](https://www.space-track.org/).
- Datos de satélites activos orbitando la Tierra, obtenidos de [CelesTrack](https://celestrak.org/).
- Propósito de la misión obtenido de [UCS Satellite Database](https://www.ucs.org/resources/satellite-database), actualizado y corregido con criterio propio. 

## 💻 Desarrollo 

El desarrollo de este proyecto se divide de la siguiente manera: 

- [Introducción a los Satélites](docs/intro_satelites.md)
- [Descripción de los Datos](docs/dataset.md)
- [Análisis y Visualización](docs/analisis_y_visualizacion.md)
- [Análisis Exploratorio y Curación de Datos](docs/analisis_exploratorio.md)
- [Aprendizaje Supervisado y/o No Supervisado](docs/aprendizaje.md)
- [Resultados y Conclusiones](docs/resultados.md)

## 📚 Referencias
- [Space-Track API](https://www.space-track.org/documentation#/api)
- [CelesTrack: Active Satellites](https://celestrak.org/NORAD/elements/table.php?GROUP=active&FORMAT=tle)
- [Union of Concerned Scientists - Satellite Database](https://www.ucs.org/resources/satellite-database)
- [ISS Tracker](https://isstracker.pl/en)
- [How many satellites can we safely fit in Earth orbit?](https://www.n2yo.com/satellite-article/How-many-satellites-can-we-safely-fit-in-Earth-orbit/86)
- [Too many satellites? Earth's orbit is on track for a catastrophe - but we can stop it](https://phys.org/news/2026-02-satellites-earth-orbit-track-catastrophe.html)
- [Satellite megaconstellations continue to grow. Could their debris fall on us?](https://www.space.com/space-exploration/satellites/satellite-megaconstellations-continue-to-grow-could-their-debris-fall-on-us)
- [Jonathan's Space Pages Satellite statistics: Satellite and Debris Population](https://planet4589.org/space/stats/active.html)
- Kessler, D. J. (1991). Collisional cascading: The limits of population growth in low Earth orbit. Advances in Space Research, 11(12), 63–66


</b><p align="center"><sup> EnzoRg | </sup><a href="/README.md"><sup>Contenidos</sup></a></p>