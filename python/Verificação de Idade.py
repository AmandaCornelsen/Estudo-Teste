diaAtual = 28
diaemmes = diaAtual/30



mesAtual = 10
mesAtual = mesAtual + diaemmes
mesemano = mesAtual/12



anoAtual = 2022
anoAtual = anoAtual + mesemano



dia = input("put your birthday  ")

mes = input("put your month  ")

ano = input("put your year  ") 

diaemmes = int(dia)/30

mesemano = (int(mes) + diaemmes)/12

ano = int(ano) + mesemano

idade = anoAtual - ano








if idade >= 18:

    print("congratulation,your access is complete")

else : 
    print("i'm so sorry, but you are not admit in our house")

19