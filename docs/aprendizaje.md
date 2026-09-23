# Aprendizaje Supervisado y/o No Supervisado

En esta última etapa se abordará el problema desde el punto de vista del aprendizaje automático, definiendo si el objetivo principal corresponde a un problema de predicción, clasificación, regresión o agrupamiento.

Con los datos ya procesados y consolidados en un único dataset, se avanzará en el entrenamiento de modelos, comenzando con un modelo base que sirva como punto de referencia para comparar el desempeño de modelos más complejos.

Posteriormente se explorarán algoritmos más avanzados (Random Forest, Gradient Boosting, Support Vector Machines, Redes Neuronales, etc.) en función de la naturaleza del problema y de las características de los datos.

## Aspectos a considerar:

- Definir el tipo de aprendizaje:
    - Supervisado: clasificación o regresión.
    - No supervisado: clustering, reducción de dimensionalidad.

- Definir la variable objetivo y las variables de entrada:
    - Qué información está realmente disponible al momento de hacer la predicción.
    - Evitar la fuga de datos (*data leakage*): no incluir variables derivadas del objetivo ni información del conjunto de test.

- Modelo base (*baseline*):
    - Entrenar primero un modelo muy simple (por ejemplo, `DummyClassifier`, `DummyRegressor` o una regresión lineal/logística) como punto de referencia.
    - Todo modelo más complejo debe superarlo claramente.

- Métricas de evaluación según el caso:
    - Clasificación: Accuracy, Precision, Recall, F1-score, ROC-AUC, Matriz de confusión. Con clases desbalanceadas, el *accuracy* puede ser engañoso: priorizar ROC-AUC y el recall/F1 de la clase de interés.
    - Regresión: RMSE, MAE, R².
    - Clustering: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz.

- Validación y partición de datos:
    - Train/Validation/Test split: el conjunto de validación se usa para comparar modelos y ajustar hiperparámetros, y el de test se reserva únicamente para medir el rendimiento final fuera de muestra.
    - K-Fold Cross Validation (estratificado en clasificación) como alternativa al conjunto de validación, para obtener estimaciones más robustas.
    - Aplicar el preprocesamiento (escalado, imputación, etc.) ajustándolo solo con datos de entrenamiento, idealmente dentro de un `Pipeline`.

- Ajuste de hiperparámetros:
    - Comparar GridSearchCV vs RandomizedSearchCV vs Bayesian Optimization para encontrar configuraciones óptimas.

- Regularización y complejidad:
    - Evitar overfitting utilizando early stopping, penalizaciones L1/L2 o pruning en árboles.

- Reducción de dimensionalidad:
    - Explorar PCA, t-SNE o UMAP para mejorar el rendimiento y la visualización de datos de alta dimensión.

- Comparación de modelos:
    - Documentar y comparar los resultados de distintos algoritmos.
    - Seleccionar el modelo final en función de la métrica más relevante para los objetivos del proyecto.

Se recomienda ver el [notebook de ejemplo](../notebooks/students_performance.ipynb) para comprender y aplicar los distintos tipos de aprendizaje. A partir del dataset *Student Performance* (UCI), el notebook recorre el flujo completo:

- Exploración de los datos y definición de la variable objetivo (clasificación binaria: aprueba / desaprueba).
- División estratificada en entrenamiento y test, y validación cruzada con `StratifiedKFold`.
- Modelo base con `DummyClassifier`.
- Random Forest, XGBoost y SVM (con escalado dentro de un `Pipeline`), con ajuste de hiperparámetros mediante Optimización Bayesiana (`BayesSearchCV`).
- Comparación con un modelo fundacional para datos tabulares ([TabICL](https://github.com/soda-inria/tabicl)), que no requiere ajuste de hiperparámetros.
- Evaluación con ROC-AUC, F1, recall y matriz de confusión, y comparación final de modelos.
- Análisis de importancia de variables y del impacto de incluir o no información previa (notas parciales).
- Aprendizaje no supervisado con K-Means (Silhouette, método del codo, Davies-Bouldin) y PCA para visualización.


##
<p align="right">Siguiente | <b><a href="resultados.md">Resultados y Conclusiones</a></b>
<br/>
Atrás | <b><a href="analisis_exploratorio.md">Análisis Exploratorio y Curación de Datos</a></p>

</b><p align="center"><sup> EnzoRg | </sup><a href="../README.md"><sup>Contenidos</sup></a></p>