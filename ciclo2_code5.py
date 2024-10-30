# coding=utf-8
# Escreva uma função que:
# a) Receba uma frase como parâmetro.
# b) Retorne uma nova frase com cada palavra com as letras invertidas.

# Criação da função
def inv_pala(frase):
    # vou dividir a frase em palavras, e inverter cada uma para juntar depois
    pala_inv = [palavra[::-1] for palavra in frase.split()]
    frase_inv = ' '.join(pala_inv)
    return frase_inv

# Campo para usuário digitar frase e ela ser invertida
frase = raw_input("Digite uma frase: ")
print("{}".format(inv_pala(frase)))