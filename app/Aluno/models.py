from app.Pessoa.models import *

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, data_nascimento, email, telefone, numero_matricula):
      super().__init__(nome, sobrenome, data_nascimento, email, telefone)
      self.numero_matricula = numero_matricula
      self.notas = {}
    
    def adicionar_nota(self, disciplina, nota):
      self.notas[disciplina] = nota