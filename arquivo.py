# open() | Abrir arquivos que precisamos
#        com o nome da pasta e outros.

arquivo=open("Núméros_Legais.txt", "w")
for linha in range(1,26):
    arquivo.write("%d\n" % linha)
arquivo.close()