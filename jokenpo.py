import random
m=int(random.randint(1,3))
print("Você vai jogar jokenpô com a máquina!")
print("Instruções:Selecione [1] para pedra")
print("Instruções:Selecione [2] para tesoura ")
print("Instruções:Selecione [3] para papel ")
j=int(input("Digite um número pra jogar com a máquina"))
if m==1 and j==2:
    print("Pedra ganha de tesoura. A máquina venceu")
elif j==1 and m==2:
     print("Pedra ganha de tesoura. O jogador venceu")
elif m==2 and j==3:
      print("Tesoura ganha de papel. A máquina venceu")
elif j==2 and m==3:
     print("Tesoura ganha de papel. O jogador venceu")
elif m==3 and j==1:
     print("Papel gannha de pedra. A máquina venceu")
elif j==3 and m==1:
     print("Tesoura ganha de papel. O jogador venceu")
elif j==m:
     print("Empate!!!")
else:
     print("Número inválido")