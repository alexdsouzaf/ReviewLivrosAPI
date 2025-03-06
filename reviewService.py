import sqlite3

from flask import jsonify
from DataBase.dbService import get_database
from reviewLivroCadastroModel import ReviewLivroCadastroModel

# ? essas querys em string são a coisa mais insegura e feia possivel mas é o que temos pra hoje
class ReviewService:
    def __init__(self):
        pass

    @staticmethod
    def get_by_id(pId:int):
        context = get_database()
        cursor = context.cursor()
        query = cursor.execute(f'select * from reviews where id = {pId}')
        dictionary = [dict(row) for row in query]
        return jsonify(dictionary)
    
    @staticmethod
    def get_listagem(pFiltroTexto:str):
        context = get_database()
        cursor = context.cursor()

        query = 'select * from reviews'

        if (pFiltroTexto != ""):
            query += " where titulo like '%{}%'".format(pFiltroTexto)

        query = cursor.execute(query)
        dictionary = [dict(row) for row in query]
        return jsonify(dictionary)

    @staticmethod
    def cadastrar_review(pModel:ReviewLivroCadastroModel):
        try:
            context = get_database()
            cursor = context.cursor()
            cursor.execute(f'insert into reviews (titulo,review) values (?,?)',(pModel.titulo,pModel.review))
            context.commit()
        except sqlite3.Error as e:
            context.rollback()
            return jsonify({'error':str(e)}),500
        finally:
            context.close()
        
        return jsonify(200);

    @staticmethod
    def alterar_review(pModel:ReviewLivroCadastroModel):
        try:
            context = get_database()
            cursor = context.cursor()
            cursor.execute(f'update reviews set titulo = ?, review = ? where id = ?',(pModel.titulo,pModel.review,pModel.id))
            context.commit()
        except sqlite3.Error as e:
            context.rollback()
            return jsonify({'error':str(e)}),500
        finally:
            context.close()
        
        return jsonify(200);


    @staticmethod
    def delete_by_id(pId:int):
        try:
            context = get_database()
            cursor = context.cursor()
            query = cursor.execute(f'delete from reviews where id = {pId}')
            context.commit()
        except sqlite3.Error as e:
            context.rollback()
            return jsonify({'error':str(e)}),500
        finally:
            context.close()
        
        return jsonify(200)