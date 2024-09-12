## NÃO USAR DESSA FORMA
#f = open("11-09/test.txt", "w", encoding="utf-8")
#f.write(str(input())+"\n")
#f.close()
##

##escrita em arquivo
#with open("11-09/test.txt", "a", encoding="utf-8") as f:
#    f.write(str(input())+"\n")
#print("______________")

#leitura em arquivo
with open("11-09/test.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)
print("--------------")

#leitura em uma linha
with open("11-09/test.txt", "r", encoding="utf-8") as f:
    linha = f.readline()
    print(linha)
print("##############")

#leitura em linhas
with open("11-09/test.txt", "r", encoding="utf-8") as f:
    for linha in f.readlines():
        print(linha + "-")
print("**************")

#leitura em bytes
with open("11-09/test.txt", "r", encoding="utf-8") as f:
    conteudo = f.read(10)
    print(conteudo)
print("///////////////")

#leitura em bytes
with open("11-09/test.txt", "r", encoding="utf-8") as f:
    f.seek(15)
    conteudo = f.read()
    print(conteudo)

import pickle ## importar biblioteca que grava objetos

dicionario = {"nome": "Caue", "idade": 11, "cpf":"415413151636"}

#serializa o dicionario
with open("11-09/test.pkl", "wb") as f:
    pickle.dump(dicionario,f)

with open("11-09/test.pkl", "rb") as f:
    dicionario_lido = pickle.load(f)
    print(dicionario_lido)

import json

with open("11-09/test.json", "w", encoding= "utf-8") as f:
    json.dump(dicionario,f,indent=4)
    print(dicionario_lido)

with open("11-09/test.json", "r", encoding= "utf-8") as f:
    mydic = json.load(f)
    print(mydic)

try:
    with open("11-09/test22.json", "r", encoding= "utf-8") as f:
        mydic = json.load(f)
        print(mydic)
except FileNotFoundError as e:
    print(f"Ocorreu um erro: {e}")