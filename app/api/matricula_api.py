import sqlite3

# Função para obter o próximo número de matrícula disponível
def gerar_matricula():
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(numero_matricula) FROM aluno')
    ultimo_numero_matricula = cursor.fetchone()[0]
    conn.close()

    if ultimo_numero_matricula is None:
        # Se não houver matrículas no banco de dados, comece com 20230000001
        proximo_numero_matricula = 20230000001
    else:
        # Caso contrário, incremente o último número de matrícula
        proximo_numero_matricula = int(ultimo_numero_matricula) + 1

    return proximo_numero_matricula