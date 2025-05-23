import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

caminho_modelo = os.path.join(os.getcwd(), 'outputs', 'models', 'knn_model.joblib')
modelo = joblib.load(caminho_modelo)
print("Modelo carregado com sucesso!")

caminho_dados = os.path.join(os.getcwd(), 'data', 'processed', 'iris_processed.csv')
df = pd.read_csv(caminho_dados)
print("Dados carregados com sucesso!")

X = df.drop('Species', axis=1)
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

y_pred = modelo.predict(X_test)

acuracia = accuracy_score(y_test, y_pred)
print(f"\nAcurácia: {acuracia:.2f}")

print("\nMatriz de Confusão:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

destino_figuras = os.path.join(os.getcwd(), 'outputs', 'figures')
os.makedirs(destino_figuras, exist_ok=True)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=y.unique(),
            yticklabels=y.unique())

plt.title('Matriz de Confusão - KNN')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.tight_layout()

caminho_figura = os.path.join(destino_figuras, 'matriz_confusao.png')
plt.savefig(caminho_figura)
plt.show()

print(f"\nMatriz de confusão salva em {caminho_figura}")