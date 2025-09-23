from tkinter import image_types

dic = {"nome" : ["Pinoquio", "Geppeto", "Alidoru"],
       "arma" : ["Espada", "cordas", "picareta"],
       "indole" : ["neutra", "má", "boa"],
       "status" : ["vivo", "morto", "desconhecido"]}

#-----------------------------------------------------cria indices--------------------------------------------
#INDICES = {dic['nome'][i] : i for i in range(len(dic['nome']))}
INDICES = {}
for i in range(len(dic['nome'])):
    INDICES[dic['nome'][i]] = i

#----------------------------------------pergunta-----------------------------------------
print(dic["nome"])
resp = input("sobre qual personagem você deseja saber mais?")

#-----------------------------------------print/resposta--------------------------------------------
for i in dic:
    print(f"{i} :",end=" ")
    print(dic[i][INDICES[resp]])
    # dic [i = chaves] [dentro da lista indice ve o nome e volta o valor]
    # exemplo: dic [armas] [2]