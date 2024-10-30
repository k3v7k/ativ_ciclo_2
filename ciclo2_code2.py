# coding=utf-8
# Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam
# ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
# os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
# não formam triângulo escrever os valores lidos. (Se a &gt; b + c não formam
# triângulo algum, se a é o maior).

import math

# para que tres lados formem um triangulo, a soma de dois lados deve ser sempre maior que o terceiro lado.

a = int(raw_input("Digite o valor do lado a: "))
b = int(raw_input("Digite o valor do lado b: "))
c = int(raw_input("Digite o valor do lado c: "))

# Verifica se os valores formam um triângulo
if (a < b + c and b < a + c and c < a + b):
    s=(a+b+c)/2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Os valores formam um triângulo.")
    print("A área do triângulo é: {:.2f}".format(area))
else:
    print("Os valores lidos não formam um triângulo: {}, {}, {}".format(a, b, c))