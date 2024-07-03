# ### Exercícios

exercicio = int(input("Informe o número do exercício (1-20): "))
print()

if exercicio < 1 or exercicio > 20:
    print("Exercício inválido.")
else:

# #### Inteiros (`int`)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
    if exercicio == 1:
        n1 = int(input("Digite um número inteiro: "))
        n2 = int(input("Digite outro número inteiro: "))
        soma = n1 + n2

        print(f"A soma dos dois números é: {soma}")


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
    if exercicio == 2:
        n1 = float(input("Digite um número: "))
        resto = n1 % 5

        print(f"O resto da divisão por 5 é: {resto}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
    if exercicio == 3:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        multiplicacao = n1 * n2

        print(f"A multiplicação dos dois números é: {multiplicacao}")


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    if exercicio == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        divisao = n1 // n2

        print(f"A divisão inteira dos dois números é: {divisao}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
    if exercicio == 5:
        n1 = float(input("Digite um número: "))
        quadrado = n1 ** 2

        print(f"O quadrado do número inserido é: {quadrado}")


# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
    if exercicio == 6:
        n1 = float(input("Digite um número decimal: "))
        n2 = float(input("Digite outro número decimal: "))
        soma = n1 + n2

        print(f"A soma dos dois números é: {soma}")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    if exercicio == 7:
        n1 = float(input("Digite um número decimal: "))
        n2 = float(input("Digite outro número decimal: "))
        media = (n1 + n2) / 2

        print(f"A media dos dois números é: {media}")


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
    if exercicio == 8:
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        potencia = base ** expoente

        print(f"A base fornecida {base} e o expoente {expoente} resulta na potência: {potencia}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
    if exercicio == 9:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32

        print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
    if exercicio == 10:
        import math

        raio = float(input("Digite o raio do círculo: "))
        area = 2 * math.pi * raio

        print(f"A circunferência do círculo é: {area}")


# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
    if exercicio == 11:
        txt = input("Digite um texto: ")

        print(f"O texto em maiúsculo é: {txt.upper()}")


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
    if exercicio == 12:
        nome_completo = input("Digite seu nome completo: ")

        print(f"Seu nome em minúsculo é: {nome_completo.lower()}")


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
    if exercicio == 13:
        frase = input("Digite uma frase: ")

        if " " not in frase:
            print("A frase fornecida não possui espaços em branco")
        else:
            print(f"Frase sem espaços no início e no final: {frase.strip()}")


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
    if exercicio == 14:
        data = input("Insira uma data no formato dd/mm/aaaa: ")
        dia, mes, ano = data.split("/")

        print(f"Dia: {dia}, mês: {mes} e ano: {ano}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
    if exercicio == 15:
        txt1 = input("Digite um texto: ")
        txt2 = input("Digite outro texto: ")

        print(f"O texto concatenado é: {txt1 + txt2}")


# #### Booleanos (`bool`)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
    if exercicio == 16:
        print("NOTA: preencha com qualquer valor para 'True' ou deixe vazio para 'False'")
        v1 = bool(input("Digite um valor booleano: "))
        v2 = bool(input("Digite outro valor booleano: "))
        resultado_and = v1 and v2

        print(f"O resultado da operação AND entre esses valores é: {resultado_and}")


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
    if exercicio == 17:
        print("NOTA: preencha com qualquer valor para 'True' ou deixe vazio para 'False'")
        v1 = bool(input("Digite um valor booleano: "))
        v2 = bool(input("Digite outro valor booleano: "))
        resultado_or = v1 or v2

        print(f"O resultado da operação OR entre esses valores é: {resultado_or}")


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
    if exercicio == 18:
        print("NOTA: preencha com qualquer valor para 'True' ou deixe vazio para 'False'")
        v1 = bool(input("Digite um valor booleano: "))
        invertido = not v1

        print(f"O valor invertido é: {invertido}")


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
    if exercicio == 19:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        
        if n1 == n2:
            print("Os números fornecidos são iguais")


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
    if exercicio == 20:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        
        if n1 != n2:
            print("Os números fornecidos são diferentes")
