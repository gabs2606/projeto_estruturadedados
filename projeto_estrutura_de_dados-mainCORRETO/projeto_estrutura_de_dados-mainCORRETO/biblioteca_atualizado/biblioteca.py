from collections import deque
from livro import livro as Livro
from usuario import usuario as Usuario
from devolucao import devolucao as Devolucao

class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista
        self.usuarios = []  # Lista
        self.historico_emprestimos = []  # Lista de tuplas
        self.livros_emprestados = set()  # Set
        self.reservas = {}  # Dicionário: isbn -> deque de usuários

    def cadastrar_livro(self, titulo, autor, isbn, faixa_etaria, quantidade, data):
        print("\n--- Cadastro de Livro ---")
        try:
            quantidade = int(quantidade)
            livro = Livro(titulo, autor, isbn, faixa_etaria, quantidade, data)
            self.livros.append(livro)
            self.reservas[isbn] = deque()
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def cadastrar_usuario(self, nome, idade, documento, telefone):
        print("\n--- Cadastro de Usuário ---")
        usuario = Usuario(nome, idade, documento, telefone)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso!")

    def emprestar_livro(self, nome_usuario, titulo_livro):
        print("\n--- Empréstimo de Livro ---")
        usuario = self.buscar_usuario_por_nome(nome_usuario)
        livro = self.buscar_livro_por_titulo(titulo_livro)

        if not usuario or not livro:
            print("Usuário ou livro não encontrado.")
            return

        if livro.disponivel:
            livro.disponivel = False
            self.livros_emprestados.add(livro.isbn)
            self.historico_emprestimos.append(("empréstimo", titulo_livro, nome_usuario))
            print(f"Livro '{titulo_livro}' emprestado para {nome_usuario}!")
        else:
            self.reservas[livro.isbn].append(nome_usuario)
            print(f"Livro indisponível. {nome_usuario} entrou na fila de espera.")

    def mostrar_historico(self):
        print("\n--- Histórico de Empréstimos ---")
        for registro in self.historico_emprestimos:
            print(f"{registro[0].upper()}: {registro[1]} -> {registro[2]}")

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower().strip() == titulo.lower().strip():
                return livro
        return None

    def buscar_usuario_por_nome(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower().strip() == nome.lower().strip():
                return usuario
        return None

    def editar_livro(self, titulo):
        livro = self.buscar_livro_por_titulo(titulo)
        if livro:
            print("Edite os dados do livro:")
            livro.titulo = input("Título: ")
            livro.autor = input("Autor: ")
            livro.isbn = input("ISBN: ")
            livro.faixa_etaria = input("Faixa Etária: ")
            livro.quantidade = int(input("Quantidade: "))
            print("Livro editado com sucesso!")
        else:
            print("Livro não encontrado.")

    def excluir_livro(self, titulo):
        livro = self.buscar_livro_por_titulo(titulo)
        if livro:
            self.livros.remove(livro)
            self.reservas.pop(livro.isbn, None)
            print("Livro excluído com sucesso!")
        else:
            print("Livro não encontrado.")

    def editar_usuario(self, nome):
        usuario = self.buscar_usuario_por_nome(nome)
        if usuario:
            print("Edite os dados do usuário:")
            usuario.nome = input("Nome: ")
            usuario.idade = int(input("Idade: "))
            usuario.documento = input("Documento: ")
            usuario.telefone = input("Telefone: ")
            print("Usuário editado com sucesso!")
        else:
            print("Usuário não encontrado.")

    def excluir_usuario(self, nome):
        usuario = self.buscar_usuario_por_nome(nome)
        if usuario:
            self.usuarios.remove(usuario)
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado.")

    def atender_fila_reserva(self, isbn):
        if isbn in self.reservas and self.reservas[isbn]:
            proximo_usuario = self.reservas[isbn].popleft()
            livro = next((livro for livro in self.livros if livro.isbn == isbn), None)
            if livro:
                print(f"Livro '{livro.titulo}' agora está disponível. Emprestando automaticamente para {proximo_usuario}.")
                self.emprestar_livro(proximo_usuario, livro.titulo)

def main():
    biblioteca = Biblioteca()
    controle_devolucao = Devolucao(biblioteca)

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Emprestar Livro")
        print("4. Ver Histórico")
        print("5. Devolver Livro")
        print("6. Buscar Livro")
        print("7. Buscar Usuário")
        print("8. Editar Livro")
        print("9. Excluir Livro")
        print("10. Editar Usuário")
        print("11. Excluir Usuário")
        print("12. Sair")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                titulo = input("Digite o título do Livro: ")
                autor = input("Digite o nome do autor: ")
                isbn = input("Digite o ISBN (13 dígitos): ")
                faixa_etaria = input("Digite a faixa etária: ")
                quantidade = input("Digite a quantidade: ")
                data = input("Digite a data (DD/MM/AAAA): ")
                biblioteca.cadastrar_livro(titulo, autor, isbn, faixa_etaria, quantidade, data)
            case "2":
                nome = input("Digite o nome: ")
                idade = int(input("Digite a idade: "))
                documento = input("Digite o CPF: ")
                telefone = input("Digite o telefone: ")
                biblioteca.cadastrar_usuario(nome, idade, documento, telefone)
            case "3":
                nome_usuario = input("Nome do usuário: ")
                titulo_livro = input("Título do livro: ")
                biblioteca.emprestar_livro(nome_usuario, titulo_livro)
            case "4":
                biblioteca.mostrar_historico()
            case "5":
                controle_devolucao.devolver_livro()
            case "6":
                titulo = input("Título do livro a buscar: ")
                livro = biblioteca.buscar_livro_por_titulo(titulo)
                if livro:
                    print("\n--- Livro Encontrado ---")
                    print(livro)
                else:
                    print("Livro não encontrado.")
            case "7":
                nome = input("Nome do usuário a buscar: ")
                usuario = biblioteca.buscar_usuario_por_nome(nome)
                if usuario:
                    print("\n--- Usuário Encontrado ---")
                    print(f"Nome: {usuario.nome}\nIdade: {usuario.idade}\nDocumento: {usuario.documento}\nTelefone: {usuario.telefone}")
                else:
                    print("Usuário não encontrado.")
            case "8":
                titulo = input("Título do livro a editar: ")
                biblioteca.editar_livro(titulo)
            case "9":
                titulo = input("Título do livro a excluir: ")
                biblioteca.excluir_livro(titulo)
            case "10":
                nome = input("Nome do usuário a editar: ")
                biblioteca.editar_usuario(nome)
            case "11":
                nome = input("Nome do usuário a excluir: ")
                biblioteca.excluir_usuario(nome)
            case "12":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
