class usuario:
    def __init__(self, nome, idade, documento, telefone):
        self.nome = nome
        self.idade = idade
        self.documento = documento
        self.telefone = telefone
        self.aprovado = idade >= 18
