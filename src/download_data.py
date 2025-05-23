import kagglehub
import os
import shutil

print("Baixando o dataset Iris...")
path = kagglehub.dataset_download("uciml/iris")
print("Dataset baixado em:", path)

destino = os.path.join(os.getcwd(), 'data', 'raw')

os.makedirs(destino, exist_ok=True)

for arquivo in os.listdir(path):
    origem = os.path.join(path, arquivo)
    destino_arquivo = os.path.join(destino, arquivo)
    shutil.copy2(origem, destino_arquivo)

print(f"Arquivos copiados para {destino} com sucesso!")