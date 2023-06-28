# Terra Instruments API

Este projeto faz parte do MVP da Disciplina Sprint I: Desenvolvimento Full Stack Básico, pós-graduação PUC-Rio.


---
## Observação importante

Ao clonar este repositório, delete a pasta `venv`, para que você possa criar o seu ambiente virtual e instalar as dependências/bibliotecas.


---
## Criando o ambiente virtual

Abra um novo terminal e digite o seguinte comando:
```
python -m venv venv
```
> Este comando cria um novo ambiente virtual usando o módulo "venv" do Python.

Ative o ambiente virtual digitando o seguinte comando:
```
.\venv\Scripts\Activate.ps1   
```


---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório e criar o ambiente virtual, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.
```
pip install -r requirements.txt
```
> Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API, basta executar:
```
flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte. 
```
flask run --host 0.0.0.0 --port 5000 --reload
```

> Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
