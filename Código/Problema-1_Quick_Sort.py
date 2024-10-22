import time
import random

def sort(array):
    """Sort the array by using quicksort."""
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
    
#Función auxiliar para el tamaño del arreglo.
#_________________________________________________________________    
def tamano(data,X):
    for i in range (0,X):
        num=random.randint(0,100)
        data.append(num)        

#_________________________________________________________________    
#Arreglo tamaño mil
prom=0
for n in range (0,10):
    data=[]    
    tamano(data,1000)
    seconds = time.time()
    data=sort(data)
    seconds_final = time.time()
    time1=seconds_final-seconds
    #print(time1)
    #print(data)
    prom+=time1
    
print("tiempo promedio",prom/10)
#_________________________________________________________________  
#Arreglo tamaño diez mil
prom=0
for n in range (0,10):
    data=[]    
    tamano(data,2000)
    seconds = time.time()
    data=sort(data)
    seconds_final = time.time()
    time1=seconds_final-seconds
    #print(time1)
    #print(data)
    prom+=time1
    
print("tiempo promedio",prom/10)
#_________________________________________________________________  
#Arreglo tamaño cien mil
prom=0
for n in range (0,10):
    data=[]    
    tamano(data,3000)
    seconds = time.time()
    data=sort(data)
    seconds_final = time.time()
    time1=seconds_final-seconds
    #print(time1)
    #print(data)
    prom+=time1
    
print("tiempo promedio",prom/10)
#_________________________________________________________________  
#Arreglo tamaño un millón
prom=0
for n in range (0,10):
    data=[]    
    tamano(data,4000)
    seconds = time.time()
    data=sort(data)
    seconds_final = time.time()
    time1=seconds_final-seconds
    #print(time1)
    #print(data)
    prom+=time1
    
print("tiempo promedio",prom/10)
#_________________________________________________________________  
#Arreglo tamaño diez millones
prom=0
for n in range (0,10):
    data=[]    
    tamano(data,5000)
    seconds = time.time()
    data=sort(data)
    seconds_final = time.time()
    time1=seconds_final-seconds
    #print(time1)
    #print(data)
    prom+=time1
    
print("tiempo promedio",prom/10)