class Devolucao:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def devolver_livro(self):
        print("\n--- Devolução de Livro ---")
        titulo_livro = input("Título do livro a devolver: ")

        livro = self.biblioteca.buscar_livro_por_titulo(titulo_livro)

        if not livro:
            print("Livro não encontrado.")
            return

        if livro.isbn not in self.biblioteca.livros_emprestados:
            print("Este livro não está emprestado.")
            return

        # Remove o livro do set de emprestados
        self.biblioteca.livros_emprestados.remove(livro.isbn)
        livro.disponivel = True

        usuario = self._buscar_ultimo_usuario_do_livro(titulo_livro)

        # Adiciona ao histórico de devolução
        self.biblioteca.historico_emprestimos.append({
            "acao": "devolução",
            "livro": titulo_livro,
            "usuario": usuario
        })

        print(f"Livro '{titulo_livro}' devolvido com sucesso por {usuario}.")

    def _buscar_ultimo_usuario_do_livro(self, titulo):
        for registro in reversed(self.biblioteca.historico_emprestimos):
            if registro["acao"] == "empréstimo" and registro["livro"].lower() == titulo.lower():
                return registro["usuario"]
        return "desconhecido"