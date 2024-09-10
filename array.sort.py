import random

numeros = random.sample(range(1, 101), 15)

print("Array original de números inteiros:", numeros)

numeros.sort()
print("Array ordenado em ordem crescente:", numeros)

numeros.sort(reverse=True)
print("Array ordenado em ordem decrescente:", numeros)

pessoas = [
    {"nome": "Ana", "dataNascimento": "1990-06-15", "cpf": "12345678901", "rg": "MG1234567"},
    {"nome": "Carlos", "dataNascimento": "1985-12-01", "cpf": "23456789012", "rg": "MG2345678"},
    {"nome": "Bruna", "dataNascimento": "1992-08-22", "cpf": "34567890123", "rg": "MG3456789"},
    {"nome": "David", "dataNascimento": "1988-04-10", "cpf": "45678901234", "rg": "MG4567890"},
]

print("\nArray original de pessoas:")
for pessoa in pessoas:
    print(pessoa)

pessoas.sort(key=lambda pessoa: pessoa["nome"])
print("\nArray de pessoas ordenado por nome (ordem crescente):")
for pessoa in pessoas:
    print(pessoa)

pessoas.sort(key=lambda pessoa: pessoa["nome"], reverse=True)
print("\nArray de pessoas ordenado por nome (ordem decrescente):")
for pessoa in pessoas:
    print(pessoa)
