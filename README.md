<h1 align="center"> 🌸 Iris Classification 🌸</h1>

## Projeto de IA (Inteligência Artificial) tem como objetivo aplicar técnicas do modelo **Machine Learning** para realizar a **classificação das espécies de flores do dataset Iris**.

_<h3 aling="center">O projeto foi desenvolvido para um desafio do projeto de extenção IA inclusiva da Universidade Federal do Ceará - UFC.</h3>_

## 📊 Sobre o Dataset

O dataset Iris é um dos mais famosos da estatística e da ciência de dados. Ele contém 150 registros de flores, divididos igualmente entre 3 espécies:
- Iris Setosa
- Iris Versicolor
- Iris Virginica

Cada registro possui 4 atributos:
- Comprimento da sépala (sepal length)
- Largura da sépala (sepal width)
- Comprimento da pétala (petal length)
- Largura da pétala (petal width)

Fonte dos dados: [Kaggle - UCI Iris Dataset](https://www.kaggle.com/datasets/uciml/iris)

## 🏗️ Estrutura do Projeto

```
iris-classification/
├── data/               # Dados brutos do dataset e processados, após normalização
│   ├── processed/
│   └── raw/
├── img/                # Img do meu perfil
├── outputs/            # Modelos treinados e imagem dos gráficos
│   ├── figures/
│   └── models/
├── src/                # Código fonte do processo
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── download_data.py        # Baixa o dataset Iris do Kaggle
│   ├── model_evaluation.py
│   └── model_training.py
├── .gitignore  
├── LICENSE        
├── README.md           
└── requirements.txt   
```


## 🚀 Como Executar

### 🔧 Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Execute os scripts na seguinte ordem:

### 1.  Baixar os dados:
```bash
python src/download_data.py
```

### 2. Pré-processamento dos dados:
```bash
python src/data_preprocessing.py
```

### 3. Treinamento do modelo:
```bash
python src/model_evaluation.py
```

### 4. Avaliação do modelo:
```bash
python src/model_training.py
```

## 🧠 Tecnologias utilizadas
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- KaggleHub


## 📈 Métricas e Resultados
- 🎯 Acurácia: 0.98
- 📊 Matriz de Confusão: salva na pasta /outputs/figures.
- 💾 Modelo treinado: salvo em /outputs/models/knn_model.joblib.

## 📜 Licença
Este projeto é para fins educacionais e profissionais.

## 👩‍💻 Autora
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/devmika-melo" target="_blank">
        <img src="img/ingrid melo.jpg" width="100px;" alt="Ingrid Melo"/><br>
        <sub>
          <b>Ingrid Melo</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

