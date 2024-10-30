# coding=utf-8
# Faca um programa que leia a idade de uma pessoa expressa em dias e
# mostre-a expressa em anos, meses e dias.

#Primeiro solicitarei a idade em dias.
idade_dias = int(raw_input("Digite sua idade em dias: "))

# Agora farei os calculos para retornar em anos, meses e dias

anos = idade_dias // 365
resto_anos = idade_dias % 365
meses = resto_anos // 30
dias = resto_anos % 30

# Print que exibe o resultado para o usuário.

print("Idade: {} anos , {} meses e {} dias.".format(anos, meses, dias))