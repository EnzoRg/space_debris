# Métricas de Clasificación: ROC-AUC, F1-Score y Recall

Este documento explica las tres métricas utilizadas en el [notebook de ejemplo](../notebooks/students_performance.ipynb) para evaluar los modelos de clasificación: **ROC-AUC**, **F1-Score** y **Recall**. Los ejemplos y resultados provienen de ese notebook, donde se predice si un estudiante aprueba o desaprueba a partir de variables demográficas, sociales y académicas.

## Contexto del problema

A partir de la nota final `G3` (de 0 a 20) se crea la variable objetivo `pass`:

- `pass = 1` → **aprobado** (`G3 >= 10`). Es la **clase positiva**.
- `pass = 0` → **desaprobado** (`G3 < 10`). Es la **clase negativa**.

Las clases están **desbalanceadas**: alrededor del 85% de los alumnos aprueba y solo el 15% desaprueba. En el conjunto de test hay 130 alumnos: 110 aprobados y 20 desaprobados.

### ¿Por qué no alcanza con el *accuracy*?

La exactitud (*accuracy*) mide el porcentaje de predicciones correctas. Con clases desbalanceadas es engañosa: un modelo que predice **siempre "aprobado"**, sin mirar ningún dato, acierta 110 de 130 casos y obtiene un *accuracy* de **0.846**, aunque no detecta a **ningún** desaprobado.

Por eso en el notebook se usan tres métricas complementarias, que miran el problema desde ángulos distintos.

## La matriz de confusión

Todas las métricas parten de la **matriz de confusión**, que cruza la etiqueta real con la predicción del modelo. Con aprobado como clase positiva:

|                         | Predicción: Desaprobado | Predicción: Aprobado |
|-------------------------|:-----------------------:|:--------------------:|
| **Real: Desaprobado**   | **TN** (verdadero negativo) | **FP** (falso positivo) |
| **Real: Aprobado**      | **FN** (falso negativo) | **TP** (verdadero positivo) |

- **TP:** aprobados que el modelo predice como aprobados.
- **TN:** desaprobados que el modelo predice como desaprobados.
- **FP:** desaprobados que el modelo predice como aprobados. **Es el error más costoso en este problema**: son alumnos en riesgo que pasan desapercibidos.
- **FN:** aprobados que el modelo predice como desaprobados.

Por ejemplo, la matriz de confusión del **SVM optimizado** en test es:

|                         | Predicción: Desaprobado | Predicción: Aprobado |
|-------------------------|:-----------------------:|:--------------------:|
| **Real: Desaprobado**   | TN = 14 | FP = 6 |
| **Real: Aprobado**      | FN = 1  | TP = 109 |

En el notebook, la función `plot_evaluation()` grafica esta matriz para cada modelo junto con la curva ROC.

## Recall

### Definición

El **recall** (también llamado **sensibilidad** o **tasa de verdaderos positivos**) responde a la pregunta:

> De todos los casos que **realmente** pertenecen a una clase, ¿qué proporción detectó el modelo?

Para la clase positiva (aprobados):

$$
\text{Recall}_{\text{aprobados}} = \frac{TP}{TP + FN}
$$

Para la clase negativa (desaprobados), el recall se calcula de forma análoga pero mirando la fila de los desaprobados:

$$
\text{Recall}_{\text{desaprobados}} = \frac{TN}{TN + FP}
$$

Toma valores entre 0 y 1, donde 1 significa que el modelo no dejó escapar ningún caso de esa clase.

### ¿Por qué el recall de desaprobados?

El conjunto de datos se creó para entender **por qué los alumnos desaprueban**. El objetivo práctico es detectar a los alumnos en riesgo para poder intervenir a tiempo. Por eso, en el notebook no se mide el recall de aprobados sino el de **desaprobados**: interesa que el modelo **no deje pasar desaprobados** (es decir, que tenga pocos FP).

Con la matriz del SVM optimizado:

$$
\text{Recall}_{\text{desaprobados}} = \frac{14}{14 + 6} = 0.70
$$

El modelo detecta 14 de los 20 alumnos que realmente desaprobaron.

### En código

`recall_score()` calcula por defecto el recall de la clase `1`. Para calcularlo sobre los desaprobados se indica `pos_label=0`:

```python
from sklearn.metrics import recall_score

recall_score(y_test, y_pred, pos_label=0)
```

Se calcula sobre la **predicción final** (`y_pred`, con valores 0 o 1), por lo que depende del *threshold* de decisión (ver más abajo).

### Limitación

El recall solo mira una fila de la matriz de confusión. Un modelo que predice **siempre "desaprobado"** tendría recall de desaprobados = 1, pero sería inútil porque clasificaría mal a todos los aprobados. Por eso el recall nunca se usa solo: se complementa con métricas como la *precision* o el F1.

## F1-Score

### Precision

Antes de definir el F1 hace falta la **precision** (precisión), que responde a otra pregunta:

> De todos los casos que el modelo **predijo** como de una clase, ¿qué proporción era realmente de esa clase?

$$
\text{Precision}_{\text{aprobados}} = \frac{TP}{TP + FP}
$$

Recall y precision suelen estar en tensión: un modelo muy "generoso", que predice aprobado casi siempre, tendrá recall alto y precision baja; uno muy "exigente", al revés.

### Definición

El **F1-Score** combina precision y recall en una sola métrica mediante su **media armónica**:

$$
F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\,TP}{2\,TP + FP + FN}
$$

La media armónica penaliza los desbalances: si una de las dos es baja, el F1 también lo es. Solo es alto cuando **ambas** son altas. Toma valores entre 0 y 1.

Con la matriz del SVM optimizado:

$$
\text{Precision} = \frac{109}{109 + 6} = 0.948 \qquad \text{Recall} = \frac{109}{109 + 1} = 0.991
$$

$$
F_1 = \frac{2 \cdot 109}{2 \cdot 109 + 6 + 1} = \frac{218}{225} = 0.9689
$$

### En código

`f1_score()` se calcula por defecto sobre la clase positiva (`pos_label=1`, aprobados):

```python
from sklearn.metrics import f1_score

f1_score(y_test, y_pred)  # F1 de aprobados (clase 1)
f1_score(y_test, y_pred, pos_label=0)  # F1 de desaprobados (clase 0)
f1_score(y_test, y_pred, average="macro")  # promedio simple de ambas clases
```

En la validación cruzada se usa con `scoring=['roc_auc', 'f1']`, que también calcula el F1 de la clase positiva.

### Cuidado: el F1 de la clase mayoritaria puede engañar

El modelo base (`DummyClassifier` que predice siempre aprobado) tiene la siguiente matriz en test: TP = 110, FP = 20, FN = 0, TN = 0. Su F1 de aprobados es:

$$
F_1 = \frac{2 \cdot 110}{2 \cdot 110 + 20 + 0} = 0.9167
$$

Un valor alto para un modelo que **no aprendió nada**. Como los aprobados son mayoría, casi cualquier modelo obtiene un buen F1 sobre esa clase. Por eso, en la comparación final, la diferencia en F1 entre el *baseline* y los demás modelos es mucho menor que en ROC-AUC o en recall de desaprobados.

Si se calcula el F1 sobre la clase minoritaria, la diferencia se vuelve evidente:

| Modelo      | F1 (aprobados) | F1 (desaprobados) | F1 macro |
|-------------|:--------------:|:-----------------:|:--------:|
| Baseline    | 0.9167         | 0.0000            | 0.4583   |
| SVM Opt.    | 0.9689         | 0.8000            | 0.8844   |

Cuando la clase de interés es la minoritaria, conviene reportar el F1 de esa clase o el F1 macro además del F1 de la clase positiva.

## ROC-AUC

### El *threshold* de decisión

La mayoría de los clasificadores no devuelve directamente 0 o 1, sino un **puntaje**: por ejemplo, la probabilidad de aprobar (`predict_proba()`) o, en el caso de SVM, la distancia al hiperplano (`decision_function()`). Luego, un **umbral** (*threshold*) transforma ese puntaje en una predicción:

- Si la probabilidad de aprobar es mayor o igual al *threshold* → aprobado.
- En caso contrario → desaprobado.

Por defecto, `predict()` usa un *threshold* de 0.5. Pero ese valor es arbitrario: con otro *threshold* cambian la matriz de confusión, el recall y el F1.

### La curva ROC

La **curva ROC** (*Receiver Operating Characteristic*) muestra el comportamiento del modelo **para todos los *thresholds* posibles**. Para cada *threshold* se calculan dos tasas:

- **Eje Y — Tasa de verdaderos positivos (TPR):** proporción de aprobados clasificados correctamente como aprobados. Es el recall de aprobados.

$$
TPR = \frac{TP}{TP + FN}
$$

- **Eje X — Tasa de falsos positivos (FPR):** proporción de desaprobados clasificados incorrectamente como aprobados.

$$
FPR = \frac{FP}{FP + TN} = 1 - \text{Recall}_{\text{desaprobados}}
$$

Cada punto de la curva es un *threshold* distinto:

- **(0, 0):** *threshold* máximo. El modelo no predice a nadie como aprobado: no comete falsos positivos, pero tampoco detecta aprobados.
- **(1, 1):** *threshold* mínimo. El modelo predice a todos como aprobados: detecta a todos los aprobados, pero también clasifica como aprobados a todos los desaprobados.
- **(0, 1):** esquina superior izquierda. Clasificador perfecto: detecta a todos los aprobados sin ningún falso positivo.
- **Diagonal:** clasificador aleatorio, que no distingue entre clases.

Por ejemplo, un punto (0.4, 1) indicaría que, con ese *threshold*, el modelo reconoce al 100% de los aprobados, pero a costa de clasificar como aprobados al 40% de los desaprobados.

Notar la relación con el recall de desaprobados: el punto de la curva correspondiente al *threshold* 0.5 del SVM optimizado tiene FPR = 6 / 20 = 0.30, es decir, recall de desaprobados = 1 − 0.30 = 0.70.

### El área bajo la curva (AUC)

El **ROC-AUC** (*Area Under the Curve*) resume la curva en un solo número: el área que queda debajo de ella.

| ROC-AUC | Interpretación |
|:-------:|----------------|
| 1.0     | Clasificador perfecto: separa completamente ambas clases. |
| 0.5     | Clasificador aleatorio: no distingue las clases (la diagonal). |
| < 0.5   | Peor que el azar: ordena las clases al revés. |

Tiene además una interpretación probabilística muy útil:

> El ROC-AUC es la probabilidad de que, dado un alumno aprobado y uno desaprobado elegidos al azar, el modelo le asigne un puntaje más alto al aprobado.

Es decir, mide qué tan bien el modelo **ordena** a los alumnos, sin importar el *threshold* elegido.

#### Ejemplo con cuatro alumnos

Supongamos que un modelo asigna las siguientes probabilidades de aprobar:

| Alumno | Etiqueta real | Probabilidad de aprobar |
|:------:|:-------------:|:-----------------------:|
| A      | Aprobado      | 0.9 |
| B      | Aprobado      | 0.6 |
| C      | Desaprobado   | 0.7 |
| D      | Desaprobado   | 0.2 |

Se comparan todos los pares (aprobado, desaprobado):

| Par   | ¿El aprobado tiene mayor puntaje? |
|:-----:|:---------------------------------:|
| A – C | Sí (0.9 > 0.7) |
| A – D | Sí (0.9 > 0.2) |
| B – C | No (0.6 < 0.7) |
| B – D | Sí (0.6 > 0.2) |

El modelo ordena correctamente 3 de los 4 pares, por lo que su **ROC-AUC = 0.75**.

### En código

A diferencia del recall y el F1, el ROC-AUC necesita el **puntaje** del modelo, no la predicción final:

```python
from sklearn.metrics import roc_auc_score, roc_curve

y_score = model.predict_proba(X_test)[:, 1]  # probabilidad de la clase positiva
roc_auc_score(y_test, y_score)

fpr, tpr, thresholds = roc_curve(y_test, y_score)  # puntos de la curva
```

Para `SVC`, que no calcula probabilidades por defecto, se usa `decision_function()`. No hace falta que el puntaje sea una probabilidad: alcanza con que ordene a los alumnos de menos a más probable de aprobar.

```python
y_score_svm = svm.decision_function(X_test)
roc_auc_score(y_test, y_score_svm)
```

> **Error frecuente:** pasar `y_pred` (0 o 1) a `roc_auc_score()`. Con predicciones binarias la curva queda reducida a un único *threshold* y el AUC resultante no refleja la capacidad real del modelo para ordenar las clases.

### Ventajas y limitaciones

- **No depende del *threshold*:** evalúa el modelo en su conjunto, antes de decidir dónde cortar.
- **Robusta al desbalance:** el *baseline* obtiene exactamente 0.5, sin importar que el 85% de los alumnos apruebe. Por eso se usó como métrica para optimizar hiperparámetros (`scoring='roc_auc'` en `BayesSearchCV`).
- **No dice cómo se comporta el modelo con el *threshold* que finalmente se use.** Dos modelos con el mismo AUC pueden tener recall de desaprobados muy distintos a *threshold* 0.5. Por eso se complementa con recall y F1.

## Las tres métricas juntas

Cada métrica responde una pregunta distinta:

| Métrica | Pregunta que responde | Usa | Depende del *threshold* |
|---------|-----------------------|-----|:-----------------------:|
| **ROC-AUC** | ¿Qué tan bien ordena el modelo a aprobados y desaprobados? | Puntaje (`predict_proba`, `decision_function`) | No |
| **F1 (aprobados)** | ¿Qué tan bien equilibra falsos positivos y falsos negativos sobre la clase positiva? | Predicción (`predict`) | Sí |
| **Recall (desaprobados)** | ¿Qué proporción de los alumnos que desaprueban detecta el modelo? | Predicción (`predict`) | Sí |

En el notebook se calculan las tres con la función `evaluate()`:

```python
def evaluate(name, y_true, y_score, y_pred):
    # y_score: probabilidad (o puntaje) de la clase positiva, necesaria para ROC-AUC
    # y_pred: predicción final (0 o 1), necesaria para F1 y recall
    results[name] = {
        "ROC-AUC": roc_auc_score(y_true, y_score),
        "F1 (aprobados)": f1_score(y_true, y_pred),
        "Recall (desaprobados)": recall_score(y_true, y_pred, pos_label=0),
    }
    return pd.DataFrame(results[name], index=[name]).round(4)
```

### El caso del *baseline*

El modelo base muestra por qué hace falta mirar más de una métrica:

| Modelo   | ROC-AUC | F1 (aprobados) | Recall (desaprobados) |
|----------|:-------:|:--------------:|:---------------------:|
| Baseline | 0.5000  | 0.9167         | 0.00                  |

- El **ROC-AUC de 0.5** indica que no distingue entre clases.
- El **F1 de aprobados** es alto solo porque la mayoría aprueba.
- El **recall de desaprobados de 0** muestra que no detecta a ningún alumno en riesgo.

Mirando solo el F1, el *baseline* parecería un buen modelo.

### Comparación final de modelos

Resultados en el conjunto de test, ordenados por ROC-AUC:

| Modelo              | ROC-AUC | F1 (aprobados) | Recall (desaprobados) |
|---------------------|:-------:|:--------------:|:---------------------:|
| TabICL              | 0.9723  | 0.9596         | 0.70                  |
| XGBoost Opt.        | 0.9668  | 0.9554         | 0.65                  |
| SVM Opt.            | 0.9618  | 0.9689         | 0.70                  |
| Random Forest Opt.  | 0.9573  | 0.9511         | 0.60                  |
| XGBoost             | 0.9432  | 0.9459         | 0.65                  |
| SVM                 | 0.9427  | 0.9558         | 0.60                  |
| Random Forest       | 0.9405  | 0.9417         | 0.60                  |
| Baseline            | 0.5000  | 0.9167         | 0.00                  |

Algunas lecturas:

- **Ninguna métrica elige sola al mejor modelo.** TabICL tiene el mejor ROC-AUC, SVM Opt. el mejor F1, y ambos empatan en recall de desaprobados.
- **TabICL y SVM Opt. detectan la misma cantidad de desaprobados** (14 de 20), pero TabICL tiene más falsos negativos (3 frente a 1), por lo que su F1 es menor.
- **El mejor AUC no implica el mejor recall a *threshold* 0.5.** XGBoost Opt. tiene mayor AUC que SVM Opt., pero menor recall de desaprobados.
- **La elección depende del objetivo.** Si lo importante es detectar alumnos en riesgo, el recall de desaprobados es la métrica a priorizar.

## Ajustar el *threshold*

Como el recall y el F1 dependen del *threshold*, se pueden modificar sin reentrenar el modelo. Si se quiere detectar más desaprobados, se puede **subir** el *threshold* para predecir "aprobado": el modelo solo clasificará como aprobado a quien tenga una probabilidad muy alta, y más alumnos quedarán marcados como en riesgo.

```python
threshold = 0.7
y_pred_custom = (y_prob >= threshold).astype(int)

recall_score(y_test, y_pred_custom, pos_label=0)
```

El costo es un aumento de los falsos negativos (aprobados marcados como en riesgo). En este problema ese costo suele ser aceptable: es preferible acompañar a un alumno que no lo necesitaba que dejar pasar a uno que va a desaprobar.

El ROC-AUC **no cambia** al modificar el *threshold*, porque ya considera todos los posibles. La curva ROC es justamente la herramienta para elegir un *threshold* adecuado: cada punto muestra el compromiso entre detectar aprobados (TPR) y dejar pasar desaprobados (FPR).

> **Importante:** el *threshold* es un hiperparámetro más. Debe elegirse con los datos de entrenamiento (por ejemplo, con las predicciones de la validación cruzada) y no mirando el conjunto de test.

## Cuidado con el tamaño del conjunto de test

El conjunto de test tiene solo **20 desaprobados**. Un único alumno mal clasificado cambia el recall de desaprobados en **5 puntos** (1 / 20 = 0.05). Por eso las diferencias pequeñas entre modelos no alcanzan para afirmar que uno es claramente superior.

Para tener una estimación más robusta conviene mirar también la **media y el desvío de la validación cruzada**, como hace la función `print_cv_scores()` del notebook:

| Modelo        | ROC-AUC (CV)      | F1 (CV)           |
|---------------|:-----------------:|:-----------------:|
| Baseline      | 0.5000 ± 0.0000   | 0.9165 ± 0.0005   |
| Random Forest | 0.9636 ± 0.0344   | 0.9629 ± 0.0173   |
| XGBoost       | 0.9573 ± 0.0399   | 0.9637 ± 0.0178   |
| SVM           | 0.9523 ± 0.0298   | 0.9491 ± 0.0143   |
| TabICL        | 0.9705 ± 0.0304   | 0.9603 ± 0.0146   |

Los desvíos (del orden de 0.03 en ROC-AUC) son mayores que muchas de las diferencias entre modelos en test.

## Resumen

- Con clases desbalanceadas, el *accuracy* y el F1 de la clase mayoritaria pueden dar una imagen engañosamente buena.
- **ROC-AUC** mide la capacidad del modelo para **ordenar** las clases, independientemente del *threshold*. Se calcula con puntajes o probabilidades, y un valor de 0.5 equivale al azar.
- **F1-Score** equilibra precision y recall sobre una clase. Por defecto se calcula sobre la clase positiva; si la clase de interés es la minoritaria, conviene calcularlo sobre ella o usar el promedio macro.
- **Recall** mide qué proporción de una clase detecta el modelo. En este problema, el **recall de desaprobados** es la métrica más alineada con el objetivo de detectar alumnos en riesgo.
- Recall y F1 dependen del *threshold*, que puede ajustarse según el costo de cada tipo de error.
- Ninguna métrica alcanza por sí sola: hay que elegir la que mejor refleje el objetivo del proyecto y complementarla con las demás.

##
<p align="right">Volver | <b><a href="aprendizaje.md">Aprendizaje Supervisado y/o No Supervisado</a></b>
<br/>

</b><p align="center"><sup> EnzoRg | </sup><a href="../README.md"><sup>Contenidos</sup></a></p>