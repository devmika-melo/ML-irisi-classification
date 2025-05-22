# 🌸 Iris Classification 🌸

## Projeto de IA (Inteligência Artificial) tem como objetivo aplicar técnicas do modelo **Machine Learning** para realizar a **classificação das espécies de flores do dataset Iris**.

O projeto foi desenvolvido para um desafio IA inclusiva da Universidade Federal do Ceará - UFC.

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

## 🏗️ Estrutura do Projeto

```
iris-classification/
├── data/               # Dados brutos e processados
│   ├── processed/
│   └── raw/
├── outputs/            # Modelos treinados e gráficos
│   ├── figures/
│   └── models/
├── src/                # Código fonte
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── model_training.py
│   └── utils.py
├── LICENSE
├── .gitignore          # Arquivos e pastas ignoradas pelo git
├── README.md           # Documentação do projeto
└── requirements.txt    # Dependências do projeto
```


## 🚀 Como Executar

### 🔧 Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Execute os scripts na seguinte ordem:

### 1. Pré-processamento dos dados:
```bash
python src/data_preprocessing.py
```

### 2. Treinamento do modelo:
```bash
python src/model_evaluation.py
```

### 3. Avaliação do modelo:
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

## 📜 Licença
Este projeto é para fins educacionais e profissionais.

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

