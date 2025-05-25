class devolucao:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def devolver_livro(self):
        print("\n--- Devolução de Livro ---")
        titulo_livro = input("Digite o título do livro que deseja devolver: ")
        
        usuario = self._buscar_ultimo_usuario_do_livro(titulo_livro)
        if not usuario:
            print("Nenhum empréstimo encontrado para este livro.")
            return

        livro = self.biblioteca.buscar_livro_por_titulo(titulo_livro)
        if not livro:
            print("Livro não encontrado na biblioteca.")
            return
        
        if livro.isbn in self.biblioteca.livros_emprestados:
            livro.disponivel = True
            self.biblioteca.livros_emprestados.remove(livro.isbn)
            self.biblioteca.historico_emprestimos.append(("devolução", titulo_livro, usuario))
            print(f"Livro '{titulo_livro}' devolvido por {usuario} com sucesso!")
            
            # Verifica se existe fila de espera para esse livro
            self.biblioteca.atender_fila_reserva(livro.isbn)
        else:
            print("Este livro não está registrado como emprestado.")

    def _buscar_ultimo_usuario_do_livro(self, titulo):
        # Percorre o histórico de trás para frente para encontrar o último empréstimo
        for registro in reversed(self.biblioteca.historico_emprestimos):
            # registro é uma tupla: (acao, livro, usuario)
            if registro[0] == "empréstimo" and registro[1].lower() == titulo.lower():
                return registro[2]
        return None
