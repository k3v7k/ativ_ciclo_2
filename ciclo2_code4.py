# coding=utf-8
# Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.

#Função que calcula se numero é primo
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# estrutura de repetição para fazer do 1 a 100
for n in range(1, 101):
    if primo(n):
        print("{} é primo.".format(n))
    else:
        print("{} não é primo.".format(n))