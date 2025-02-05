# 🐶🐱 Classificador de Imagens: Cachorros vs Gatos

Este projeto utiliza aprendizado de máquina para classificar imagens entre **cachorros** e **gatos**.  
Ele foi treinado com o dataset [Dogs vs Cats do Kaggle](https://www.kaggle.com/datasets/salader/dogs-vs-cats).  
A acurácia do modelo foi de: 97.4875

## 📂 Estrutura do Projeto  

```
📁 projeto/
│── 📄 train_model.py        # Script para treinar o modelo
│── 📄 classifier_images.py   # Script para classificar novas imagens
│── 📁 train/                   # Pasta com imagens de treino (baixar do Kaggle)
│── 📁 test/                    # Pasta com imagens de teste (baixar do Kaggle)
│── 📁 imagens_para_classificar/ # Adicione imagens para classificação
│── 📁 output/                   # Resultado das imagens classificadas
```

## 🚀 Como Usar  

### 1️⃣ Baixar o dataset  
Baixe o conjunto de dados do Kaggle no link:  
🔗 [Dogs vs Cats Dataset](https://www.kaggle.com/datasets/salader/dogs-vs-cats)  

### 2️⃣ Organizar os arquivos  
Coloque as pastas `train/` e `test/` no diretório do projeto.  

### 3️⃣ Instalar dependências  
Antes de rodar os scripts, instale as bibliotecas necessárias:  
```bash
pip install tensorflow keras numpy opencv-python
```

### 4️⃣ Treinar o modelo  
Execute o script para treinar o modelo com as imagens:  
```bash
python train_model
```

### 5️⃣ Classificar imagens  
Coloque as imagens na pasta `imagens_para_classificar/` e execute:  
```bash
python classifier_images.py
```
As imagens classificadas serão salvas na pasta `output/`.  

## 📊 Resultados  

Após o treinamento, o modelo poderá distinguir **cachorros** de **gatos** com alta precisão, baseado no conjunto de dados fornecido.  

## 📜 Licença  

Este projeto é de livre uso para fins educacionais e experimentação. 🚀
