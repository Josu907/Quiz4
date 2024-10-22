import random
import time

#Defining entries

#Bubble Sort Algorithm

def bubbleSort(lista):
    for n in range(len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i+1]:
                swapped = True
                lista[i], lista[i+1] = lista[i+1], lista[i]


ToSort = []

def insert(size):
    for i in range(0,size):
        num = random.randint(0,21)
        ToSort.append(num)



#List size 1000
sizee = 5000
insert(sizee)
start = time.time()
bubbleSort(ToSort)
end = time.time()

executionTime = (end-start)

print(f"Execution time for list size: {sizee} is: {executionTime}")