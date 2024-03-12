import math


graus = float(input("Digite um valor em graus para um ângulo: "))


radianos = math.radians(graus)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Imprimir os resultados
print("O seno do ângulo é:", seno)
print("O cosseno do ângulo é:", cosseno)
print("A tangente do ângulo é:", tangente)