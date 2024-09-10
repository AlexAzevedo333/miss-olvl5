import time

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

with open('texto.txt', 'r') as arquivo:
    lista_palavras = []
    for linha in arquivo:
        palavras = linha.split()  # Separar a linha em palavras
        lista_palavras.extend(palavras)  # Adicionar as palavras à lista

print("Palavras lidas do arquivo:", lista_palavras)

lista_bubble = lista_palavras[:]
lista_selection = lista_palavras[:]
lista_sort = lista_palavras[:]

inicio_bubble = time.time()
bubbleSort(lista_bubble)
fim_bubble = time.time()
print("\nPalavras ordenadas pelo Bubble Sort:", lista_bubble)
print("Tempo de execução do Bubble Sort: {:.6f} segundos".format(fim_bubble - inicio_bubble))

inicio_selection = time.time()
selectionSort(lista_selection)
fim_selection = time.time()
print("\nPalavras ordenadas pelo Selection Sort:", lista_selection)
print("Tempo de execução do Selection Sort: {:.6f} segundos".format(fim_selection - inicio_selection))

inicio_sort = time.time()
lista_sort.sort()
fim_sort = time.time()
print("\nPalavras ordenadas pelo método nativo sort:", lista_sort)
print("Tempo de execução do método nativo sort: {:.6f} segundos".format(fim_sort - inicio_sort))

with open('palavras_ordenadas.txt', 'w') as arquivo_ordenado:
    for palavra in lista_sort:
        arquivo_ordenado.write(palavra + "\n")

print("\nPalavras ordenadas salvas no arquivo 'palavras_ordenadas.txt'.")
