import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import warnings

# Cargar el dataset iris
iris = load_iris()

# Crear un DataFrame de pandas con los datos
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Configurar el estilo de seaborn
sns.set()

# Visualizar la relación entre las características con pairplot
sns.pairplot(iris_df, height=2.5)

# Ignorar las advertencias para una mejor visualización
warnings.filterwarnings("ignore", category=UserWarning)

# Configurar el Kmeans para 5 clusters
kmeans = KMeans(n_clusters=5, random_state=42)

# Ajustar el modelo KMeans
kmeans.fit(iris_df)

# Obtener las etiquetas de los clusters
labels = kmeans.predict(iris_df)

# Verificar el DataFrame
print(iris_df.head())
