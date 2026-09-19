COR_FUNDO = dict(
        branco=';107',
        preto=';40',
        vermelho=';41',
        verde=';42',
        amarelo=';43',
        azul=';44',
        magenta=';45',
        ciano=';46',
        cinza_claro=';47',
        cinza_escuro=';100',
        vermelho_claro=';101',
        verde_claro=';102',
        amarelo_claro=';103',
        azul_claro=';104',
        magenta_claro=';105',
        ciano_claro=';106',
        transparente=''
    )

COR_TEXTO = dict(
    preto='30',
    vermelho='31',
    verde='32',
    amarelo='33',
    azul='34',
    magenta='35',
    ciano='36',
    cinza_claro='37',
    cinza_escuro='90',
    vermelho_claro='91',
    verde_claro='92',
    amarelo_claro='93',
    azul_claro='94',
    magenta_claro='95',
    ciano_claro='96',
    branco='97',
    transparente=''
)

ESTILOS = dict(
    reset='0',
    negrito=';1',
    fraco=';2',
    italico=';3',
    sublinhado=';4',
    piscante=';5',
    piscante_rapido=';6',
    invertido=';7',
    oculto=';8',
    riscado=';9',
    sem_estilo=''
)

TIPOS_MENSAGEM = {
    'sucesso': {
        'cor': 'verde',
        'fundo': 'transparente',
        'estilo': 'negrito'
    },

    'erro': {
        'cor': 'branco',
        'fundo': 'vermelho',
        'estilo': 'negrito'
    },

    'aviso': {
        'cor': 'amarelo',
        'fundo': 'transparente',
        'estilo': 'negrito'
    },

    'notificacao': {
        'cor': 'ciano',
        'fundo': 'transparente',
        'estilo': 'sem_estilo'
    },

    'informacao': {
        'cor': 'azul',
        'fundo': 'transparente',
        'estilo': 'sem_estilo'
    },

    'pergunta': {
        'cor': 'ciano',
        'fundo': 'transparente',
        'estilo': 'negrito'
    },

    'destaque': {
        'cor': 'preto',
        'fundo': 'amarelo',
        'estilo': 'negrito'
    },

    'critico': {
        'cor': 'branco',
        'fundo': 'vermelho',
        'estilo': 'negrito'
    },

    'processando': {
        'cor': 'ciano',
        'fundo': 'transparente',
        'estilo': 'piscante'
    },

    'entrada': {
        'cor': 'verde_claro',
        'fundo': 'transparente',
        'estilo': 'negrito'
    }
}


def print_formatado(texto='', *cores, fundo='transparente', estilo='sem_estilo', tipo='', sep=" ", end="\n",
                    caractere=False, palavras=False):

    """
    Exibe um texto no terminal utilizando cores, cores de fundo e estilos ANSI.

    A função permite imprimir textos utilizando uma ou várias cores, aplicar
    uma cor de fundo, um estilo de formatação e definir tipos de mensagens
    predefinidos.

    As cores podem ser aplicadas ao texto inteiro ou distribuídas
    automaticamente entre caracteres, ou palavras.

    Args:
        texto (str):
            Texto que será exibido no terminal.

            Padrão: ''.

        *cores (str):
            Uma ou mais cores utilizadas na formatação do texto.

            As cores devem ser informadas utilizando os nomes definidos
            no dicionário COR_TEXTO.

            Opções disponíveis:
                - 'preto'
                - 'vermelho'
                - 'verde'
                - 'amarelo'
                - 'azul'
                - 'magenta'
                - 'ciano'
                - 'cinza_claro'
                - 'cinza_escuro'
                - 'vermelho_claro'
                - 'verde_claro'
                - 'amarelo_claro'
                - 'azul_claro'
                - 'magenta_claro'
                - 'ciano_claro'
                - 'branco'
                - 'transparente'

            Quando mais de uma cor é informada, elas são utilizadas em
            sequência. Ao chegar ao final da sequência, ela é reiniciada.

            Exemplos:
                print_colorido('Olá mundo', 'azul', 'verde')
                print_colorido('Python', 'vermelho', 'amarelo', 'azul')

            Quando nenhuma cor é informada:
                - no modo normal, utiliza 'transparente';
                - nos modos caractere ou palavras, utiliza automaticamente
                  as cores disponíveis em COR_TEXTO;
                - quando tipo é informado, utiliza a cor definida para
                  aquele tipo de mensagem.

            Padrão: nenhuma cor.

        fundo (str):
            Define a cor de fundo utilizada na impressão.

            Opções disponíveis:
                - 'branco'
                - 'preto'
                - 'vermelho'
                - 'verde'
                - 'amarelo'
                - 'azul'
                - 'magenta'
                - 'ciano'
                - 'cinza_claro'
                - 'cinza_escuro'
                - 'vermelho_claro'
                - 'verde_claro'
                - 'amarelo_claro'
                - 'azul_claro'
                - 'magenta_claro'
                - 'ciano_claro'
                - 'transparente'

            Quando tipo é informado, o valor de fundo é substituído pelo
            fundo definido para o tipo de mensagem.

            Padrão: 'transparente'.

        estilo (str):
            Define o estilo aplicado ao texto.

            Opções disponíveis:
                - 'reset' — redefine os atributos de formatação.
                - 'negrito' — aplica negrito.
                - 'fraco' — reduz a intensidade do texto.
                - 'italico' — aplica itálico.
                - 'sublinhado' — aplica sublinhado.
                - 'piscante' — faz o texto piscar.
                - 'piscante_rapido' — faz o texto piscar rapidamente.
                - 'invertido' — inverte as cores do texto e do fundo.
                - 'oculto' — oculta o texto.
                - 'riscado' — aplica efeito de texto riscado.
                - 'sem_estilo' — não aplica nenhum estilo.

            Quando tipo é informado, o valor de estilo é substituído pelo
            estilo definido para o tipo de mensagem.

            Padrão: 'sem_estilo'.

        tipo (str):
            Define um tipo de mensagem predefinido.

            Os tipos disponíveis são definidos no dicionário
            TIPOS_MENSAGEM:

                - 'sucesso' — indica que uma operação foi concluída.
                - 'erro' — indica que ocorreu um erro.
                - 'aviso' — chama atenção para uma situação.
                - 'notificacao' — exibe uma notificação.
                - 'informacao' — exibe uma informação.
                - 'pergunta' — apresenta uma pergunta ao usuário.
                - 'destaque' — destaca uma informação importante.
                - 'critico' — indica uma situação grave.
                - 'processando' — indica que uma operação está em andamento.
                - 'entrada' — indica que o programa aguarda uma entrada.

            Ao utilizar tipo, a função obtém automaticamente do dicionário
            TIPOS_MENSAGEM a cor, o fundo e o estilo correspondentes.

            O tipo de mensagem é utilizado somente quando caractere=False
            e palavras=False.

            Padrão: ''.

        sep (str):
            Define o separador utilizado entre os elementos impressos.

            Padrão: ' '.

        end (str):
            Define o que será impresso ao final do texto.

            Padrão: '\n'.

        caractere (bool):
            Se True, cada caractere do texto recebe uma cor.

            Se forem informadas várias cores em *cores, elas serão utilizadas
            em sequência e reiniciadas quando todas forem utilizadas.

            Se nenhuma cor for informada, a função utiliza automaticamente
            as cores disponíveis em COR_TEXTO.

            Quando caractere=True, esse modo possui prioridade sobre
            palavras=True e tipo.

            Padrão: False.

        palavras (bool):
            Se True, cada palavra do texto recebe uma cor.

            Se forem informadas várias cores em *cores, elas serão utilizadas
            em sequência e reiniciadas quando todas forem utilizadas.

            Se nenhuma cor for informada, a função utiliza automaticamente
            as cores disponíveis em COR_TEXTO.

            Quando caractere=True e palavras=True, o modo caractere possui
            prioridade.

            Quando caractere=False e palavras=True, o tipo de mensagem não
            é utilizado.

            Padrão: False.

    Observações:
        - As cores do texto são definidas pelo dicionário COR_TEXTO.
        - As cores de fundo são definidas pelo dicionário COR_FUNDO.
        - Os estilos são definidos pelo dicionário ESTILOS.
        - Os tipos de mensagem são definidos pelo dicionário TIPOS_MENSAGEM.
        - O operador % é utilizado para repetir a sequência de cores.
        - Quando caractere=True, a distribuição das cores ocorre caractere
          por caractere.
        - Quando palavras=True, a distribuição das cores ocorre palavra
          por palavra.
        - Quando caractere=False e palavras=False, as cores são aplicadas
          às palavras do texto.
        - Quando nenhuma cor é informada no modo normal, utiliza
          'transparente'.
        - Quando caractere=True e palavras=True simultaneamente, o modo
          caractere possui prioridade.
        - Quando caractere=False e palavras=False e tipo é informado, a
          função utiliza a configuração correspondente em TIPOS_MENSAGEM.
        - O método split() é utilizado para separar as palavras. Por isso,
          múltiplos espaços, quebras de linha e outras formas de espaçamento
          não são preservados no modo palavras.
        - Caso seja informada uma cor, fundo, estilo ou tipo inexistente,
          a função exibe uma mensagem de erro no terminal.

    Examples:
        >>> print_formatado('Olá mundo')
        >>> print_formatado('Olá mundo', 'verde')
        >>> print_formatado('Olá mundo', 'azul', 'verde')
        >>> print_formatado(
        ...     'Aviso!',
        ...     'vermelho',
        ...     fundo='amarelo',
        ...     estilo='negrito'
        ... )
        >>> print_formatado('Python', 'azul', 'verde', caractere=True)
        >>> print_formatado(
        ...     'Olá mundo Python',
        ...     'azul',
        ...     'verde',
        ...     palavras=True
        ... )
        >>> print_formatado('Python', 'azul', 'verde', palavras=True, sep=' | ')
        >>> print_formatado('Arquivo salvo!', tipo='sucesso')
        >>> print_formatado('Arquivo não encontrado!', tipo='erro')
        >>> print_formatado('Processando...', tipo='processando')
        >>> print_formatado('Digite seu nome:', tipo='entrada')
    """

    try:
        if not type(texto) is str:
            texto = str(texto)

        lista_palavras = texto.split()

        # Cada caractere ou palavra recebe uma cor
        if caractere or palavras:
            if len(cores) == 0:
                cores = list(COR_TEXTO.keys())


        elif tipo:
            cores = [TIPOS_MENSAGEM[tipo]['cor']]
            fundo = TIPOS_MENSAGEM[tipo]['fundo']
            estilo = TIPOS_MENSAGEM[tipo]['estilo']

        # Texto normal
        else:
            if len(cores) == 0:
                cores = ['transparente']

        for i, palavra in enumerate(lista_palavras if not caractere else texto):
            cor_atual = i % len(cores)

            print(
                    f'\033[{COR_TEXTO[cores[cor_atual]]}{COR_FUNDO[fundo]}{ESTILOS[estilo]}m'
                    f'{palavra}',
                    end='' if caractere else sep if i < len(lista_palavras)-1 else ' '
            )
        print('\033[m', end=end)

    except KeyError:
        print(
            f'\033[{COR_TEXTO["branco"]}{COR_FUNDO["vermelho"]}{ESTILOS["negrito"]}m'
            'ERRO! opção de cor do texto, fundo ou estilo inválida!\033[m'
        )


def entrada_personalizada(legenda=''):
   return input(f'\033[{COR_TEXTO["verde_claro"]}{ESTILOS["negrito"]}m{legenda}\033[m')