# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples
# (canal, volume e liga/desliga)

from rich import print
from rich.panel import Panel


class ControleRemoto:
    """
    Cria um controle remoto que muda de canal, aumenta e diminui o volume, e liga e desliga a tv
    """
    canal_min = 1
    canal_max = 5
    volume_min = 1
    volume_max = 5


    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 1


    def mostrar_tv(self):

        if controle.ligada:

            conteudo = 'Canal  = '
            for i in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if i == self.canal:
                    conteudo += f'[yellow on yellow] {i} [/]'
                else:
                    conteudo += f' {i} '

            conteudo += '\nVolume = '
            for i in range(ControleRemoto.volume_min, ControleRemoto.volume_max+1):
                if i <= self.volume:
                    conteudo += '[black on cyan] [/]'
                else:
                    conteudo += '[black on white] [/]'

            estado_tv = Panel(conteudo, title="TV", width=30)

        else:
            estado_tv = Panel(f'🚫 [red]A TV está desligada[/]', title='[ TV ]', width=30)
        print('\n' * 5)
        print(estado_tv)


    def opcao_escolhida(self, opcao):

        if opcao == '@':
            controle.liga_desliga()
            self.mostrar_tv()

        elif opcao == "<" or opcao == ">":
            controle.mudar_de_canal(opcao)

        elif opcao == "-" or opcao == "+":
            controle.mudar_volume(opcao)
        else:
            print("[red]Opção inexistente[/]")


    def mudar_de_canal(self, comando):

        if self.ligada:
            if comando == ">":
                if self.canal < 5:
                    self.canal += 1
                else:
                    self.canal = ControleRemoto.canal_min
            elif comando == "<":
                if self.canal > 1:
                    self.canal -= 1
                else:
                    self.canal = ControleRemoto.canal_max


    def mudar_volume(self, comando):
        if self.ligada:
            if comando == "+":
                if self.volume < 5:
                    self.volume += 1
            elif comando == "-":
                if self.volume > 1:
                    self.volume -= 1


    def liga_desliga(self):
        self.ligada = not self.ligada


controle = ControleRemoto()

while True:
    controle.mostrar_tv()
    opcao = input(f'< CH{controle.canal} >      - VOL{controle.volume} + ')
    if opcao == '0':
        break
    else:
        controle.opcao_escolhida(opcao)