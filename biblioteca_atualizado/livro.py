class livro:
    def __init__(self, titulo, autor, isbn, faixa_etaria, quantidade, data):
        if len(str(isbn)) != 13:
            raise ValueError("ISBN deve ter 13 dígitos!")
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.faixa_etaria = faixa_etaria
        self.disponivel = True
        self.quantidade = int(quantidade)
        self.data = data

    def __str__(self):
        disponibilidade = "Disponível" if self.disponivel else "Indisponível"
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"ISBN: {self.isbn}\n"
            f"Faixa Etária: {self.faixa_etaria}\n"
            f"Quantidade: {self.quantidade}\n"
            f"Data: {self.data}\n"
            f"Status: {disponibilidade}"
        )
