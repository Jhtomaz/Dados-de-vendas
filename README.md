# Dados de Vendas

Projeto simples para carregar, analisar e transformar uma base de dados de vendas com Python e pandas.

## Estrutura do projeto

```text
data/           Arquivo CSV original
notebooks/      Notebook de análise dos dados
transformation/ Script de transformação
output/         Arquivo CSV transformado
```

## Power BI

<img width="1313" height="738" alt="image" src="https://github.com/user-attachments/assets/9ac41d05-9de0-4696-ac1f-3f1ed1e5af81" />

## Requisitos

- Python 3
- pandas
- Jupyter Notebook (opcional, para executar o notebook)

Instale as dependências com:

```bash
pip install pandas jupyter
```

## Como executar

Para realizar a transformação dos dados:

```bash
python transformation/main.py
```

O arquivo processado será salvo na pasta `output/`.

Para abrir a análise exploratória:

```bash
jupyter notebook notebooks/analysis_data.ipynb
```

## Transformações realizadas

- Leitura do CSV considerando a vírgula como separador decimal.
- Padronização dos nomes das colunas.
- Conversão dos tipos de dados.
- Exportação da base tratada para um novo arquivo CSV.
