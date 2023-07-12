# Terra Instruments API

Este projeto faz parte do MVP da Disciplina Sprint I: Desenvolvimento Full Stack Básico, pós-graduação PUC-Rio.
O objetivo desta aplicação é desempenhar o controle e a visualização dos recursos disponibilizados pela loja fictícia chamada Terra Instruments, 
a qual vende produtos para músicos, em geral.
Esta aplicação permite aos usuários consultar, adicionar ou deletar produtos cadastrados no banco de dados, bem como adicionar ou deletar comentários associados
aos produtos.


---
## Observação 1

A pasta `venv`, presente neste repositório, representa o ambiente virtual utilizado para construir este projeto.
Nesta pasta já se encontram todas as dependências e bibliotecas necessárias para executar esta API.


---
## Como executar a API

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder ativar o ambiente virtual.

Ative o ambiente virtual digitando o seguinte comando:
```
.\venv\Scripts\Activate.ps1   
```

Para executar a API, basta executar:
```
(venv) flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte. 
```
(venv) flask run --host 0.0.0.0 --port 5000 --reload
```

> Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


---
## Observação 2

Em um contexto em que a pasta `venv`, presente neste repositório, se encontre inexistente ou indisponível na sua máquina, siga os seguintes passos.


---
### Passo 1: Criando um ambiente virtual

Após clonar o repositório, abra um novo terminal e digite o seguinte comando:
```
python -m venv venv
```
> Este comando cria um novo ambiente virtual usando o módulo "venv" do Python.

Ative o ambiente virtual digitando o seguinte comando:
```
.\venv\Scripts\Activate.ps1   
```


---
### Passo 2: Executando a API

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório e ativar o ambiente virtual (veja o passo 1), é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.
```
(venv) pip install -r requirements.txt
```
> Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API, basta executar:
```
(venv) flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte. 
```
(venv) flask run --host 0.0.0.0 --port 5000 --reload
```

> Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
