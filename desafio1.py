listaInteira = [31,-41,59,26,-53,58,97,-93,-23,84]
listaNova = []
i = 0
while len(listaInteira) > i:
    if listaInteira[i] > 0:
        listaNova.append(listaInteira[i])
        i+=1
    else:
        i+=1
print(sum(listaNova))