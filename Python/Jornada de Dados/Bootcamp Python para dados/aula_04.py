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


#%%
# 6. Eliminação de Duplicatas: Dada uma lista de emails, remover todos os duplicados.
emails : list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
print(emails)

emails_unicos = list(set(emails))
print(emails_unicos)


#%%
# 7. Filtragem de Dados: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades : list = [22, 15, 30, 17, 18]
maior_igual_18 : list = [idade for idade in idades if idade >= 18]

print(maior_igual_18)


#%%
# 8. Ordenação Personalizada: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas : list = [
    {"nome": "Alice", "idade": 30}
,   {"nome": "Bob", "idade": 25}
,   {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)


#%%
# 9. Agregação de Dados: Dado um conjunto de números, calcular a média.
numeros : list = [10, 20, 30, 40, 50]
media : float = sum(numeros) / len(numeros)

print("Média: ", media)


#%%
# 10. Divisão de Dados em Grupos: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares : list = [valor for valor in valores if valor % 2 == 0]
impares : list = [valor for valor in valores if valor % 2 != 0]

print("Pares: ", pares)
print("Ímpares: ", impares)


#%%
# 11. Atualização de Dados: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
    {"id": 1, "nome": "Teclado", "preco": 100}
,   {"id": 2, "nome": "Mouse", "preco": 80}
,   {"id": 3, "nome": "Monitor", "preco": 300}
,   {"id": 4, "nome": "Monitor", "preco": 299}
,   {"id": 5, "nome": "Monitor", "preco": 300.0}
]

print(produtos)

for produto in produtos:
    if produto["nome"] == "Monitor":
        produto["preco"] = 192

print(produtos)


#%%
# 12. Fusão de Dicionários: Dados dois dicionários, fundi-los em um único dicionário.
dic_1 : dict = {"a": 1, "b": 2, "c": 10}
dic_2 : dict = {"c": 3, "d": 4, "a": 10}

dicionario : dict = {**dic_1, **dic_2}

print(dicionario)


#%%
# 13. Filtragem de Dados em Dicionário: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque : dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)


#%%
# 14. Extração de Chaves e Valores: Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario : dict = {"a": 1, "b": 2, "c": 3}

chave : list = list(dicionario.keys())
valor : list = list(dicionario.values())

print(chave)
print(valor)


#%%
# 15. Contagem de Frequência de Itens: Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto : str = "engenharia de dados"
frequencia : dict = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)


#%%
# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def somar_numeros(numeros : list) -> float:
    return sum(numeros)

somar_numeros([12, 2.3, 30, 4, 35, 6, 17, 82, 29, 9.7])


#%%
# 17. Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário.
def verificar_numero_primo(numero : float) -> bool:
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

print( verificar_numero_primo(11) )
print( verificar_numero_primo(4) )
print( verificar_numero_primo(17) )
print( verificar_numero_primo(-17) )



#%%
# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
txt = input("Digite um texto qualquer: ")

def inverter_texto(texto : str) -> str:
    return texto[::-1]

inverter_texto(txt)


#%%
# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def exercicio_19(lista_numero : list, numero : float):
    return [(a, b) for a in lista_numero for b in lista_numero if a + b == numero]

exercicio_19([12, 2.3, 30, 4, 35, 6, 17, 82, 29, 9.7], 36)


#%%
# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
def ordenar_chave(dicionario : dict) -> list:
    return sorted(dicionario.keys())

ordenar_chave({"c": 1, "e": 2, "a": 3})

