import Livro
import Usuario
from Devolucao import Devolucao
from collections import deque

class Biblioteca:
    def __init__(self):
        self.livros = [] 
        self.usuarios = [] 
        self.historico_emprestimos = []  
        self.livros_emprestados = set() 

    def cadastrar_livro(self, titulo, autor, isbn, faixa_etaria, quantidade):
        print("\n--- Cadastro de Livro ---")
        try:
            livro = Livro.Livro(titulo, autor, isbn, faixa_etaria, quantidade)
            self.livros.append(livro)
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def cadastrar_usuario(self, nome, idade, documento, telefone):
        print("\n--- Cadastro de Usuário ---")
        usuario = Usuario.Usuario(nome, idade, documento, telefone)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso!")
    
    def emprestar_livro(self, nome_usuario, titulo_livro):
        print("\n--- Empréstimo de Livro ---")
        usuario_encontrado = self.buscar_usuario_por_nome(nome_usuario)
        livro_encontrado = self.buscar_livro_por_titulo(titulo_livro)

        if usuario_encontrado and livro_encontrado:
            if livro_encontrado.disponivel:
                livro_encontrado.disponivel = False
                self.livros_emprestados.add(livro_encontrado.isbn)  #Armazena ISBN no SET
                self.historico_emprestimos.append({
                    "acao": "empréstimo",
                    "livro": titulo_livro,
                    "usuario": nome_usuario
                })
                print(f"Livro '{titulo_livro}' emprestado para {nome_usuario}!")
            else:
                print("Livro indisponível.")
        else:
            print("Usuário ou livro não encontrado.")
            
             
    def mostrar_historico(self):
        print("\n--- Histórico de Empréstimos ---")
        for registro in self.historico_emprestimos:
            print(f"{registro['acao'].upper()}: {registro['livro']} está com -> {registro['usuario']}")    
            
            

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
            livro.quantidade = input("Quantidade: ")
            print("Livro editado com sucesso!")
        else:
            print("Livro não encontrado.")

    def excluir_livro(self, titulo):
        livro = self.buscar_livro_por_titulo(titulo)
        if livro:
            self.livros.remove(livro)
            print("Livro excluído com sucesso!")
        else:
            print("Livro não encontrado.")

    def editar_usuario(self, nome):
        usuario = self.buscar_usuario_por_nome(nome)
        if usuario:
            print("Edite os dados do usuário:")
            usuario.nome = input("Nome: ")
            usuario.idade = input("Idade: ")
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


    #def __init__(self):
     #   reserva_de_livros = deque()
      #  reserva_de_livros.append("Gabriel")
       # reserva_de_livros.append("Gustavo")
        #reserva_de_livros.append("Gabriela")
        #proximo_usuario = reserva_de_livros.popleft()
        #print("O próximo usuario a receber é: {proximo_usuario}")
            
                   
            


# Função principal com menu
def main():
    biblioteca = Biblioteca()
    devolucao = Devolucao(biblioteca)
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Emprestar Livro")
        print("4. Ver Histórico")
        print("5. Devolver Livro")
        print("6. Buscar Livro")
        print("7. Buscar Usuario")
        print("8. Editar Livro")
        print("9. Excluir Livro")
        print("10. Editar Usuário")
        print("11. Excluir Usuário")
        print("12. Sair")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                titulo = input("Digite o titulo do Livro: ")
                autor = input("Digite o nome do autor: ")
                isbn = input("Digite o isbn (APENAS 13 DIGITOS): ")
                faixa_etaria = input("Digite a faixa etaria da categoria do livro: ")
                quantidade = input("Digite a quantidade de exemplares:")
                biblioteca.cadastrar_livro(titulo, autor, isbn, faixa_etaria, quantidade)
            case "2":
                nome = input("Digite um nome:")
                idade = int(input("Digite uma idade:"))
                documento = input("Digite seu CPF:")
                telefone = input("Digite seu número com DDD:")
                biblioteca.cadastrar_usuario(nome, idade, documento, telefone)

            case "3":
                nome_usuario = input("Nome do usuário: ")
                titulo_livro = input("Título do livro: ")
                biblioteca.emprestar_livro(nome_usuario, titulo_livro)
            case "4":
                biblioteca.mostrar_historico()
            case "5":
                devolucao.devolver_livro()
            case "6":
                titulo_livro = input("Digite o título do livro a buscar: ")
                livro = biblioteca.buscar_livro_por_titulo(titulo_livro)
                if livro:
                    print("\n--- Livro Encontrado ---")
                    print(livro)
                else:
                    print("Livro não encontrado")
            case "7":
                nome_usuario = input("Digite o nome do usuário a buscar: ")
                usuario = biblioteca.buscar_usuario_por_nome(nome_usuario)
                if usuario:
                    print("\n--- Usuário Encontrado ---")
                    print(f"Nome: {usuario.nome}")
                    print(f"Idade: {usuario.idade}")
                    print(f"Documento: {usuario.documento}")
                    print(f"Telefone: {usuario.telefone}")
                else:
                    print("Usuário não encontrado")
            case "8":
                titulo = input("Digite o título do livro a editar: ")
                biblioteca.editar_livro(titulo)
            case "9":
                titulo = input("Digite o título do livro a excluir: ")
                biblioteca.excluir_livro(titulo)
            case "10":
                nome = input("Digite o nome do usuário a editar: ")
                biblioteca.editar_usuario(nome)
            case "11":
                nome = input("Digite o nome do usuário a excluir: ")
                biblioteca.excluir_usuario(nome)
            case "12":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
