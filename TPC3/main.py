import collections
import re
import json

f = open("TPC3/processos.txt","r")
dataset = f.readlines()
texto = ''.join(dataset)

# Devolve o numero de processos de determinado ano
def procAno(ano):
    res = len(re.findall(rf"::{ano}-",texto))
    return res

# Devolve a frequencia de nomes proprios de determinados seculos 
def procSec(sec):
    match_sec = []  
    freqProprios = {}
    freqApelidos = {}

    # Procurar as entradas que correspondem a um determinado século
    for line in dataset:
        if (re.search(rf"::{sec-1}[0-9][0-9]-", line)):
            match_sec.append(line)

    # Determinar a frequência de nomes para cada entrada de um determinado século
    for line in match_sec:
        dados = re.split(r'::', line[:-1])
        if len(dados) > 1:
            nome = re.split(r' ', dados[2])

            # Armazena os nomes próprios
            if nome[0] not in freqProprios.keys():
                freqProprios[nome[0]] = 1
            else:
                freqProprios[nome[0]] += 1

            # Armazena os apelidos
            if nome[len(nome) - 1] not in freqApelidos.keys():
                freqApelidos[nome[len(nome) - 1]] = 1
            else:
                freqApelidos[nome[len(nome) - 1]] += 1

    #Ordena os dicionarios com base na frequencia dos nomes 
    sorted_proprio = dict(sorted(freqProprios.items(), key=lambda item: item[1], reverse=True))

    sorted_apelido = dict(sorted(freqApelidos.items(), key=lambda item: item[1], reverse=True))
    
    #Imprimir frequencia de nomes:
    print("FREQUENCIA DE NOMES PROPRIOS")
    for k,v in sorted_proprio.items():
        print(f"Nome: {k}     Frequencia:{v}")
    print("\n")
    print("FREQUENCIA DE APELIDOS")
    for k,v in sorted_apelido.items():
        print(f"Nome: {k}     Frequencia:{v}")
    print("\n")
    #Imprimir Top 5 de nomes mais frequentes 
    print("TOP 5 NOMES PROPRIOS")
    for n in list(sorted_proprio.items())[:5]:
        print(f"Nome: {n[0]}     Frequencia:{n[1]}")
    print("\n")
    print("TOP 5 DE APELIDOS")
    for n in list(sorted_apelido.items())[:5]:
        print(f"Nome: {n[0]}     Frequencia:{n[1]}")
    print("\n")

#Devolve a frequencia de uma relação
def procRelacao(relacao):
    freqRelacao = 0
    for line in dataset:
        dados = re.split(r'::', line[:-1])
        extra = dados[len(dados) - 2]
        
        relacoes = re.findall(r',[aA-zZ]*[ ]*[aA-zZ]*\.', extra)
        
        for rel in relacoes:
            if relacao in rel:
                freqRelacao += 1
            
    print(f"Relação:{relacao}    Frequencia:{freqRelacao}")

#Converte para Jason
def convertjson(ficheiro):
    jsonfile =''
    f=open(ficheiro)
    lista = f.readlines()
    file = open("processos.json", "w")
    file.write("[\n")
    count = 0
    for line in lista[:20]:   
        match = re.search("(?P<Pasta>\d+)::(?P<Data>\d+-\d+-\d+)::(?P<Nome>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)::(?P<Pai>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)?::(?P<Mae>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)?::(?P<Outro>.*?)::",line).groupdict()
        json.dump(match,file)
        if count<19:
                file.write(",\n")
        count+=1
    file.write("]")    


    
def menu():
    print("\n")
    print("Menu:")
    print("1 - Numero de processos por ano")
    print("2 - Numero de frequência de nomes próprios e apelidos por seculo")
    print("3 - Numero de frequencia de relações")
    print("4 - Converte ficheiro para Json")
    print("\n")
    opcao = input("Indique a sua opção:")
    match(opcao):
        case "1":
            ano = input("Indique um ano:")
            print("Numero de processos:" + str(procAno(ano)))
        case "2":
            sec = input("Indique um seculo:")
            procSec(int (sec))
        case "3":
            relacao = input("Introduza a relação:")
            procRelacao(relacao)
        case "4":
            convertjson("TPC3/processos.txt")

menu()
