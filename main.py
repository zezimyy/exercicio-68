import random

loop = True
escolha = "a"
escolha_numero = 0
PouI = 0
escolha_numero_maquina = 0
vitorias = 0

while loop == True:
  escolha = str(input("Par ou Impar: "))

  if escolha == "par":
    escolha_numero_maquina = random.randint(0, 10)
    escolha_numero = int(input("Digite um numero: "))
    PouI = escolha_numero + escolha_numero_maquina

    if PouI % 2 == 0:
      print()
      print("-=" * 10)
      print("jogador ganhou!!!")
      vitorias += 1
      print("-=" * 10)
      print()

    else:      
      print()
      print("-=" * 10)
      print("jogador perdeu!!!")
      print(vitorias)
      print("-=" * 10)
      print()
      break

  if escolha == "impar":
    escolha_numero_maquina = random.randint(0, 10)
    escolha_numero = int(input("Digite um numero: "))
    PouI = escolha_numero + escolha_numero_maquina

    if PouI % 2 != 0:
      print()
      print("-=" * 10)
      print("jogador ganhou!!!")
      vitorias += 1
      print("-=" * 10)
      print()

    else:      
      print()
      print("-=" * 10)
      print("jogador perdeu!!!")
      print(vitorias)
      print("-=" * 10)
      print()
      break