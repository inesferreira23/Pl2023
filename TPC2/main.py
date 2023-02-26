def removeMenos(num):
    fs = ""
    sc = ""
    i = 0
    while num[i] != "-":
        fs = fs + num[i]
        i += 1
    i += 1
    while i < len(num):
        sc = sc + num[i]
        i += 1
    res = int(fs)-int(sc)
    return res

def main():
    On = True
    count = 0
    num = "0"
    texto = input("Insira um texto: ")
    print("\n")

    for i in range(0, len(texto)):
        if texto[i] != "=":
            if On:
                if texto[i].isdigit() or texto[i] == "-" and texto[i+1].isdigit():
                    num = num + texto[i]
                else:
                    if "-" in num: 
                     aux = removeMenos(num)
                     count += int(aux)
                     num = "0"
                    else:
                        count += int(num)
                        num = "0"

            if texto[i] in "Oo" and texto[i+1] in "Nn":
                On = True
            if texto[i] in "Oo" and texto[i+1] in "Ff" and texto[i+2] in "Ff":
                On = False
        else:
            if "-" in num:
                aux = removeMenos(num) 
                count += int(aux)
                num = "0"
            else:
                count += int(num)
                num = "0"
            print("A soma dos numeros inseridos é:" + str(count))

main()
