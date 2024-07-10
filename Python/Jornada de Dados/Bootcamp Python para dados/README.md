# Bootcamp Python para dados

## Aula 01
Setup inicial: Python, Git & Github, e VSCode.

Comandos:
```python
    $ print()
    $ input()
    $ type()
```



## Aula 02
Try-Except, TypeError, Type Check, Type Conversion e Condicional (if, elif e else).

Try-Except:
```python
    $ try:
        # tente fazer isso

    $ except:
        # caso contrario (exceção), faça isso

    $ else:
        # adicionalmente tente fazer isso

    $ finally:
        # incondicionalmente, faça isso
```

TypeError:
```python
    $ try:
        # alguma coisa

    $ except TypeError as e:
        print(e)
```

Type Check:
```python
    $ isinstance()
```

Type Conversion:
```python
    $ str()
    $ int()
    $ float()
    $ bool()
```

Condicional:
```python
    $ if <condicao>:
        # faça isso se <condicao> for verdadeira

    else:
        # faça isso se <condicao> for falsa
```

```python
    $ if <condicao>:
        # faça isso se <condicao> for verdadeira
    
    elif <nova_condicao>:
        # faça isso se <nova_condicao> for verdadeira
    
    else:
        # faça isso se <condicao> e <nova_condicao> forem falsas
```



## Aula 03
Run-Debug (VSCode), Condicional (if, elif e else), Laço de Repetição (for e while), Listas (list) e Dicionários (dict).

Laço de Repetição:<br />
`for` é utilizado para iterar sobre os itens de qualquer iterável (listas, strings, objetos de dicionário e etc.) e executar um bloco de código para cada item.
```python
    $ for <nome_variavel> in <objeto_iteravel>:
        # repita isso
```

`while` é utilizado para executar um bloco de código repetidamente enquanto uma condição especificada é avaliada como verdadeira (True).
```python
    $ while <condicao>:
        # repita isso
```

Listas (`list()`):
```python
    $ list(range(5, 10))
    > [5, 6, 7, 8, 9]

    $ list(range(0, 10, 3))
    > [0, 3, 6, 9]

    $ list(range(-10, -100, -30))
    > [-10, -40, -70]
```

Dicionários (`dict()`):
```python
    $ vendas = {"categoria": "eletrônicos", "valor": 1200}

    $ lista_usuarios = [
        {"nome": "Alice", "email": "alice@example.com"}
    ,   {"nome": "Bob", "email": ""}
    ,   {"nome": "Carol", "email": "carol@example.com"}
    ]
```



<br>
<hr />
<br>

## Exercícios

### [Aula 01](#aula-01)

1- Solicitar o nome do usuário e retornar o número de caracteres deste nome.

2- Solicitar dois números e retornar a soma deles.

✅ **Resolução:** [aula_01.py](https://github.com/gpchierentin/lll/tree/main/Python/Jornada%20de%20Dados/Bootcamp%20Python%20para%20dados/aula_01.py)



### [Aula 02](#aula-02)

1- Solicitar dois números inteiros e retornar a soma deles.

2- Solicitar um número e retornar o resto da divisão dele por 5.

3- Solicitar dois números e retornar a multiplicação deles.

4- Solicitar dois números inteiros e retornar a divisão inteira do primeiro pelo segundo.

5- Solicitar um número e retornar o valor quadrado dele.

6- Solicitar dois números flutuantes e retornar a soma deles.

7- Solicitar dois números flutuantes e retornar a média deles.

8- Solicitar a base e o expoente e retornar a potência.

9- Solicitar a temperatura em Celsius e retornar em Fahrenheit.

10- Solicitar o raio de um círculo e retornar a área dele.

11- Solicitar uma string e retornar em maiúsculo.

12- Solicitar o nome completo do usuário e retornar em minúsculo.

13- Solicitar uma frase e retornar sem espaços em branco no início e no final.

14- Solicitar uma data no formato "dd/mm/aaaa" e retornar separadamente o dia, o mês e o ano.

15- Solicitar duas strings e retornar elas concatenadas.

16- Solicitar dois valores booleanos e retornar a operação `AND` entre eles.

17- Solicitar dois valores booleanos e retornar a operação `OR` entre eles.

18- Solicitar um valor booleano e retornar o valor inverso.

19- Solicitar dois números e retornar se são iguais.

20- Solicitar dois números e retornar se são diferentes.

21- Solicitar a temperatura em Celsius e retornar em Fahrenheit.
Tratar se o valor inserido é numérico.

22- Solicitar uma palavra ou frase e retornar se esse texto é um palíndromo.
Tratar se o valor inserido é string.

23- Solicitar dois números, uma operação matemática básica e retornar o cálculo dessa operação.
Tratar se os valores inseridos são numéricos e a divisão por zero.

24- Solicitar um número e retornar como positivo, negativo ou zero. Adicionalmente, se par ou ímpar.
Tratar se o valor inserido é numérico.

25- Solicitar uma lista de números, separados por vírgulas, e retornar os números convertidos para inteiro.
Tratar a conversão de cada item da lista.

✅ **Resolução:** [aula_02.py](https://github.com/gpchierentin/lll/tree/main/Python/Jornada%20de%20Dados/Bootcamp%20Python%20para%20dados/aula_02.py)



### [Aula 03](#aula-03)

1- Verificar qualidade de dados de vendas e garantir valores positivos para quantidade e preço.

2- Classificar cada leitura de temperatura de sensores IoT considerando a escala: menor que 18°C está baixa, menor ou igual 26°C está normal e acima disso a temperatura está alta.

3- Analisar logs de uma aplicação e filtrar mensagens com severidade igual a 'ERROR'.

4- Solicitar a idade e o e-mail do usuário e verificar se a idade está dentro do intervalo do sistema de recomendação e seja um e-mail válido.

5- Analisar uma transação e verificar se ela é suspeita seguindo as regras de negócio estabelecidas.

6- Contar quantas vezes cada palavra aparece em um determinado texto.

7- Normalizar uma lista de números para que fiquem na escala de 0 a 1.

8- Analisar uma lista de usuários e identificar o registro que tenha campos ausentes.

9- Extrair os números pares de uma lista de valores aleatórios.

10- Calcular o total de vendas por categoria de um conjunto de registros de vendas.

11- Solicitar a entrada de dados até que uma palavra-chave específica ("sair") seja fornecida.

12- Solicitar um número dentro de um intervalo específico até que a entrada seja válida.

13- Simular o consumo de uma API paginada, onde cada página de dados é processada em loop até que não haja mais páginas.

14- Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

15- Processar itens de uma lista até encontrar um valor específico inserido pelo usuário que indica a condição de interrupção.

✅ **Resolução:** [aula_03.py](https://github.com/gpchierentin/lll/tree/main/Python/Jornada%20de%20Dados/Bootcamp%20Python%20para%20dados/aula_03.py)


<br>
<hr />
<br>


## Desafios

### [Aula 01](#aula-01)

1- Escrever um programa que o usuário digita o seu nome, o valor do seu salário mensal e o percentual do bônus que recebeu. 
O programa deve imprimir uma mensagem saudando o usuário e informando o valor do novo salário.

✅ **Resolução:** [kpi.py](https://github.com/gpchierentin/lll/tree/main/Python/Jornada%20de%20Dados/Bootcamp%20Python%20para%20dados/kpi.py)



### [Aula 02](#aula-02)

1- Refatorar o programa da [aula anterior](https://github.com/gpchierentin/lll/tree/main/Python/Jornada%20de%20Dados/Bootcamp%20Python%20para%20dados#aula-01-2) evitando bugs conhecidos.

✅ **Resolução:** [kpi_try_except.py](https://github.com/gpchierentin/lll/tree/main/Python/Jornada%20de%20Dados/Bootcamp%20Python%20para%20dados/kpi_try_except.py)



### [Aula 03](#aula-03)

1- Refatorar o programa da [aula anterior](https://github.com/gpchierentin/lll/tree/main/Python/Jornada%20de%20Dados/Bootcamp%20Python%20para%20dados#aula-02-2) repetindo o fluxo até que o usuário insira informações válidas.

✅ **Resolução:** [kpi_while.py](https://github.com/gpchierentin/lll/tree/main/Python/Jornada%20de%20Dados/Bootcamp%20Python%20para%20dados/kpi_while.py)


<br>
<hr />
<br>

🌐 Referências:
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
