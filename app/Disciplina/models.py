class Disciplina:
  def __init__(self, nome, descricao, carga_horaria):
    self.nome = nome
    self.descricao = descricao
    self.carga_horaria = carga_horaria
    self.alunos_inscritos = []
    
  def inscrever_aluno(self, aluno):
    self.alunos_inscritos.append(aluno)