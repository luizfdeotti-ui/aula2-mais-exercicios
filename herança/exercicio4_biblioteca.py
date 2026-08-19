class ItemBiblioteca:

    def __init__(self, titulo: str, codigo: int):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

class Livro(ItemBiblioteca):

    def __init__(self, titulo: str, codigo: int, autor: str, num_paginas: int):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas

class Usuario:

    def __init__(self, nome: str):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item: ItemBiblioteca):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)
            print(f"'{item.titulo}' foi emprestado com sucesso para {self.nome}!")
        else:
            print(f"Indisponível: O item '{item.titulo}' já está emprestado no momento.")

    def devolver_item(self, item: ItemBiblioteca):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f"✅ '{item.titulo}' foi devolvido com sucesso por {self.nome}!")
        else:
            print(f"O item '{item.titulo}' não está na lista de empréstimos de {self.nome}.")

    def ver_historico(self):
        print(f"\n=== HISTÓRICO DE: {self.nome} ---")
        if not self.itens_emprestados:
            print("Nenhum item em posse no momento.")
        else:
            for item in self.itens_emprestados:
                print(f"- {item.titulo} (Código: {item.codigo})")
        print("=" * 32)

livro1 = Livro("Dom Casmurro", 101, "Machado de Assis", 256)
livro2 = Livro("1984", 102, "George Orwell", 328)
user1 = Usuario("Luiz")
user2 = Usuario("Maria")

user1.pegar_item(livro1) 
user2.pegar_item(livro1)  
user1.ver_historico()
user1.devolver_item(livro1)
user2.pegar_item(livro1)  
user2.ver_historico()