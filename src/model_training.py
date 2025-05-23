import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

caminho_dados = os.path.join(os.getcwd(), 'data', 'processed', 'iris_processed.csv')
df = pd.read_csv(caminho_dados)

print("Dados carregados com sucesso")
print(df)

X = df.drop('Species', axis=1)
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42,stratify=y)

print(f"\nTamanho do treino: {X_train.shape}")
print(f"Tamanho do teste: {X_test.shape}")

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

print("\nModelo KNN treinado com sucesso!")

destino_modelo = os.path.join(os.getcwd(), 'outputs', 'models')
os.makedirs(destino_modelo, exist_ok=True)

caminho_modelo = os.path.join(destino_modelo, 'knn_model.joblib')
joblib.dump(modelo, caminho_modelo)

print(f"\nModelo salvo em {caminho_modelo}")