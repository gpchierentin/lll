#%%
# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista = range(1, 11)

for i in lista:
    print(i**2)


#%%
# 2. Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item "C++" e adicione "Ruby".
lista = ["Python", "Java", "C++", "JavaScript"]
print(lista)

lista.remove("C++")
lista.append("Ruby")

print(lista)


#%%
# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
dic = {}

dic["titulo"] = "A Game of Thrones"
dic["autor"] = "George Martin"
dic["ano_publicacao"] = 1996

print(f'--> Título do livro: ', dic["titulo"])
print(f'--> Autor: ', dic["autor"])
print(f'--> Ano de Publicação: ', dic["ano_publicacao"])




#%%
# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

texto = "Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário"

dicionario = {}

for i in texto:
    if i in dicionario:
        dicionario[i] += 1
    else:
        dicionario[i] = 1

print(dicionario)

#Ordenando dicionário com mais ocorrências
print(sorted(dicionario.items(), key=lambda x: x[1], reverse=True))


#%%
# 5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.
l_fruta = ["maçã", "banana", "cereja"]
d_fruta = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

total : float = 0

for fruta in l_fruta:
    total += d_fruta[fruta]

# total = sum(d_fruta[fruta] for fruta in l_fruta)

print(f'Total da lista de compras: R$ {total:.2f}')


