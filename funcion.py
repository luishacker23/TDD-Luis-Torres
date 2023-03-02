def encontrar_menor(arr):
   
    pequeno = arr[0] 
    for num in arr:
        if num < pequeno:
            pequeno = num
    return pequeno

arreglo = [35, 22, 8, 20, 14, 3]
print(encontrar_menor(arreglo))
 