# Crie uma classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie também um método que permita mostrar a ficha desse gamer.

from rich import print

class Gamer:
    """
    Cadastra nome, nick e jogos favoritos de uma pessoa, e permite também exibir a ficha desse gamer
    """
    def __init__(self, nome, nick):

        self.nome = nome
        self.nick = nick
        self.jogos = []


    def add_favoritos(self,jogo):
        self.jogos.append(jogo)

    def ficha(self):
        from rich.panel import Panel
        jogos = '\n🎮 '.join(sorted(self.jogos))
        f = Panel(f"Nome real: [black on blue] {self.nome} [/]"
                  f"\nJogos favoritos:"
                  f"\n🎮 [blue]{jogos}[/]", title=f'Jogador <{self.nick}>', width=40)

        print(f)


j1 = Gamer("Fabricio da Silva", "Detonador2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olivia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bross")
j2.add_favoritos("Call of Duty")
j2.ficha()