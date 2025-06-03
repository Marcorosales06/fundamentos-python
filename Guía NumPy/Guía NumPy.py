import numpy as np

# Supongamos que esta es la matriz de consumos de ejemplo (puedes reemplazarla con los datos reales):
# Cada fila representa un hogar, cada columna un día (0 = lunes, ..., 6 = domingo)
#            L   M   X   J   V   S   D
consumo = np.array([
    [10, 12, 11, 13, 12, 15, 14],  # hogar 0
    [8, 9, 10, 11, 9, 8, 10],      # hogar 1
    [15, 14, 13, 16, 14, 17, 18],  # hogar 2
    [6, 5, 7, 6, 5, 5, 6],         # hogar 3
    [9, 10, 11, 12, 13, 14, 15],   # hogar 4
    [20, 19, 18, 21, 22, 23, 24],  # hogar 5
    [7, 8, 9, 7, 6, 5, 6]          # hogar 6
])

# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
# Día 5 = viernes → índice 4
consumo_hogar5_viernes = consumo[5, 4]
print("1. Consumo del hogar 5 el viernes:", consumo_hogar5_viernes)

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
# Últimos 3 hogares: filas -3: → índices [-3, -2, -1]
# Domingo = día 6 → índice 6
consumo_ultimos3_domingos = consumo[-3:, 6]
print("2. Consumo de los últimos 3 hogares el domingo:", consumo_ultimos3_domingos)

# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
promedio_fines_semana = np.mean(consumo[:, [5, 6]])
print("3. Promedio de consumo fines de semana (sábado y domingo):", promedio_fines_semana)

# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares?
# Calcular desviación estándar por columna (día)
std_dias = np.std(consumo, axis=0)
dia_mayor_std = np.argmax(std_dias)
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
print(f"4. Día con mayor desviación estándar: {dias[dia_mayor_std]} (std = {std_dias[dia_mayor_std]:.2f})")
# Explicación:
# Una mayor desviación estándar indica que los consumos entre hogares varían mucho ese día, es decir, hay más desigualdad.

# 5. Identifica los 3 hogares con menor consumo total durante la semana.
consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print("5. Tres hogares con menor consumo total (índice y valor):")
for i, valor in zip(indices_menor_consumo, valores_menor_consumo):
    print(f"   Hogar {i} → {valor}")

# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
hogar3_original = consumo[3]
hogar3_incrementado = hogar3_original * 1.10  # Aumentar 10%
nuevo_total_hogar3 = np.sum(hogar3_incrementado)
print("6. Nuevo consumo total semanal del hogar 3 con +10% diario:", nuevo_total_hogar3)