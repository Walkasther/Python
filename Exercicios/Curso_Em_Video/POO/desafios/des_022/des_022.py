# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples
# (canal, volume e liga/desliga)

from rich import print
from rich.panel import Panel


class ControleRemoto:
    """
    Cria um controle remoto que muda de canal, aumenta e diminui o volume, e liga e desliga a tv
    """
    def __init__(self):
        self.ligada = 'desligada'
        self.canal = 1
        self.volume = 1


    def mudar_de_canal(self, comando):

        if comando == ">":
            if self.canal < 5:
                self.canal += 1
            else:
                self.canal = 1
        elif comando == "<":
            if self.canal > 1:
                self.canal -= 1
            else:
                self.canal = 5


    def mudar_volume(self, comando):
        if comando == "+":
            if self.volume < 5:
                self.volume += 1
        elif comando == "-":
            if self.volume > 1:
                self.volume -= 1


    def liga_desliga(self):
        self.ligada = "ligada" if self.ligada == 'desligada' else 'desligada'

controle = ControleRemoto()
cores = ['', '', '', '', '']
volume_atual = ' '
volume_total = '    '

while True:
    if controle.ligada == 'ligada':
        if controle.canal == 1:
            cores= ['yellow', '', '', '', '']
        if controle.canal == 2:
            cores = ['', 'yellow', '', '', '']
        if controle.canal == 3:
            cores = ['', '', 'yellow', '', '']
        if controle.canal == 4:
            cores = ['', '', '', 'yellow', '']
        if controle.canal == 5:
            cores = ['', '', '', '', 'yellow']

        if controle.volume == 1:
            volume_atual = " "
            volume_total = '    '
        elif controle.volume == 2:
            volume_atual = "  "
            volume_total = '   '
        elif controle.volume == 3:
            volume_atual = "   "
            volume_total = '  '
        elif controle.volume == 4:
            volume_atual = "    "
            volume_total = ' '
        elif controle.volume == 5:
            volume_atual = "     "
            volume_total = ''

        print('\n' * 5)

        estado_tv = Panel(f'CANAL  = [on {cores[0]}] 1 [/] [on {cores[1]}] 2 [/] [on {cores[2]}] 3 [/] [on {cores[3]}] 4 [/] [on {cores[4]}] 5 [/]'
                                     f'\nVOLUME = [on gray62][on blue]{volume_atual}[/]{volume_total}[/]', title="TV", width=35)
    else:
        estado_tv = Panel(f'🚫 [red]A TV está {controle.ligada}[/]', title='[ TV ]', width=30)


    print(estado_tv)

    opcao = input(f'< CH{controle.canal} >      - VOL{controle.volume} + ')

    if opcao == '@':
        controle.liga_desliga()

    elif opcao == "<" or opcao == ">":
        controle.mudar_de_canal(opcao)

    elif opcao == "-" or opcao == "+":
        controle.mudar_volume(opcao)

    elif opcao == "0":
        break
    else:
        print("[red]Opção inexistente[/]")
