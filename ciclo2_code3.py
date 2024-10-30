# coding=utf-8
#Faça um programa que leia 3 números inteiros e mostre o menor deles.

# Cria uma lista
num = []

# Crio uma variavel para condição do while
i = 0

# Estrutura de repetição para pegar 3 valores e adicionar na lista num
while i < 3:
    nume = int(input("Digite um valor: "))
    num.append(nume)
    i = i + 1

# Calculo do menor numero da lista
menor = min(num)

print("O menor numero digitado foi: "+ str(menor))