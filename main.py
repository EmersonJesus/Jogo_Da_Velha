from lib.sistema import *

lista = ['JOGAR', 'SAIR']
while True:
    menu(lista)
    while True: 
        opcao = str(input('Deseja jogar de novo?[S/N]  ')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('OPÇÃO INVALIDA!')
    if opcao == 'N':
        print('SAINDO... VOLTE SEMPRE :)')
        break
