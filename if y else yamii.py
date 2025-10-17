Estructura de control utilizando condicional if - else
# Lista de calificaciones de estudiantes
calificaciones = [85, 60, 78, 45, 92, 55, 70, 100, 39, 68, 80, 59]

# 1. Clasificar cada calificacion usando if - else
print("Clasificacion de cada calificacion:")
aprobados = 0
reprobados = 0

for cal in calificaciones:
    if cal >= 60:
        print(f"¨{cal}: Aprobado")
        aprobados += 1
    else:
        print(f"{cal}: Reprobado")
        reprobados += 1

# 2. Contar cuantos aprobaron y reprobaron
print("\nTotal de aprobados:", aprobados)
print("Total de reprobados:", reprobados)

# 3.Encontrar la calificacion  mas alta y mas baja usando if - else 
maxima = calificaciones[0]
minima = calificaciones[0]
for cal in calificaciones:
    if cal > maxima:
        maxima = cal
    if cal < minima:
        minima = cal

print("\nLa calificacion mas alta es:", maxima)
print("La calificacion mas baja es:", minima)

# 4. Analizar si cada calificacion es par o impar usando if - else
print("\nParidad de cada calificacion:")
for cal in calificaciones:
    if cal % 2 == 0:
        print(f"{cal} es par")
    else:
        print("f{cal} es impar")