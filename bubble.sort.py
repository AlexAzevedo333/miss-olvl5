def bubbleSort(array):
    
    for i in range(len(array)):        
        for j in range(0, len(array) - i - 1):          
            if array[j] > array[j + 1]:               
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

array_numeros = [64, 34, 25, 12, 22, 11, 90, 23, 50, 75, 8, 33, 18, 41, 67]

print("Array original:", array_numeros)

bubbleSort(array_numeros)

print("Array ordenado:", array_numeros)
