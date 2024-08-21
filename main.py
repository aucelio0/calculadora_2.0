# funções
def mostar_menu():
    print('1- Somar')
    print('2- Subtrair')
    print('3- Multipilcar')
    print('4- Dividir')
    print('5- Extrair o resto da divisão')
    print('6- Potênciação')
    print('Outro valor - Sair do programa')
    
somar       = lambda x,y: x + y
subtrair    = lambda x,y: x - y
multiplicar = lambda x,y: x * y
dividir     = lambda x,y: x / y
resto       = lambda x,y: x % y
potenciacao = lambda x,y: x ** y

# programa principal
if __name__ == '__main__':
    while True:
        mostar_menu()
        try:
            opcao = int(input('Opção desejada: '))
            if opcao > 0 and opcao < 7:
                x = float(input('Informe o valor de x: ').replace(',', '.'))
                y = float(input('Informe o valor de y: ').replace(',', '.'))
                match opcao:
                    case 1:
                        print(f'A soma entre {x} e {y} é: {somar(x,y)}.')
                        continue
                    case 2:
                        print(f'A subtração entre {x} e {y} é: {subtrair(x,y)}.')
                        continue
                    case 3:
                        print(f'A multiplicação entre {x} e {y} é: {multiplicar(x,y)}.')
                        continue
                    case 4:
                        print(f'A divisão entre {x} e {y} é: {dividir(x,y)}.')
                        continue
                    case 5:
                        print(f'O resto da divisão entre {x} e {y} é: {resto(x,y)}.')
                        continue
                    case 6:
                        print(f'{x} elevado a {y} é: {potenciacao(x,y)}.')
                        continue
                    case _:
                        print('Opção inválida.')
                        continue
            else:
                print('Programa encerrado!')
                break
        except: 
            print('Não foi possível verificar a opção.')
            continuar = input('Deseja voltar ao programa? (s/n)').lower()
            if continuar == 's':
                continue
            else:
                break