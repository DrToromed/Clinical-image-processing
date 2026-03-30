pacientes = [
    {"nombre": "Ana", "edad": 34, "diagnostico": "hipertensión"},
    {"nombre": "Luis", "edad": 17, "diagnostico": "asma"},
    {"nombre": "María", "edad": 52, "diagnostico": "diabetes"},
    {"nombre": "Carlos", "edad": 15, "diagnostico": "asma"},
    {"nombre": "Rosa", "edad": 61, "diagnostico": "hipertensión"},
]

acumulado = {}  # {"hipertensión": [suma, count], ...}
    # Pasada 1: acumular edades y contar
for datos in pacientes:
    dx = datos["diagnostico"]
    if dx not in acumulado:
        acumulado[dx] = [datos["edad"], 1]
    else:
        acumulado[dx][0] += datos["edad"]
        acumulado[dx][1] += 1
    # Pasada 2: calcular promedios
resultado = {}
for dx, (suma, count) in acumulado.items():
    print(dx)
    resultado[dx] = suma / count


print(acumulado)
print(resultado)