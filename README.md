# sistema_de_controle_de_material_de_apoio_SCMA

# Descrição
O SCMA, é um sistema de controle que é responsável por gerenciar todo o material de apoio utilizados pelos docentes do Ceres Caicó, a fim de eliminar o controle destes materiais através de planilhas em papel , reduzindo o consumo de material , agilizando o processo e permitindo um maior controle do patrimônio.


## Tutorial para instalação e configuração do git 

    https://www.webdevdrops.com/git-no-windows-github/

## Tutorial de Django

    Django 2.0 - Fundamentos Gregory Pacheco 1 / 19

    https://www.youtube.com/watch?v=UIvnNCQnejw&list=PLHWfNMxB2F4HdKbo8zdgXyxVDOxH429Ko

    Aprenda Django Victor Lima - Guia do Programador 1 / 5

    https://www.youtube.com/watch?v=Vs1Uk5MzKis&list=PLJ_KhUnlXUPvJRWpVRILh-pNTMk3KmluE&index=2

    Python Django Tutorials Tech With Tim 1 / 11

    https://www.youtube.com/watch?v=Z4D3M-NSN58&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9


C:\Users\proxx\Desktop\sonar-scanner-4.7.0.2747-windows\bin\sonar-scanner.bat -D sonar.login=b6d0bab1e972644439b6efc872720c910bdbdf3a


## Passo a passo da execução do projeto

### Passo 1
Criando o clone do repositório do projeto :

*Copiar o link do repositório no Github.
```console 
git clone https://github.com/marlemM/SCMA.git
```
### Passo 2
Criando ambiente virtual :
```console
python3 -m venv .venv
```
### Passo 3
Ativando ambiente virtual:
```console
source .venv/bin/activate
```
### Passo 4
Entrando na pasta do projeto:
```console
cd SCMA
```
### Passo 5
Criar arquivo "requirements.txt":
*No vscode criar um novo arquivo com o seguinte conteúdo:
````
django==4.1.4
python-decouple==3.6
coverage==6.5.0
````
### Passo 6
Instalar o requirements:
```console
pip install -r requirements.txt
```


## Passo a passo - rodando o programa
### Passo 1
A partir do vs code dentro de SCMA
``` 
cd projeto
```
### Passo 2
Já dentro do projeto
```
python manage.py migrate
```

### Passo 3
```
python manage.py runserver
```

### Passo 4
No terminal aparece o caminho, como omouse em cima desse caminho , segurar o ctrl e clicar para abrir o navegador.
