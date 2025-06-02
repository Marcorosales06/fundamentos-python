x = input("Ingrese números separados por espacio: ").split()
x = [int(i) for i in x]
z = []

for i in range(len(x)):
    for i in x:
        if i not in z:
            z.append(i)
    
print(z)