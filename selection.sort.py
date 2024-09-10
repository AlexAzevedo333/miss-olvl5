def selectionSort(array):
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

array_numeros = [64, 25, 12, 22, 11, 90, 18, 30, 50, 80, 33, 56, 23, 45, 78]

print("Array original:", array_numeros)

selectionSort(array_numeros)

print("Array ordenado:", array_numeros)