import sqlite3

# Conectar ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Crie tabelas para as classes Aluno, Disciplina e Professor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        sobrenome TEXT,
        data_nascimento TEXT,
        email TEXT,
        telefone TEXT,
        numero_matricula TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS disciplina (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        descricao TEXT,
        carga_horaria INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS professor (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        sobrenome TEXT,
        data_nascimento TEXT,
        email TEXT,
        telefone TEXT,
        numero_registro TEXT
    )
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
