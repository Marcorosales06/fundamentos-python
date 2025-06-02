x = input("Ingresa un número: ")
y = list(x)
z = 0

print("Proceso de reducción para", x, ":")

while True:

    
    z = 0  
    for i in range(len(y)):
        z = z + int(y[i])
    print(x," = ",z)
    x = z
    if z < 10:
        break  
    else:
        y = list(str(z))  
    
print("El resultado final es: ",z)
