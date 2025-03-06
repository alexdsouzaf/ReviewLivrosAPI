import sqlite3

from flask import Flask, app

DATABASE = "db_reviews.db"

# * retorna uma conexao com o banco de dados
def get_database() -> sqlite3.Connection:
    context = sqlite3.connect(DATABASE)
    context.row_factory = sqlite3.Row
    return context

# * inicializa o banco de dados gerando as migracoes
def init_database(app : Flask):
    with app.app_context():
        context = get_database()
        with app.open_resource('DataBase/schema.sql', mode='r') as f:
            context.cursor().executescript(f.read())
        context.commit()