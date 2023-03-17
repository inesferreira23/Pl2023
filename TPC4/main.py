import json
import re

with open("TPC4/alunos5.csv", "r", encoding="utf-8") as f:
    dataset = f.readlines()


def csv_to_json():
    
    registo = []
    with open("TPC4/alunos5.json", "w", encoding="utf-8") as f:
        
        funcao = ""
        campos_cabecalho = re.split(r',(?!\d+})', dataset[0].strip())
        if len(campos_cabecalho)>3:
            existe_funcao = re.split(r'(::)', campos_cabecalho[3])
            if len(existe_funcao) > 1:
                funcao = existe_funcao[2]
        

        for line in dataset[1:]:
            lista = []
            linha = line.strip().split(',')
            dic = {}
            for j in range(0,3):
                dic[campos_cabecalho[j]] = linha[j] 
            numeros = re.findall(r'\d+', line)
            if len(numeros)>1:
                for k in numeros:
                    if funcao == "sum":
                        if "Notas_"+ funcao in dic.keys():
                            dic["Notas_"+ funcao] += int(k)
                        else: 
                            dic["Notas_"+ funcao] = 0
                    elif funcao == "media":
                        if "Notas_"+ funcao in dic.keys():
                            soma += int(k)
                            dic["Notas_"+ funcao] = soma/(len(numeros)-1)
                        else: 
                            soma = 0
                            dic["Notas_"+ funcao] = 0
                    else:
                        lista.append(k)
                        dic["Notas"] = lista[1:]
            registo.append(dic) 
        
        json_str = json.dumps(registo, ensure_ascii=False)
        f.write(json_str)

csv_to_json()