games = {"NOME"     : ["GOD OF WAR"     ,"ZELDA"           ,"FORZA"  ],
       "PREÇO"      : [199.00           ,230.00            ,150.00   ],
       "PLATAFORMA" : ["playstation"    ,"nintendo"        ,"xbox"   ],
       "GENERO"     : ["ação e aventura","ação e aventura" ,"corrida"],
       "GOT"        : [ True            ,True              ,False    ],
       "ESTOQUE"    : [ 20              ,17                ,12       ]}

def choose(msg, lista):
       opc = " | ".join(lista)
       esc = input(f"{msg} \n {opc} \n ->")
       esc = esc.upper()
       while esc not in lista:
              print("opção invalida!")
              esc = input(f"{msg} \n {opc} \n ->")
              esc = esc.upper()
       return esc

def CriaIndices():
    global INDICES
    INDICES = {games['NOME'][i] : i for i in range(len(games['NOME']))}
    return INDICES

def remove():
       item = choose("qual jogo você deseja remover?", games["NOME"])
       indice = INDICES[item]
       for key in games.keys():
              games[key].pop(indice)
       CriaIndices()
       return

def add():
       for key in games.keys():
              info = input(f"diga o(a) {key} do novo jogo")
              games[key].append(info)
       CriaIndices()
       return

def atualizar():
       jogo = choose("qual jogo voce deseja atualizar as informações?", games["NOME"])
       indice = INDICES[jogo]

       forma = choose("deseja atualizar os itens 'um a um' ou 'escolher' quais informações alterar?", ["UM A UM","ESCOLHER"])

       if forma == "ESCOLHER":
              num_inf = input(f"deseja atualizar quantas informações de {jogo}?: ")
              num_inf = int(num_inf)
              for i in range(num_inf):
                     item = choose("qual item deseja atualizar?", games.keys())
                     value = input(f"diga o novo {item}: ")
                     games[item][indice] = value

       else:
              for key in games.keys():
                     confirmar = choose(f"voce deseja atualizar {key} de {jogo}?", ["S","N"])
                     if confirmar == "S":
                            value = input(f"diga o novo {key}: ")
                            games[key][indice] = value

def intVerify(msg):
       num = input(msg)
       while not num.isnumeric():
              print("invalido")
              num = input(msg)

       return int(num)

def buy():
       jogo = choose("qual jogo você deseja comprar?", games["NOME"])
       indice = INDICES[jogo]

       for key in games.keys():
              print(f"{key} : {games[key][indice]}")
       continuar = choose(f"Você vai levar o {jogo}?", ["SIM","NÃO"])
       if continuar == 'SIM':
              qtd = intVerify(f"Quantas unidades deseja?")
              games['ESTOQUE'][indice] -= qtd
              if qtd <= games['ESTOQUE'][indice]:
                     valor = games['PREÇO'][indice]*qtd
                     carrinho['valor total'] += valor
                     if jogo in carrinho['itens'].keys():
                            carrinho['itens'][jogo] += qtd
                     else:
                            carrinho['itens'][jogo] = qtd
              else:
                     print(f"estamos sem estoque desse jogo")
                     return buy()
       else:
              conti = choose("deseja ver outros itens?", ["SIM","NÃO"])
              if continuar == "SIM":
                  return buy()
              return





carrinho = {"endereço"   : {},
            "itens"      : {},
            "valor total": 0  }

CriaIndices()
buy()
print(carrinho)