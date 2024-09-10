arquivo = open('loremipsum.txt', 'r')

conteudo_completo = arquivo.read()
print("Conteúdo completo do arquivo:")
print(conteudo_completo)

arquivo.seek(0)

primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:")
print(primeira_linha)

arquivo.seek(0)

tres_primeiros_caracteres = arquivo.read(3)
print("\nTrês primeiros caracteres do arquivo:")
print(tres_primeiros_caracteres)

arquivo.close()

with open('loremipsum.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print("\nConteúdo lido com a instrução 'with':")
print(conteudo)