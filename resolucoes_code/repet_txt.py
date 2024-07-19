# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Solicita ao usuário que insira uma string
string = input("Por favor, insira uma string: ")

# Solicita ao usuário que insira um número inteiro
num = int(input("Por favor, insira um número inteiro: "))

# Cria a string repetida o número de vezes informado, com espaços entre as repetições
resultado = (string + " ") * num

# Remove o espaço extra no final da string resultante
resultado = resultado.strip()

# Exibe o resultado
print("A string repetida é:", resultado)
