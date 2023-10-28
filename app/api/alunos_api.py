import sqlite3
from flask import Blueprint, request, jsonify
from matricula_api import gerar_matricula

alunos_bp = Blueprint('alunos_bp', __name__)

# Endpoint para criar um novo aluno
@alunos_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    dados_aluno = request.get_json()
    matricula_auto = gerar_matricula()  # Gere uma nova matrícula para cada aluno
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO aluno (nome, sobrenome, data_nascimento, email, telefone, numero_matricula) VALUES (?, ?, ?, ?, ?, ?)',
                   (dados_aluno['nome'], dados_aluno['sobrenome'], dados_aluno['data_nascimento'], dados_aluno['email'], dados_aluno['telefone'], matricula_auto))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Aluno criado com sucesso'}), 201

# Endpoint para listar todos os alunos
@alunos_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM aluno')
    alunos = cursor.fetchall()
    conn.close()
    return jsonify({'alunos': alunos})