import types

diz_o_dicionario={"a":1,
                  "b":2,
                  "c":3}
diz_a_lista=[1+1,2,2+2,4,4+4,8,8+8,16]

def diz_o_tipo(a):
    tipo=type(a)
    if tipo==str:
        return("String")
    elif tipo==list:
        return("Lista")
    elif tipo==dict:
        return("Dicionário")
    elif tipo==int:
        return("Número inteiro")
    elif tipo==float:
        return("Número decimal")
    elif tipo==types.FunctionType:
        return("Função")
    elif tipo==types.BuiltinFunctionType:
        return("Função interna")
    else:
        return(str(tipo))
    
print("É um/a: ", diz_o_tipo("Alo")) # Exibe: String 1
print("É um/a: ", diz_o_tipo(print)) # Exibe: Função interna 2
print("É um/a: ", diz_o_tipo(diz_o_dicionario)) # Exibe: Dicionário 3
print("É um/a: ", diz_o_tipo(diz_a_lista)) # Exibe: Lista 4 
print("É um/a: ", diz_o_tipo(diz_o_tipo)) # Exibe: Função 5
print("É um/a: ", diz_o_tipo(605+4)) # Exibe: Número inteiro 6
print("É um/a: ", diz_o_tipo(6.8+0.1)) # Exibe: Número decimal 7