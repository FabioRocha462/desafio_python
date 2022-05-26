# função para transformar a string em uma lista de caraeteres ordenados
def sort(name):
	lista = []
	for i in name:
		lista.append(i)
	return sorted(lista)

#função para transformar a lista em uma string com os caracteres ordenados
def trans(lista):
	STRG = ""
	for i in lista:
		STRG = STRG + i
	return STRG
# função para contar as vezes que aquele caractere aparece na string
def cont(a, name):
	return name.count(a)
# função para guardar o caractere em uma lista e às vezes que ele aparece em outra lista, sempre observando se o caractere já está na lista ou não
def show(name):
	lista_str = []
	lista_number = []
	for i in name:
		if ((i in lista_str) == False):
			lista_str.append(i)
			lista_number.append(cont(i,name))
	listazip = zip(lista_number,lista_str)
	return listazip
	
	
name = input("Digite o nome ")
if ((len(name) >3) and (len(name) < 10**4)):
	lista = sort(name)
	strg = trans(lista)
	ziper = show(strg)
	lista1 = []
	for i in ziper:
		lista1.append(i)
	lista1 = sorted(lista1, reverse=True)
	j=0
	print(strg)
	for i in range(3):
		print(lista1[i])
else:
	print("Nome inválido")
