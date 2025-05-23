import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

caminho_arquivo = os.path.join(os.getcwd(), 'data', 'raw', 'Iris.csv')
destino = os.path.join(os.getcwd(), 'data', 'processed')

os.makedirs(destino, exist_ok=True)

print(f"Lendo o dataset de {caminho_arquivo}...")

df = pd.read_csv(caminho_arquivo)
print("Dataset lido com sucesso!")
print(df)

print("\nVerificando dados faltantes:")
print(df.isnull().sum())

X = df.drop('Species', axis=1)
y = df['Species']

scaler = StandardScaler()
X_normalizado = scaler.fit_transform(X)

X_normalizado = pd.DataFrame(X_normalizado, columns=X.columns)

df_processado = pd.concat([X_normalizado, y], axis=1)

caminho_saida = os.path.join(destino, 'iris_processed.csv')
df_processado.to_csv(caminho_saida, index=False)

print(f"\nDataset processado e salvo em {caminho_saida}")