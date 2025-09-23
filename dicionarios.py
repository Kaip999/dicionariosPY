from tkinter import image_types

dic = {"nome"   : ["PINOQUIO", "GEPPETO",  "ALIDORU"     ],
       "arma"   : ["Espada"  ,  "cordas",  "picareta"    ],
       "indole" : ["neutra"  ,  "má"    ,  "boa"         ],
       "status" : ["vivo"    ,  "morto" ,  "desconhecido"],
       "ergo"   : [30000     ,  12000   ,   5600         ]}

#-----------------------------------------------------cria indices--------------------------------------------
def CriaIndices(lista):
    # INDICES = {dic['nome'][i] : i for i in range(len(dic['nome']))}
    INDICES = {}
    for i in range(len(lista)):
        INDICES[lista[i]] = i
    return INDICES

def AchaIndice(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

INDICES = CriaIndices(dic["nome"])

#----------------------------------------pergunta-----------------------------------------
print(dic["nome"])
resp = input("sobre qual personagem você deseja saber mais?")
resp = resp.upper()

#-----------------------------------------print/resposta--------------------------------------------
for i in dic:
    print(f"{i} :",end=" ")
    print(dic[i][INDICES[resp]])
    # dic [i = chaves] [dentro da lista indice ve o nome e volta o valor]
    # exemplo: dic [armas] [2]

#--------------------------------------------acha o maior valor de ergo ------------------------
def MaiorErgo(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    return maior
