import tkinter as tk

class CadastroAlunoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Aluno")
        
        # Crie rótulos e campos de entrada
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_sobrenome = tk.Label(root, text="Sobrenome:")
        self.label_data_nascimento = tk.Label(root, text="Data de Nascimento:")
        self.label_email = tk.Label(root, text="Email:")
        self.label_telefone = tk.Label(root, text="Telefone:")
        self.label_numero_matricula = tk.Label(root, text="Número de Matrícula:")
        
        self.entry_nome = tk.Entry(root)
        self.entry_sobrenome = tk.Entry(root)
        self.entry_data_nascimento = tk.Entry(root)
        self.entry_email = tk.Entry(root)
        self.entry_telefone = tk.Entry(root)
        self.entry_numero_matricula = tk.Entry(root)
        
        # Crie um botão para enviar o cadastro
        self.btn_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_aluno)
        
        # Organize os widgets na janela
        self.label_nome.pack()
        self.entry_nome.pack()
        self.label_sobrenome.pack()
        self.entry_sobrenome.pack()
        self.label_data_nascimento.pack()
        self.entry_data_nascimento.pack()
        self.label_email.pack()
        self.entry_email.pack()
        self.label_telefone.pack()
        self.entry_telefone.pack()
        self.label_numero_matricula.pack()
        self.entry_numero_matricula.pack()
        self.btn_cadastrar.pack()
    
    def cadastrar_aluno(self):
        # Obtenha os dados dos campos de entrada
        nome = self.entry_nome.get()
        sobrenome = self.entry_sobrenome.get()
        data_nascimento = self.entry_data_nascimento.get()
        email = self.entry_email.get()
        telefone = self.entry_telefone.get()
        numero_matricula = self.entry_numero_matricula.get()
        
        # Crie uma instância de Aluno com os dados
        aluno = Aluno(nome, sobrenome, data_nascimento, email, telefone, numero_matricula)
        
        # Faça algo com a instância do aluno (por exemplo, adicione-a ao banco de dados)
        # ...

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroAlunoApp(root)
    root.mainloop()
