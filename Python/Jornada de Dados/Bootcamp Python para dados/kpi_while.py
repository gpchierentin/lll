# Questão: Cálculo de Bônus com Entrada do Usuário
# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

MSG_ERRO_PADRAO = "ERRO: entrada inválida!"

nome_validado = False
salario_validado = False
bonus_validado = False

# 1. O programa deve começar solicitando ao usuário que insira seu nome.
while not nome_validado:
    try:
        nome = input("\nInsira o seu nome: ")
        
        # Valida se tem 3 ou mais caracteres
        if len(nome) < 3:
            print(MSG_ERRO_PADRAO)

        # Valida se não contém apenas espaços em branco
        elif nome.isspace():
            print(MSG_ERRO_PADRAO)
        
        # Valida se não contém dígitos
        elif any(char.isdigit() for char in nome):
            print(MSG_ERRO_PADRAO)
        
        else:
            nome = nome.title().strip()
            nome_validado = True

    except ValueError:
        print(MSG_ERRO_PADRAO)

# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
while not salario_validado:
    try:
        salario = float(input("\nInsira o valor do seu salário: "))

        if salario <= 0:
            print(MSG_ERRO_PADRAO)
        else:
            salario_validado = True

    except ValueError:
        print(MSG_ERRO_PADRAO)

# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
while not bonus_validado:
    try:
        p_bonus = float(input("\nInsira a porcentagem do bônus recebido: "))

        if p_bonus < 0:
            print(MSG_ERRO_PADRAO)
        else:
            bonus_validado = True

    except ValueError:
        print(MSG_ERRO_PADRAO)

# 4. O cálculo do KPI do bônus de 2024 é de `1000 + salario * bônus`
bonus = 1000 + salario * p_bonus

# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f'\n\nOlá {nome}, o valor do seu bônus foi de R$ {bonus:.2f}')
