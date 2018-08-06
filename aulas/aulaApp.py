
nomes = []
def addnome():
    print("Digite o nome")
    nome = input()
    nomes.append(nome)

def listarNomes():
    print('Listando Nomes')
    for nome in nomes:
        print(nome)


def menu():
    escolha = ''
    while(escolha != '0'):
        print("Escolha Função - 1 cadastrar - 2 mostrar nomes - 0 para sair")
        escolha = input()

        if(escolha == '1'):
            addnome()
        if(escolha == '2'):
            listarNomes()

menu()