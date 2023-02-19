from matplotlib import pyplot as plt

total = 0
dados = []
sexos = {"M": 0, "F": 0}
faixasEtarias = dict()
niveisColesterol = dict()

def parseFile():
    global total
    # Guardamos a informação do ficheiro em memória
    with open("myheart.csv", "r") as f:
        for line in f.readlines()[1:]:
            total += 1
            dados_pessoa = line[:-1].split(',')
            dados.append(dados_pessoa)

def set_sexos():
    # Calcula o numero de mulheres doentes e o numero de homens doentes
    for dado_pessoa in dados:
        if dado_pessoa[1] == 'F':
            if dado_pessoa[5] == '1':
                sexos['F'] += 1
        else:
            if dado_pessoa[5] == '1':
                sexos['M'] += 1

#Devolve a idade minima e a idade maxima presentes nos dados
def maxMinIdade():
    min = None
    max = None
    for dado_pessoa in dados:
        if min == None or int(dado_pessoa[0]) <= min: min = int(dado_pessoa[0])
        if max == None or int(dado_pessoa[0]) >= max: max = int(dado_pessoa[0])
    return min, max


def set_faixasEtarias():
    # Calculamos a minima e a maxima idade presente nos dados
    min,max = maxMinIdade()
    # Percorre-se uma lista que vai desde a idade minima até à idade maxima presente nos dados de 5 em 5
    # e inicializamos assim um dicionario com as faixas etárias possiveis para os dados que temos
    for idade in [x for x in range(min, max) if x % 5 == 0]:
        faixasEtarias[idade] = 0
    # Contabilizamos para cada faixa etária quantas pessoas doentes se encontram na mesma
        for dado_pessoa in dados:
            if idade <= int(dado_pessoa[0]) <= idade + 4:
                if dado_pessoa[5] == "1":
                    faixasEtarias[idade] += 1

#Devolve o nivel minimo e o nivel maximo de colesterol presentes nos dados
def maxMinColesterol():
    min = 0
    max = None
    for dado_pessoa in dados:
        if min == None or int(dado_pessoa[3]) <= min: min = int(dado_pessoa[3])
        if max == None or int(dado_pessoa[3]) >= max: max = int(dado_pessoa[3])
    return min, max

def set_niveisColesterol():
    # Calculamos o maximo e o minimo nivel de colesterol presente nos dados
    min,max = maxMinColesterol()
    # Percorre-se uma lista que vai desde o nivel minimo de colesterol até ao nivel maximo de colesterol presente nos dados de 10 em 10
    # e inicializamos assim um dicionario com os niveis de colesterol possiveis para os dados que temos
    for nivel in [x for x in range(min, max) if x % 10 == 0]:
        niveisColesterol[nivel] = 0
        # Contabilizamos para cada nivel de colesterol quantas pessoas doentes se encontram no mesmo
        for dado_pessoa in dados:
            if nivel <= int(dado_pessoa[3]) <= nivel + 9:
                if dado_pessoa[5] == '1':
                    niveisColesterol[nivel] += 1


def imprimeTabela(opcao, distrbuicao, x, y):
    for key, value in distrbuicao.items():
        perc = value / total * 100

        if opcao == 1:
            if key == 'M':
                s = "Masculino"
            else:
                s = "Feminino"
            print("{:<20}".format(s) + str(round(perc, 2)) + "%")
            x.append(key)
            y.append(perc)
        elif opcao == 2:
            print("{:<20}".format(str(key) + " - " + str(key + 4) + " anos") + str(round(perc, 2)) + "%")
            x.append(str(key)+"-"+str(key+4))
            y.append(perc)
        elif opcao == 3:
            print("{:<20}".format(str(key) + " - " + str(key + 9)) + str(round(perc, 2)) + "%")
            x.append(str(key)+"-"+str(key+9))
            y.append(perc)

def menu():
    # Fazemos o parse dos ficheiros
    parseFile()

    # Preenchemos os dicionários com a informação guardada
    set_sexos()
    set_faixasEtarias()
    set_niveisColesterol()

    print("1 - Percentagem de doentes por sexo")
    print("2 - Percentagem de doentes por faixa etária")
    print("3 - Percentagem de doentes por nível de colesterol")
    print("0 - Sair")
    print("\n")
    opcao = input("Qual a sua opção? ")
    print("\n")
    x = []
    y = []
    match opcao:
        case "1":
            # Header da tabela
            print("{:<20}TEM A DOENÇA".format('SEXO'))
            imprimeTabela(int(opcao), sexos, x, y)

        case "2":
            # Header da tabela
            print("{:<20}TEM A DOENÇA".format('FAIXA ETÁRIA'))
            imprimeTabela(int(opcao), faixasEtarias, x, y)

        case "3":
            # Header da tabela
            print("{:<20}TEM A DOENÇA".format('NÍVEL COLESTEROL'))
            imprimeTabela(int(opcao), niveisColesterol, x, y)

        case '0':
            print("Saindo...")

    if int(opcao) > 3 or int(opcao) < 0:
        print("Opção inválida!")
        menu()

    plt.plot(x, y, marker='o')
    plt.show()

menu()
