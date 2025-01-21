### Projeto de Scrapping com Python

Este documento apresenta a realização do projeto de webscraping que teve como objetivo principal: praticar os fundamentos da linguagem python, desenvolver noções de análise de dados por meio de dados públicos e fictícios da web. Foram utilizadas as seguintes bibliotecas e suas funções: ``requests`` para realização de requisições http e ``beautifulsoup4`` para realizar a extração dos dados para análise.

**Estrutura do diretório**

- main.py - script .py responsável pela inicialização e execução do código do projeto; 
- requirements.txt - arquivo .txt que contém as dependencias necessarias para execucao do projeto; 
- .gitignore - arquivo git que fica responsavel por excluir do historico git a pasta .venv utilizada durante o desenvolvimento do projeto; 
- data/ - pasta criada pelo script main.py que será o diretório dos dados extraídos; 
- /data.csv - arquivo .csv que contém os dados do projeto;

**Desenvolvimento**

O projeto foi desenvolvido utilizando paradigma de programação funcional, onde cada função tem um papel crucial e segue uma lógica de execução afim de deixar o código com uma maior taxa de manutenibilidade.

##### Estrutura do arquivo main.py

A princípio, inicia-se importando as bibliotecas e dependências necessárias para execução do projeto.

```python
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import os
```




