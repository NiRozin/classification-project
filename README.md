# Projeto de classificação

Resolução de problema de [classificação](http://archive.ics.uci.edu/ml/datasets/Census+Income)

## Atenção:
A parte do teste foi feita muito rápida e havia um erro no target afetando a avaliação final do algoritmo, verificando isso após o prazo, no dia seguinte o problema foi corrigido e as mudanças podem ser rastreadas pelo commit do git, a versão anterior do jupyter notebook com esse resultado pode ser visualizada (_notebooks/model_processing.ipynb_), mas se repŕocessada irá sobrescrever com o resultado corrigido, uma vez que a função foi alterada.


## Processamento

O processamento dos dados e dos modelos são feito no Jupyter Notebook _notebooks/model_processing_correto.ipynb_,
enquanto a análise inicial dos dados é dado no notebook _notebooks/analise-inicial-das-features.ipynb_

## Sobre o ambiente: 

**Linguagem**

Python = 3.8.10


**Gerenciamento de dependências:**

- **(Ao clonar o projeto)** Criar o ambiente, caso ele não exista:


    $ cd <path_env>

    $ python3 -m venv <env_name>

ou

    $ python -m venv <env_name>

Se a chamada 'python' refere-se a versão 3.

- **(Ao fazer um pull)** Atualizar o ambiente com as dependências caso ele já exista:

Isso pode ser feito com pip ativando o ambiente:

    $ source <path_env>/<env_name>/bin/activate
    $ pip install -r requirements.txt
    $ deactivate

Ou chamando o pip pelo diretório do ambiente

    $  <path_env>/<env_name>/bin/pip install -r requirements.txt


- **(Antes do push)** Atualizar o arquivo de dependências do ambiente:

Isso pode ser feito com pip ativando o ambiente:

    $ source <path_env>/<env_name>/bin/activate
    $ pip freeze > requirements.txt
    $ deactivate

Ou chamando o pip pelo diretório do ambiente

    $ <path_env>/<env_name>/bin/pip freeze > requirements.txt


- Ativação: 


        $ source <path_env>/<env_name>/bin/activate


- Desativação do ambiente:


        $ deactivate




## Organização do projeto

    
    ├── README.md          <- Apresentação do projeto.
    ├── data
    │   ├── processed      <- dados processados para modelagem.
    │   └── raw            <- Dados originais.
    │
    ├── models             <- Modelos treinados eserializados
    │
    ├── notebooks          <- Jupyter notebooks. 
    │                             │                         
    │
    ├── requirements.txt   <- Dependências do ambiente de desenvolvimento.
    │                 
    │
    └── src                <- Scripts do projeto
        ├── __init__.py    <- Faz de src um mosulo Python
        │
        ├── data           <- Scripts para fazer o download e manipulação dos conjuntos de dados
        │   └── make_dataset.py
        │   └── resampling.py
        │
        ├── features       <- Scripts para transformar os dados em atributos para o modelo
        │   └── build_features.py
        │   └── features_encoder.py
        │
        └── models         <- Script para busca de parâmetros, treinamento e teste de mdoelos
            └── model.py                               
            
 

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
