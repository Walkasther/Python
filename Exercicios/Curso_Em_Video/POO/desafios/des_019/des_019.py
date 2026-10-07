# Crie uma classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou
# ao fim da leitura.

from rich import print

class Livro:
    """
    cadastra um livro e o número de páginas, e folheia até o final
    """
    def __init__(self, titulo, paginas):
        self.titulo =  titulo
        self.paginas = paginas
        self.paginas_restantes = paginas
        self.pagina_atual = 1

        print(f"📖 [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' "
              f"que tem [green]{self.paginas} páginas[/] no total. "
              f"Você agora está na [yellow]página {self.pagina_atual}[/][/]")

    def avancar_paginas(self, quantidade):
        from time import sleep

        tira_pagina = self.paginas_restantes - quantidade
        cont = 0

        if tira_pagina >=1:
            while self.paginas_restantes > tira_pagina:

                sleep(0.2)
                self.pagina_atual += 1
                self.paginas_restantes -= 1
                print(f'Pág{self.pagina_atual} ▶', end=' ')

            print(f'[blue]Você avançou {quantidade} páginas e agora está na [yellow]página {self.pagina_atual}[/]')

        else:

            while self.paginas_restantes > 1:

                sleep(0.2)
                self.pagina_atual += 1
                self.paginas_restantes -= 1
                cont +=1

                print(f'Pág{self.pagina_atual} ▶', end=' ')

            print(f'[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/]')
            print(f"🚨 [red]Você chegou ao final do livro '{self.titulo}'")


l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(20)
l1.avancar_paginas(10)
l1.avancar_paginas(5)

