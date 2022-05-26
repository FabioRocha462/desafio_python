from collections import Counter
import random as r
#criando o tota de pares de sapato em uma loja e verificando se atende ac condição dada
total_shoes = -1
while total_shoes <= 0 or total_shoes > 1000:
    total_shoes = int(input("Digite o numero de pares de sapato da loja "))

#criando uma lista com os tamanhos aleatórios entre 2,20 até o tanto de pares passado
lista_shoes = []
lista_shoes = [r.randint(2,20) for x in range(total_shoes)]

#verificando se o número de clientes é válido
total_client = -1
while total_client <= 0 or total_client >= 1000:
    total_client = int(input("digite o total de clientes "))

#criando uma lista com tamanhos de sapatos variados para os clientes, observe que a lista vai até o tanto de clientes passados
sizes = [r.randint(1,20)for x in range(total_client)]

# lista onde vai armazenar os valores pagos pelos clientes
lista_values = []

for i in sizes: # for para percorrer a lista de tamanhos desejados pelos clientes
    if (i in lista_shoes):# verificando se aquele tamanho desejado está na lista ou não
       j=0
       for h in lista_shoes:
           if (i == h):
               lista_shoes.pop(j)
               break
            j=j+1
            lista_values.append([r.randint(10,100)])

mylist = sum(lista_values)
print("total vendido ",mylist)




#lista  = Counter(lista_shoes).keys()
#print(lista)

