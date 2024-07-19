# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita ao usuário que insira o primeiro número
num1 = float(input("Por favor, insira o primeiro número: "))

# Solicita ao usuário que insira o segundo número
num2 = float(input("Por favor, insira o segundo número: "))

# Solicita ao usuário que escolha a operação
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
operacao = input("Digite o número correspondente à operação desejada: ")

# Realiza a operação escolhida
if operacao == "1":
    resultado = num1 + num2
    print("Resultado da adição:", resultado)
elif operacao == "2":
    resultado = num1 - num2
    print("Resultado da subtração:", resultado)
elif operacao == "3":
    resultado = num1 * num2
    print("Resultado da multiplicação:", resultado)
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
