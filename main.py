from flask import Flask, jsonify, request

from DataBase.dbService import init_database
from reviewLivroCadastroModel import ReviewLivroCadastroModel
from reviewService import ReviewService

#pip install -U flask-cors
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/listar-reviews")
def listar_reviews():
    pFiltroTexto = request.args.get('pFiltroTexto', default='', type=str)
    return ReviewService.get_listagem(pFiltroTexto)

@app.get("/consultar-por-id/<int:pId>")
def consultar_por_id(pId:int):
    return ReviewService.get_by_id(pId)

@app.delete("/deletar-por-id/<int:pId>")
def deletar_por_id(pId:int):
    return ReviewService.delete_by_id(pId)

@app.post("/cadastrar-review")
def cadastrar():
    pModel = ReviewLivroCadastroModel.from_dict(request.get_json()["registro"])
    return ReviewService.cadastrar_review(pModel)

@app.put("/alterar-review")
def alterar():
    pModel = ReviewLivroCadastroModel.from_dict(request.get_json()["registro"])
    return ReviewService.alterar_review(pModel)


init_database(app)

app.run(debug=True)