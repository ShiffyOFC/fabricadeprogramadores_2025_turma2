#Codigo que pode causar é colocado em bloco 'try'
#e o código que trata o erro é colocado no block 'except'
#Se ocorrer um erro, ele é colocado em try e enviado após para except
#Se não, ele só será ignorado.

"""try:
    divisão=10/0
    print(divisão)
except:
    print('''    Não foi
    possível realizar
    essa operação!''')"""

"""x=int(input("Escolha seu X: "))
y=int(input("Escolha seu Y: "))
def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("Por favor, não use zeros!")
    except:
        print("\033[91m Algo deu errado...]")
    else:
        print(f"Seu resultado é: {result}")
    finally:
        print("\033[92m Vamos de novo?")
divide(x,y)"""
