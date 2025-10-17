#Añadir comentarios
nombres = [
    "ANGEL MAURICIO", "MARCO ANTONIO", "EDGAR DANIEL", "BETHZY ALEYDIS", "FABIOLA MICHEL", "FRIDA VICTORIA",
    "ERNESTO YAHIR", "ANGEL YAEL", "AMBAR NAHOMI", "URIEL", "LUIS ENRIQUE", "BRAYAN ALEXANDER",
    "ERICK", "FERNANDA ABIGAIL", "ESTEFANI SARAHI", "YUMIKO JATZERY", "HANSEL DANIEL", "JULIO ALBERTO", 
    "ENRIQUE UZIEL", "YOJAN JOEL", "PEDRO EDUARDO", "MIREYA YAMILE", "ALISON DAYANA", "PRISCILA", 
    "SERGIO ALEXIS", "RICARDO", "SAMUEL JESHUA", "VANESSA ISABEL", "SARAHI VALERIA",
    "DAVID GERSSAYN", "JOSE ANGEL", "GABRIEL", "CHISTIAN YUREM", "ARTURO AZAEL", "ARMANDO"
]

# 1. Cuantos nombres inician con vocal
vocales = ("A", "E", "I", "O", "U")
inicio_vocal = 0
for nombre in nombres:
    if nombre[0] in vocales:
        inicio_vocal += 1
print("Nombres que inician con vocal:", inicio_vocal)

# 2. Cuantos nombres tienen mas de 10 letras
mas_de_10 = 0
for nombre in nombres:
    if len(nombre.replace(" ", "")) > 10:
        mas_de_10 += 1
print("Nombres con mas de 10 caracteres (sin espacio):", mas_de_10)

# 3. Primeros 3 nombres en orden alfabetico
nombres_ordenados = sorted(nombres)
print("Primeros 3 nombres en orden alfabetico:")
for nombre in nombres_ordenados[:3]:
    print(nombre)

# 4. Buscar nombres que contienen la letra "Y"
con_y = []
for nombre in nombres:
    if "Y" in nombre:
        con_y.append(nombre)
print("Nombres que contienen la letra Y:")
for nombre in con_y:
    print(nombre)