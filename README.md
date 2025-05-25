# Projeto Biblioteca

*Sistema de Biblioteca*
INTEGRANTES: Gabriel Veloso Barbosa(RA:1990821), Gabriela dos Santos de Lima(RA:2014108), Gustavo Lima dos Santos (RA:1992035), Luigi Gabriel da Silva Lima(RA:2009016).

Descrição principal: é um sistema CLI, desenvolvido em python, utlizando-se de estruturas de dados aprendidas em sala. O sistema consiste em permitir que se cadastre livros e usuários, que usuários possam emprestar e devolver livros, é possível visualziar o histórico de empréstimos e buscar e editar livros e usuários!

# Funcionalidades:
- Cadastro de livros e usuários
- Empréstimo de livros
- Devolução de livros
- Visualização do histórico de empréstimos
- Busca de livros e usuários
- Edição e exclusão de livros e usuários

# Tecnologias utilizadas:
Para executar o sistema, você precisará ter o Python instalado 3.0 e para executar pode se utilizar uma IDE como visual studio code.

#Estrutura de dados:
- Listas: Utilizadas para armazenar os livros e usuários cadastrados, bem como o histórico de empréstimos.
- Set: Utilizado para armazenar os ISBNs dos livros emprestados.
- Dicionário: Utilizado para armazenar as reservas de livros, onde a chave é o ISBN do livro e o valor é uma fila (deque) de usuários.
- Fila (Deque): Utilizada para implementar a fila de espera para os livros reservados.
- Tuplas: Utilizadas para armazenar os registros do histórico de empréstimos, contendo informações como a ação (empréstimo ou devolução), o título do livro e o nome do usuário.

