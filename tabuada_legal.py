#tabuada de adição
"""n=int(input("Tabuada de:"))
x=1
while x<=10:
    print(n+x)
    x=x+1"""
#tabuada de multiplicação
"""n=int(input("Insira o número para a tabuada: "))
x=1
while x<=20:
    print(n*x)
    x=x+1"""
#calculadora de tabuada completa
"""def tabuada(): 
    numero=int(input("Tabuada do número: "))
    multiplicador=int(input("Qual será o último multiplicador desse número: "))
    y=0
    while y<=multiplicador:
        print(numero, "x", y,"=", numero*y)
        y=y+1
tabuada()"""
#*break' é utilizado para interromper um *while*.
s=0
c=0
while True:
    v=int(input("Número a somar ou 0 pra sair: "))
    if v==0:
        break
    s+=v
    c+=1

if c > 0:
    media = s / c
    print("Soma:", s)
    print("Quantidade de valores:", c)
    print("Média dos valores: ", media)
else:
    print("Nenhum número informado.")