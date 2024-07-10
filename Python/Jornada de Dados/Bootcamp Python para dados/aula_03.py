#%%
# ### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
quantidade = float(input('Informe a quantidade: '))
preco = float(input('Informe o preço: '))

if quantidade > 0 and preco > 0:
    print('Dados válidos!')
else:
    print('Dados inválidos!')

#%%
# ### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
temp = float(input('Informe a temperatura: '))

if temp < 18:
    print('Temperatura baixa')
elif temp >= 18 and temp <= 26:
    print('Temperatura normal')
else:
    print('Temperatura alta')

#%%
# ### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])
else:
    print('Nenhum erro encontrado!')

#%%
# ### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
idade = int(input('Informe sua idade: '))
email = input('Informe seu email: ')

if idade > 18 and idade < 65:
    if '@' in email and '.' in email:
        print('Dados de usuário válidos!')
    else:
        print('Email inválido.')
else:
    print('Idade fora do intervalo de recomendação.')

#%%
# ### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print('Transação suspeita!')


#%%
# ### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
txt = "Seja forte e corajoso\n Não temas e não desanimes!"
txt = txt.lower()

palavras = txt.split()
ocorrencias = {}

for p in palavras:
    if p in ocorrencias:
        ocorrencias[p] += 1
    else:
        ocorrencias[p] = 1

print(ocorrencias)

#%%
# ### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
lista_numero = [10, 20, 30, 40, 50, 60,]
minimo = min(lista_numero)
maximo = max(lista_numero)
normalizados = [(x - minimo) / (maximo - minimo) for x in lista_numero]

print(normalizados)

#%%
# ### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

for u in usuarios:
    for campo, valor in u.items():
        if valor == '' or valor is None:
            print(u)

# campo_ausente = [chave for chave, valor in usuarios.items() if valor is None or valor == '']
# print(campo_ausente)

#%%
# ### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
import random

lista_numero = [random.randint(0, 10) for _ in range(10)]
pares = [n for n in lista_numero if n % 2 == 0]
print("Lista original: ", lista_numero)
print("Números pares: ", pares)
#Removendo repetidos 
pares_unicos = list(set(pares))
print("Números pares sem repetições: ", pares_unicos)

#%%
# ### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

vendas_por_categoria = {}
for v in vendas:
    if v["categoria"] in vendas_por_categoria:
        vendas_por_categoria[v["categoria"]] += v["valor"]
    else:
        vendas_por_categoria[v["categoria"]] = v["valor"]

print(vendas_por_categoria)
