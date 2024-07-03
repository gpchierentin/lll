# ### Exercícios

exercicio = int(input("Informe o número do exercício (1-25): "))
print()

if exercicio < 1 or exercicio > 25:
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
    elif exercicio == 2:
        n1 = float(input("Digite um número: "))
        resto = n1 % 5

        print(f"O resto da divisão por 5 é: {resto}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
    elif exercicio == 3:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        multiplicacao = n1 * n2

        print(f"A multiplicação dos dois números é: {multiplicacao}")


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    elif exercicio == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        divisao = n1 // n2

        print(f"A divisão inteira dos dois números é: {divisao}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
    elif exercicio == 5:
        n1 = float(input("Digite um número: "))
        quadrado = n1 ** 2

        print(f"O quadrado do número inserido é: {quadrado}")


# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
    elif exercicio == 6:
        n1 = float(input("Digite um número decimal: "))
        n2 = float(input("Digite outro número decimal: "))
        soma = n1 + n2

        print(f"A soma dos dois números é: {soma}")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    elif exercicio == 7:
        n1 = float(input("Digite um número decimal: "))
        n2 = float(input("Digite outro número decimal: "))
        media = (n1 + n2) / 2

        print(f"A media dos dois números é: {media}")


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
    elif exercicio == 8:
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        potencia = base ** expoente

        print(f"A base fornecida {base} e o expoente {expoente} resulta na potência: {potencia}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
    elif exercicio == 9:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32

        print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
    elif exercicio == 10:
        import math

        raio = float(input("Digite o raio do círculo: "))
        area = 2 * math.pi * raio

        print(f"A circunferência do círculo é: {area}")


# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
    elif exercicio == 11:
        txt = input("Digite um texto: ")

        print(f"O texto em maiúsculo é: {txt.upper()}")


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
    elif exercicio == 12:
        nome_completo = input("Digite seu nome completo: ")

        print(f"Seu nome em minúsculo é: {nome_completo.lower()}")


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
    elif exercicio == 13:
        frase = input("Digite uma frase: ")

        if " " not in frase:
            print("A frase fornecida não possui espaços em branco")
        else:
            print(f"Frase sem espaços no início e no final: {frase.strip()}")


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
    elif exercicio == 14:
        data = input("Insira uma data no formato dd/mm/aaaa: ")
        dia, mes, ano = data.split("/")

        print(f"Dia: {dia}, mês: {mes} e ano: {ano}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
    elif exercicio == 15:
        txt1 = input("Digite um texto: ")
        txt2 = input("Digite outro texto: ")

        print(f"O texto concatenado é: {txt1 + txt2}")


# #### Booleanos (`bool`)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
    elif exercicio == 16:
        print("NOTA: preencha com qualquer valor para 'True' ou deixe vazio para 'False'")
        v1 = bool(input("Digite um valor booleano: "))
        v2 = bool(input("Digite outro valor booleano: "))
        resultado_and = v1 and v2

        print(f"O resultado da operação AND entre esses valores é: {resultado_and}")


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
    elif exercicio == 17:
        print("NOTA: preencha com qualquer valor para 'True' ou deixe vazio para 'False'")
        v1 = bool(input("Digite um valor booleano: "))
        v2 = bool(input("Digite outro valor booleano: "))
        resultado_or = v1 or v2

        print(f"O resultado da operação OR entre esses valores é: {resultado_or}")


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
    elif exercicio == 18:
        print("NOTA: preencha com qualquer valor para 'True' ou deixe vazio para 'False'")
        v1 = bool(input("Digite um valor booleano: "))
        invertido = not v1

        print(f"O valor invertido é: {invertido}")


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
    elif exercicio == 19:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        
        if n1 == n2:
            print("Os números fornecidos são iguais")


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
    elif exercicio == 20:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        
        if n1 != n2:
            print("Os números fornecidos são diferentes")


### Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando `try-except`, garantir que a entrada seja numérica, tratando qualquer `ValueError`. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
    elif exercicio == 21:
        try:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
        
            print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

        except ValueError:
            print("ERRO: entrada inválida; por favor, insira um número!")


### Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize `try-except` para garantir que a entrada seja uma string. Dica: Utilize a função `isinstance()` para verificar o tipo da entrada.
    elif exercicio == 22:
        MSG_ERRO = "ERRO: entrada inválida; por favor, insira uma palavra ou frase!"

        txt = input("Digite uma palavra ou frase: ")
        
        if txt is not None and txt != "":
            try:
                if isinstance(txt, str):
                    if txt.lower() == txt.lower()[::-1]:
                        print("A palavra ou frase é um palíndromo!")
                    else:
                        print("A palavra ou frase não é um palíndromo!")
            except:
                print(MSG_ERRO)
        else:
            print(MSG_ERRO)


### Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use `try-except` para lidar com divisões por zero e entradas não numéricas. Utilize `if-elif-else` para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
    elif exercicio == 23:
        try:
            n1 = float(input("Digite o 1° número: "))
            n2 = float(input("Digite o 2° número: "))

            operacao = input("Digite a operação desejada (+, -, *, /): ")

            if isinstance(operacao, str):
                if operacao == "+" or operacao.lower() == "adição":
                    resultado = n1 + n2
                elif operacao == "-" or operacao.lower() == "subtração":
                    resultado = n1 - n2
                elif operacao == "*" or operacao.lower() == "multiplicação":
                    resultado = n1 * n2
                elif operacao == "/" or operacao.lower() == "divisão":
                    try:
                        resultado = n1 / n2
                    except ZeroDivisionError:
                        print("ERRO: não é possível dividir por zero!")
                        exit()
                
                print(f'O resultado da operação "{operacao}" de {n1} e {n2} é: {resultado}')
            else:
                print("ERRO: operação inválida!")
        except ValueError:
            print("ERRO: entrada inválida; por favor, insira um número!")


### Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize `try-except` para assegurar que a entrada seja numérica e utilize `if-elif-else` para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
    elif exercicio == 24:
        try:
            n1 = float(input("Digite um número: "))
            
            if isinstance(n1, float):
                positivo, negativo, zero, par, impar = False, False, False, False, False

                if n1 > 0:
                    positivo = True
                elif n1 < 0:
                    negativo = True
                else:
                    zero = True

                # Transformando em inteiro para verificar a paridade
                if int(n1) % 2 == 0:
                    par = True
                else:
                    impar = True

                # Criando uma lista (tupla) de nomes que serão exibidos e valores (True/ False)
                lista = zip(['positivo', 'negativo', 'zero', f'o inteiro {int(n1)} é par', 'ímpar'], [positivo, negativo, zero, par, impar])
                
                # valores = []
                # for nome, valor in lista:
                #     if valor:
                #         valores.append(nome)
                valores = [nome for nome, valor in lista if valor]
                
                resultado = " e ".join(valores)

                print(f"O número inserido {n1} é {resultado}!")

        except ValueError:
            print("ERRO: entrada inválida; por favor, insira um número!")


### Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize `try-except` para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
    elif exercicio == 25:
        numeros = input("Digite uma lista de números (separados por vírgula): ")
        
        # Remover espaços em branco e transformar em uma lista
        lista_numeros = numeros.replace(" ", "").split(',')

        try:
            nova_lista = []

            for i in lista_numeros:
                nova_lista.append(int(float(i)))                
                
            print(f'A lista de números inteiros é: {nova_lista}')

            # Ordena a lista de forma ascendente
            nova_lista.sort()
            print(f'Ordem ascendente: {nova_lista}')

            # Remove elementos duplicados
            nova_lista = list(dict.fromkeys(nova_lista))
            print(f'Numeros distintos: {nova_lista}')

        except:
            print("ERRO: entrada inválida; por favor, insira um número!")
