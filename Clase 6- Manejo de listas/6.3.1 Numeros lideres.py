x = list(map(int, input("Ingrese números separados por espacio: ").split()))
n = len(x)
lideres = []

max_derecha = float('-inf')

for i in range(n - 1, -1, -1):  
    if x[i] > max_derecha:
        lideres.append(x[i])
        max_derecha = x[i]

lideres.reverse()  
print(*lideres)