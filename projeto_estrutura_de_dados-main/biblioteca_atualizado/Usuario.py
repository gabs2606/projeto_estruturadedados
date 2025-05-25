class Usuario:
    def __init__(self, nome, idade, documento, telefone):
        self.nome = nome
        self.idade = idade
        self.documento = documento
        self.telefone = telefone
        self.aprovado = idade >= 18  # Aprovação automática se maior de 18 anos