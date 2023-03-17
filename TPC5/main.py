import re
from sys import stdin

def calculaTroco(saldo):
    troco = {"5c":0, "10c":0,"20c":0,"50c":0,"1e":0,"2e":0}
    if saldo == 0:
        string = "0,"
    else:
        while saldo >= 0.005:
            if saldo >= 2:
                troco["2e"] +=1
                saldo = round(saldo-2, 2)
            elif saldo >= 1:
                troco["1e"] +=1
                saldo = round(saldo-1, 2)
            elif saldo >= 0.5:
                troco["50c"] +=1
                saldo = round(saldo-0.5, 2)
            elif saldo >= 0.2:
                troco["20c"] += 1
                saldo = round(saldo-0.2, 2)
            elif saldo >= 0.1:
                troco["10c"] += 1
                saldo = round(saldo-0.1, 2)
            elif saldo >= 0.05:
                troco["5c"] +=1
                saldo = round(saldo-0.05, 2)
            else:
                print("Inválido")
                break
        string = ""
        for moeda in troco.keys():
            if troco[moeda] != 0:
                string += str(troco[moeda]) + "x" + moeda + ","
    return string

def main():
    flag = False
    global saldo
    saldo = 0 
    for opcao in stdin:
            if opcao == "ABORTAR\n":
                flag = False
                if saldo == 0:
                    print("troco = 0, volte sempre!\n")
                else: 
                    string = calculaTroco(saldo)
                    print("troco = " + string + " volte sempre!\n")
                saldo = 0
                break
            
            if opcao == "LEVANTAR\n" and flag == False:
                flag = True
                moedas = print("Introduza moedas:\n")
            
            
            if re.match(r"MOEDAS\s",opcao) and flag == True:
                listaMoedasAceites = ["5c","10c","20c","50c","1e","2e"]
                moedas2 = re.findall(r"\d+\w",opcao)
                for moeda in moedas2:
                    if moeda in listaMoedasAceites:
                        if moeda[1] == "e":
                            saldo += int(moeda[0])
                        elif moeda[1] == "c":
                            saldo += int(moeda[0]) / 100
                        elif moeda[2] == "c":
                            saldo += int(moeda[:1]) / 10
                    else: print(moeda + "- moeda inválida;")
                print(f"saldo = {saldo:.3f}")
            
            
            if opcao[0] == "T" and flag == True:
                if re.match(r'(T=601\d+|T=641\d+)',opcao) or len(opcao) != 12 and opcao[2] != "0" and opcao[3] != "0":
                    print("Esse número não é permitido neste telefone. Queira discar novo número!\n")
                else:
                    if re.match(r"T=00\d+",opcao):
                        if saldo>= 1.5:
                            saldo -= 1.5
                        else: 
                            print("Saldo insuficiente para realizar ligação para o número escolhido\n")
                    elif re.match(r"T=2\d+",opcao):
                        if saldo >= 0.25:
                            saldo -= 0.25
                        else: 
                            print("Saldo insuficiente para realizar ligação para o número escolhido\n")
                    elif re.match(r"T=808\d+",opcao):
                        if saldo>= 0.10:
                            saldo -= 0.10
                        else: 
                            print("Saldo insuficiente para realizar ligação para o número escolhido\n")
                    elif re.match(r"T=800\d+",opcao):
                        saldo-=0
                    else:
                        print("Número inválido")
                    print(f"saldo = {saldo:.3f}"+"\n")
            
            if opcao == "POUSAR\n" and flag == True:
                flag = False
                string = calculaTroco(saldo)
                print("troco = " + string + " volte sempre!\n")
                saldo = 0

main()