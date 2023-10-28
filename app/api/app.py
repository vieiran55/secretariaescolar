from flask import Flask, request, jsonify
from alunos_api import alunos_bp
import sqlite3

app = Flask(__name__)

# Endpoint para listar todos os alunos
@app.route('/', methods=['GET'])
def pagina_inicial():
    return jsonify("Bem-vindo ao banco de dados da escola")

# Outros endpoints para professores, disciplinas, etc.

app.register_blueprint(alunos_bp)

if __name__ == '__main__':
    app.run(debug=True)
