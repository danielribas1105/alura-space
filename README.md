## Crie o ambiente virtual:

python -m venv venv

## Ative o ambiente virtual de acordo com o terminal que você usa:

### Prompt de Comando (cmd):

venv\Scripts\activate

### PowerShell:

.\venv\Scripts\Activate.ps1

### Git Bash:

source venv/Scripts/activate

## Para desativar o ambiente virtual

deactivate

## Instale as dependências:

pip install fastapi

pip install pydantic

pip install uvicorn

pip install pymongo python-dotenv

## Verificar pacotes instalados

pip freeze

## Criar o requirements.txt a partir do pip freeze

pip freeze > requirements.txt <!-- cria e/ou atualiza o requirements.txt -->

## Para instalar as dependências em outro ambiente

pip install -r requirements.txt

## Para desistalar um pacote

pip uninstall 'nome_do_pacote'

## ▶️ Rodando o servidor

uvicorn app.main:app --reload

## Para rodar a aplicação

uvicorn main:app --reload

# Django

## Consultar comandos

django-admin help

## Para iniciar um projeto Django

django-admin startproject config .

## Rodar o servidor django

python manage.py runserver

## Migrations

python manage.py makemigrations

python manage.py migrate

## Atualizar os arquivos static/

python manage.py collectstatic
