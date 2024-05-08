import sklearn
# Imprime el dataset iris
from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

import pandas as pd
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

iris_df.head

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import seaborn as sns; sns.set()
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue='species', height=2.5)

#----------------------------------------
# Verificar el Dataframe
print(iris_df.head())

# Configurar el Kmeans para 5 clusters
kmeans = KMeans(n_clusters=5, random_state=42)

# Ajustar el modelo
kmeans.fit(iris_df)

# Obtener las etiquetas
labels = kmeans.predict(iris_df)

import matplotlib.pyplot  


