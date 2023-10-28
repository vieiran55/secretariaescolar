from app.Pessoa.models import *

class Professor(Pessoa):
    def __init__(self, nome, sobrenome, data_nascimento, email, telefone, numero_registro):
      super().__init__(nome, sobrenome, data_nascimento, email, telefone)
      self.numero_registro = numero_registro
      self.disciplinas_lecionadas = []
      
    def adicionar_disciplina(self, disciplina):
      self.disciplinas_lecionadas.append(disciplina)