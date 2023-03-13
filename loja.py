camisas = ["Camisa Branca", "Camisa Verde","Camisa Laranja","Camisa Polo Vermelha", "Camisa Social Azul", "Camisa Xadrez Amarela"]
calcas = ["Calça Beje","Calça Jeans","Calça Rosa","Calça jeans azul", "Calça social preta", "Calça legging cinza", "Calça moletom verde", "Calça cargo marrom"]
blusas = ["Blusa Verde", "Blusa Azul""Blusa cropped amarela",  "Blusa manga longa verde", "Blusa ciganinha branca com flores", "T-shirt cinza"]
espaco = '-'*20
total = []
valores = []
def main():
    while True:
        esc = int(input('''Escolha um dos produtos:
[1]camisas
[2]calças
[3]blusas
:'''))
        if(esc == 1):
            return 1
            break
        elif(esc == 2):
            return 2
            break
        elif(esc == 3):
            return 3
            break
        else:
            print(espaco,'\nOpção inválida\n',espaco)
def esc1():
    esc = main()
    while True:
        if(esc == 1):
            print(espaco)
            for i in range(len(camisas)):
                print(f'[{i}]{camisas[i]}')
                maxi = i
            print(espaco)
            resp = camisas
        elif(esc == 2):
            print(espaco)
            for i in range(len(calcas)):
                print(f'[{i}]{calcas[i]}')
                maxi = i
            print(espaco)
            resp = calcas
        elif(esc == 3):
            print(espaco)
            for i in range(len(blusas)):
                print(f'[{i}]{blusas[i]}')
                maxi = i
            print(espaco)
            resp = blusas
        escolha = int(input(f"Qual Escolha?: "))
        if(escolha <= maxi and escolha >= 0):
            print(f'{resp[escolha]} foi adicionado ao seu carrinho\n{espaco}')
            return (maxi,resp,escolha)
        else:
            print(espaco, '\nOpção inválida')
def esc2():
    resp = esc1()
    while True:
        pergunta = int(input(f'''Deseja algo mais?: 
[1]Outra(s) {resp[1][resp[2]]}.
[2]Outra roupa.
[3]Não, quero pagar.
:'''))
        if(pergunta == 1):
            quantidade = int(input(f'{espaco}\nQual a quantidade: '))
            objeto = (resp[1][resp[2]])
            return (objeto, 1, quantidade)
            break
        elif(pergunta == 2):
            objeto = (resp[1][resp[2]])
            return (objeto, 2)
            break
        elif(pergunta == 3):
            objeto = (resp[1][resp[2]])
            return (objeto, 3)
            break
        else:
            print(espaco, '\nOpção inválida\n', espaco)
def compra():
    resp = esc2()
    total.append(resp[0])
    pergunta = resp[1]
    while True:
        if(pergunta == 1):
            per2 = input(f'{espaco}\nQuer algo mais \n [s]Sim ou [n]Não \n:').lower()
            if (per2 == 's'):
                for n in range(resp[2]-1):
                    total.append(resp[0])
                pagamento()
                break
            elif (per2 == 'n'):
                for n in range(resp[2]-1):
                    total.append(resp[0])
                return total
                break
            else:
                print(espaco, '\nOpção inválida\n', espaco)
        elif(pergunta == 2):
            print(espaco)
            pagamento()
            break
        elif(pergunta == 3):
            return total
            break
        else:
            print(espaco, '\nOpção inválida\n', espaco)
def pagamento():
    compras = compra()

    for com in compras:
        if com in camisas:
            valores.append(80)
            print(f'{espaco}\n{com} R$ 70.00')
        elif com in blusas:
            valores.append(200)
            print(f'{espaco}\n{com} R$ 120.00')
        elif com in calcas:
            valores.append(140)
            print(f'{espaco}\n{com} R$ 100.00')
    while True:
        per = input(f'{espaco}\nTem certeza que só quer estes itens?: \n [s]Sim ou [n]Não \n:').lower()
        if(per == 's'):
            conta = sum(valores)
            print(f'{espaco}\nO valor total é de: R$ {conta:.2f}\n{espaco}')
            exit()
        elif(per == 'n'):
            print(espaco,'\n Adcione mais itens:\n',espaco)
            pagamento()
        else:
            print(espaco, '\nOpção inválida\n', espaco)
pagamento()