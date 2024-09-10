arquivo = open('texto.txt', 'w', encoding='utf-8')

texto = list()

texto.append("Esta é a primeira linha do arquivo.\n")
texto.append("Aqui está a segunda linha do texto.\n")
texto.append("E finalmente, esta é a terceira linha.\n")

arquivo.writelines(texto)

arquivo.close()

print("Arquivo 'texto.txt' criado e escrito com sucesso.")