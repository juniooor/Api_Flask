from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(jsonify(Carros) ) 

@app.route('/')
def create_car():
    carro = request.json
    Carros.append(carro)
    return carro

app.run()