import os

def leiaInt(msg):
    """Função que lê um número inteiro digitado pelo úsuario"""
    valor = 0
    while True:
        n = input(msg).strip()
        try:
            valor = int(n)
            break
        except (TypeError, ValueError):
            print('ERRO! Digite um número válido.')
        except KeyboardInterrupt:
            print('Entrada interrompida pelo usuario')
            return 0
    return valor

def linha(tam=42):
    """Função que desenha uma linha na tela, usada para criar a interface para úsuario"""
    return f'='*tam

def mensagem(msg):
    """Função que mostra uma mensagem na tela"""
    print(f'{msg}'.center(42))
     
def menu(lista):
    """Função que mostra um menu na tela"""
    while True:
        print(linha())
        mensagem('JOGO DA VELHA')
        print(linha())
        c = 1
        for item in lista:
            print(f'{c:>17} - {item}')
            c += 1
        print(linha())
        opc = leiaInt('Sua opção: ')
        match opc:
            case 1:
                jogo()
                break
            case 2:
                mensagem('Saindo do Programa...')
                break
            case _:
                mensagem('Opção Inválida!')

def desenhatab(tabuleiro):
    """Função que desenha o tabuleiro na tela"""
    os.system('clear' if os.name == 'posix' else 'cls')
    print("┌───┬───┬───┐".center(42))
    print(f"│ {tabuleiro['7']} │ {tabuleiro['8']} │ {tabuleiro['9']} │".center(42))
    print("├───┼───┼───┤".center(42))
    print(f"│ {tabuleiro['4']} │ {tabuleiro['5']} │ {tabuleiro['6']} │".center(42))
    print("├───┼───┼───┤".center(42))
    print(f"│ {tabuleiro['1']} │ {tabuleiro['2']} │ {tabuleiro['3']} │".center(42))
    print("└───┴───┴───┘".center(42))

def jogo():
    """Função principal do jogo"""
    cont = 0
    estadojogo = False
    tabuleiro = {
        '7': '7', '8': '8', '9': '9',
        '4': '4', '5': '5', '6': '6',
        '1': '1', '2': '2', '3': '3',
    }
    desenhatab(tabuleiro)
    vez = 1
    while not estadojogo:
        vez = ((vez+1)%2)
        jogada(tabuleiro, vez)
        cont += 1
        desenhatab(tabuleiro)
        estadojogo = verificajogo(tabuleiro)
    
def verificajogo(tabuleiro):
    """Função que se o jogo acabou"""
    combinacoes_vitoria = [
        ('7', '8', '9'), ('4', '5', '6'), ('1', '2', '3'),
        ('7', '4', '1'), ('8', '5', '2'), ('9', '6', '3'),
        ('7', '5', '3'), ('9', '5', '1')
    ]

    for comb in combinacoes_vitoria:
        a, b, c = comb
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            if tabuleiro[a] == 'X' or tabuleiro[a] == 'O':
                print(f'O JOGADOR {tabuleiro[a]} GANHOU!')
            return True

    if all(val == 'X' or val == 'O' for val in tabuleiro.values()):
        print('DEU VELHA!')
        return True

    return False

def jogada(tabuleiro, vez):
    """Função que faz a jogado dos jogadores e verifica se a posição está vazia"""
    if vez == 0:
        jogada = 'X'
    else:
        jogada = 'O'
        
    while True:
        try:
            posicao = int(input(f'Jogador {jogada}, escolha uma posição (1-9): '))
            if 1 <= posicao <= 9:
                if tabuleiro[str(posicao)] != 'X' and tabuleiro[str(posicao)] != 'O':
                    tabuleiro[str(posicao)] = jogada
                    break
                else:
                    print('Essa posição já está ocupada. Escolha outra.')
            else:
                print('Posição inválida. Escolha uma posição de 1 a 9.')
        except ValueError:
            print('Entrada inválida. Digite um número de 1 a 9.')
    return vez