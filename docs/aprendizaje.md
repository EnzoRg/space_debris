# Aprendizaje Supervisado y/o No Supervisado

En esta última etapa se abordará el problema desde el punto de vista del aprendizaje automático, definiendo si el objetivo principal corresponde a un problema de predicción, clasificación, regresión o agrupamiento.

Con los datos ya procesados y consolidados en un único dataset, se avanzará en el entrenamiento de modelos, comenzando con un modelo base que sirva como punto de referencia para comparar el desempeño de modelos más complejos.

Posteriormente se explorarán algoritmos más avanzados (Random Forest, Gradient Boosting, Support Vector Machines, Redes Neuronales, etc.) en función de la naturaleza del problema y de las características de los datos.

## Aspectos a considerar:

- Definir el tipo de aprendizaje:
    - Supervisado: clasificación o regresión.
    - No supervisado: clustering, reducción de dimensionalidad.

- Métricas de evaluación según el caso:
    - Clasificación: Accuracy, Precision, Recall, F1-score, ROC-AUC, Matriz de confusión.
    - Regresión: RMSE, MAE, R².
    - Clustering: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz.

- Validación y partición de datos:
    - K-Fold Cross Validation para asegurar la robustez de los modelos.
    - Train/Validation/Test split para medir el rendimiento real fuera de muestra.

- Ajuste de hiperparámetros:
    - Comparar GridSearchCV vs RandomizedSearchCV vs Bayesian Optimization para encontrar configuraciones óptimas.

- Regularización y complejidad:
    - Evitar overfitting utilizando early stopping, penalizaciones L1/L2 o pruning en árboles.

- Reducción de dimensionalidad:
    - Explorar PCA, t-SNE o UMAP para mejorar el rendimiento y la visualización de datos de alta dimensión.

- Comparación de modelos:
    - Documentar y comparar los resultados de distintos algoritmos.
    - Seleccionar el modelo final en función de la métrica más relevante para los objetivos del proyecto.

Se recomienda ver el [notebook de ejemplo](../notebooks/students_performance.ipynb) para comprender y aplicar los distintos tipos de aprendizaje.


##
<p align="right">Siguiente | <b><a href="resultados.md">Resultados y Conclusiones</a></b>
<br/>
Atrás | <b><a href="analisis_exploratorio.md">Análisis Exploratorio y Curación de Datos</a></p>

</b><p align="center"><sup> EnzoRg | </sup><a href="../README.md"><sup>Contenidos</sup></a></p>