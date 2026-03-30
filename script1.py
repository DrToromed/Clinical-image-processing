import random

pacientes = [
    {"nombre": "Ana", "edad": 34, "diagnostico": "hipertensión"},
    {"nombre": "Luis", "edad": 17, "diagnostico": "asma"},
    {"nombre": "María", "edad": 52, "diagnostico": "diabetes"},
    {"nombre": "Carlos", "edad": 15, "diagnostico": "asma"},
    {"nombre": "Rosa", "edad": 61, "diagnostico": "hipertensión"},
]


# Escribe una función filtrar_pacientes que
#reciba la lista y un diagnóstico, y retorne solo los nombres de los pacientes mayores de 18 años con ese diagnóstico.


def filtrar_pacientes(lista, diagnostico):
    lista_dx = []
    for datos in lista:
        if diagnostico == datos["diagnostico"] and datos["edad"]>=18:
            lista_dx.append(datos["nombre"])
    return lista_dx

print(filtrar_pacientes(pacientes, "hipertensión"))

print("__________________________________________________________________")



#Crea una clase Paciente con:
#Atributos: nombre, edad, diagnostico
#Método es_adulto() → retorna True si edad ≥ 18#
#Método descripcion() → retorna un string como: "Ana, 34 años — hipertensión"#

class Paciente():
    def __init__(self,nombre, edad, diagnostico):
        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico

    def es_adulto(self):
        return self.edad >= 18

    def descripcion(self):
        return "{}, {} años - {}".format(self.nombre, self.edad, self.diagnostico)

p = Paciente("Ana", 15, "hipertensión")
print(p.es_adulto())
print(p.descripcion())


print("__________________________________________________________________")

#Ahora crea una clase Medico que herede de Paciente (ambos son personas con nombre y edad), pero con estas diferencias:

#Atributo adicional: especialidad
#Sobreescribe descripcion() → debe retornar: "Dr. Ana — Cardiología"
#Método adicional puede_atender(paciente) → recibe un objeto Paciente y retorna True
# si el diagnóstico del paciente coincide con la especialidad del médico



class Paciente():
    def __init__(self, nombre, edad, diagnostico):
        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico

    def descripcion(self):
        return "{}, {}".format(self.nombre, self.edad)

class Medico(Paciente):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad, None)
        self.especialidad = especialidad

    def descripcion(self):
        return "Dr. {} — {}".format(self.nombre, self.especialidad)

    def puede_atender(self, paciente):
        return self.especialidad == paciente.diagnostico


m = Medico("Ana", 35, "Cardiología")
print(m.descripcion())           # → "Dr. Ana — Cardiología"

p = Paciente("Luis", 45, "Cardiología")
print(m.puede_atender(p))        # → True


print("_____________________________________________________")

class Medicamento():
    def __init__(self, nombre, dosis_mg, frecuencia_horas):
        self.nombre=nombre
        self.dosis_mg=dosis_mg
        self.frecuencia_horas=frecuencia_horas

    def __str__(self):
        return "{}, {}mg, cada {}h ".format(self.nombre, self.dosis_mg, self.frecuencia_horas)

    def __repr__(self):
        return "Medicamento('{}', {}, {})".format(self.nombre, self.dosis_mg, self.frecuencia_horas)

    def doblar_dosis(self):
        return Medicamento(self.nombre, self.dosis_mg * 2, self.frecuencia_horas)



m = Medicamento("Ibuprofeno", 400, 8)
print(m)   # → Ibuprofeno 400mg cada 8h
repr(m)    # → Medicamento('Ibuprofeno', 400, 8)

m1 = Medicamento("Ibuprofeno", 400, 8)
m2 = m1.doblar_dosis()

print(m2)   # → Ibuprofeno 800mg cada 8h
m1 is m2    # → False  (son objetos distintos)

print("_____________________________________________________")

class Medicamento:
    def __init__(self, nombre, dosis_mg):
        self.nombre = nombre
        self.dosis_mg = dosis_mg

    def getNombre(self):
        return self.nombre

    def getDosis(self):
        return self.dosis_mg

    def combinar(self, medicamento_2):
        nomb = "{} + {}".format(self.nombre, medicamento_2.nombre)
        sumas = self.dosis_mg + medicamento_2.dosis_mg
        return Medicamento(nomb, sumas)

m1 = Medicamento("Ibuprofeno", 400)
m2 = Medicamento("Paracetamol", 500)
m3 = m1.combinar(m2)
print(m3.getNombre())  # → "Ibuprofeno + Paracetamol"
print(m3.getDosis())   # → 900

print("_____________________________________________________")

datos_pacientes = [
    ("Ana", 34, "hipertensión"),
    ("Luis", 17, "asma"),
    ("María", 52, "diabetes"),
]

class Paciente():
    def __init__(self, nombre, edad, diagnostico):
        self.nombre=nombre
        self.edad=edad
        self.diagnostico=diagnostico
    def __str__(self):
        return "{}, {}, {}".format(self.nombre,self.edad,self.diagnostico)

lista_pacientes = []
for nombre, edad, diagnostico in datos_pacientes:
    nuevo_paciente = Paciente(nombre,edad,diagnostico)
    lista_pacientes.append(nuevo_paciente)

for p in lista_pacientes:
    print(p)

print("_____________________________________________________")

class Medicamento:
    def __init__(self, nombre, dosis_mg):
        self.nombre = nombre
        self.dosis_mg = dosis_mg

    def getNombre(self):
        return self.nombre

    def getDosis(self):
        return self.dosis_mg

    def combinar(self, medicamento_2):
        nomb = "{} + {}".format(self.nombre, medicamento_2.nombre)
        sumas = self.dosis_mg + medicamento_2.dosis_mg
        return Medicamento(nomb, sumas)

    def __lt__(self, other):
        return self.dosis_mg < other.dosis_mg

medicamentos = [
    Medicamento("Omeprazol", 20),
    Medicamento("Ibuprofeno", 400),
    Medicamento("Amoxicilina", 500),
    Medicamento("Paracetamol", 1000),
]

print("--- Por dosis ---")
for m in sorted(medicamentos, key=lambda x: x.dosis_mg):
    print(m.getNombre(), m.getDosis())

print("--- Por nombre ---")
for m in sorted(medicamentos, key=lambda x: x.nombre):
    print(m.getNombre())

print("--- Default (__lt__) ---")
for m in sorted(medicamentos):
    print(m.getNombre(), m.getDosis())


print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")


class Tratamiento:
    def __init__(self, nombre, dosis_mg):
        self.nombre = nombre
        self.dosis_mg = dosis_mg

    def __str__(self):
        return "{}, {}mg".format(self.nombre, self.dosis_mg)

class Farmaco(Tratamiento):
    def __init__(self,nombre,dosis_mg,laboratorio):
        super().__init__(nombre,dosis_mg)
        self.laboratorio=laboratorio

    def ficha_tecnica(self):
        return "Ficha: {} {}mg".format(self.nombre, self.dosis_mg)

    def __str__(self):
        return "{}, {}mg, {}".format(self.nombre, self.dosis_mg, self.laboratorio)


class Farmaco_Biologico(Farmaco):
    def __init__(self, nombre, dosis_mg, laboratorio, requiere_refrigeración):
        super().__init__(nombre,dosis_mg,laboratorio)
        self.requiere_refrigeracion=requiere_refrigeración

    def condiciones_almacenamiento(self):
        if self.requiere_refrigeracion == True:
            return "{} requiere refigeración: Sí".format(self.nombre)
        else:
            return "{} requiere refigeración: No".format(self.nombre)

fb = Farmaco_Biologico("Humira", 40, "AbbVie", True)
print(fb)                          # → Humira, 40mg, AbbVie
fb.ficha_tecnica()                 # → "Ficha: Humira 40mg"
print(fb.condiciones_almacenamiento())   # → "Humira requiere refrigeración: Sí"


print("_____________________________________________________")

def verificar_dosis(func):
    def wrapped(dosis): #me confunde como python sabe que aqui va lo que esta en administar(dosis)
        if dosis > 0:
            return func(dosis) #me confunde porque hay que pasar de nuevo dosis
        else:
            print("Error: dosis inválida")
    return wrapped #me confunde porque va sin ()
@verificar_dosis
def administrar(dosis):
    print("Administrando {}mg".format(dosis))

administrar(400)   # → Administrando 400mg
administrar(-10)   # → Error: dosis inválida
print("_____________________________________________________")

def nombre_valido(func):
    def wrapped(nombre):
        if nombre != '':
            return func(nombre)
        else:
            print("Error: nombre inválido")
    return wrapped

@nombre_valido
def registrar_paciente(nombre):
    print("Paciente registrado: {}".format(nombre))

registrar_paciente("Ana")   # → Paciente registrado: Ana
registrar_paciente("")      # → Error: nombre inválido

print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")

def agregar_str(cls):
    def __str__(self):
        return "{}, {}mg".format(self.nombre,self.dosis_mg)
    cls.__str__ = __str__
    return cls

@agregar_str
class Medicamento:
    def __init__(self, nombre, dosis_mg):
        self.nombre = nombre
        self.dosis_mg = dosis_mg

m = Medicamento("Ibuprofeno", 400)
print(m)   # → Ibuprofeno, 400mg

print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")



class Medicamento():
    count = 0
    def __init__(self, nombre, dosis_mg):
        self._nombre=nombre
        self.dosis=dosis_mg
        Medicamento.count += 1

    def __str__(self):
        return "{}, {}mg".format(self._nombre,self._dosis_mg)

    @property
    def dosis(self):
        return self._dosis_mg

    @dosis.setter
    def dosis(self,valor):
        if valor <= 250:
            raise ValueError("The minimun dossage is 250")
        else:
            self._dosis_mg = valor

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def unidades_disponibles():
        return "Unidades: mg, g, mcg"



med = Medicamento("Paracetamol", 400)
print(med)
print(med._nombre)
print(med.dosis)
Medicamento("Paracetamol", 400)
Medicamento("Paracetamol", 400)
Medicamento("Paracetamol", 400)
Medicamento("Paracetamol", 400)
print(Medicamento.get_count())
print(Medicamento.unidades_disponibles())

print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")

def repetir(value):
    def decorador(func):
        def wrapper(*args):
            for _ in range(value):
                func()
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("Hola!")

saludar()
# → Hola!
# → Hola!
# → Hola!

print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")
import random


class Dado():
    def __init__(self):
        self.value = random.randint(1, 6)

    def lanzar(self):
        # actualiza self.value con un número aleatorio
        self.value = random.randint(1, 6)
        # no retorna nada
        return self.value

    def get_value(self):
        # retorna self.value
        return self.value

    def __str__(self):
        return f"The initial value is: {self.value}"


class Player():
    def __init__(self, name):
        # nombre y puntos
        self.name = name
        self.points = 0

    def accum_points(self, dado):
        # recibe el dado como argumento
        value = dado.lanzar()
        # suma el valor del dado a self.points
        self.points += value
        # imprime el resultado
        print( f"{self.points}")

    def __str__(self):
        return f"The player {self.name} has {self.points}"


# Programa principal
dado = Dado()
jugador = Player("Oswaldo")

while jugador.points < 20:
    jugador.accum_points(dado)

print(jugador)

print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")

class Paciente():
    def __init__(self, nombre,edad,fc,fr,spO2, PAS, PAD,glucemia,temp):
        self.nombre = nombre
        self.edad = edad
        self.fc = fc
        self.fr = fr
        self.spO2 = spO2
        self.PAS = PAS
        self.PAD = PAD
        self.glucemia = glucemia
        self.temp = temp

    def __str__(self):
        return f"""El paciente {self.nombre} {self.edad} años, ha sido registrado con los siguientes datos:
        Frecuencia Cardiaca: {self.fc}  
        Freceuncia Respiratoria: {self.fr} 
        spO2: {self.spO2}%
        T/A {self.PAS}/{self.PAD} mmHg
        Glucemia Capilar: {self.glucemia} mg/dl
        Temperatura: {self.temp}°C"""

class TriageSystem():
    def __init__(self):
        self.score = 0

    def evaluacion(self, paciente):
        self.score = 0
        if paciente.fc < 70 or paciente.fc > 160:
            self.score += 1
        if paciente.fr > 25:
            self.score += 1
        if paciente.glucemia < 65 or paciente.glucemia > 250:
            self.score += 1
        if paciente.PAS > 180 and paciente.PAD > 90:
            self.score += 1
        if paciente.PAS < 90 and paciente.PAD < 60:
            self.score += 0.5
        if paciente.spO2 < 90:
            self.score += 0.5
        if paciente.temp <= 35 or paciente.temp >= 39:
            self.score += 1
        return self.score

    def clasificacion(self, paciente):
        score = self.evaluacion(paciente)
        if score > 4:
            return "rojo"
        elif score == 4:
            return "amarillo"
        else:
            return "verde"

    def __str__(self):
        return f"Total Score = {self.score}"


class Cola ():
    def __init__(self):
        self.cola_roja = []
        self.cola_amarilla = []
        self.cola_verde = []

    def add_cola(self, triage, paciente):
        clasificacion = triage.clasificacion(paciente)  # ← calcula una vez
        if clasificacion == "rojo":
            self.cola_roja.append(paciente.nombre)
        elif clasificacion == "amarillo":
            self.cola_amarilla.append(paciente.nombre)
        elif clasificacion == "verde":
            self.cola_verde.append(paciente.nombre)

    def __str__(self):
        return "Fila de personas"

triage = TriageSystem()
cola = Cola()

p1 = Paciente("Ana", 45, 110, 28, 88, 185, 95, 300, 38.5)
print(p1)
triage.evaluacion(p1)
print(triage.clasificacion(p1))
cola.add_cola(triage, p1)
print(cola.cola_verde)


print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")

import requests
def ApiPokemon(pokemon):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_buscar = pokemon.lower()
    try:
        resp = requests.get(base_url + pokemon_buscar)
        print(resp.url)
        if resp.status_code != 200:
            return "El Pokémon no existe"
        data = resp.json()
        name = data["name"]
        weight = data["weight"]
        height = data["height"]
        print(f"Pokémon: {name}, weight: {weight}, height: {height}")
        return f"Pokémon: {name}, weight: {weight}, height: {height}"
    except:
        return "El pokémon no existe"

#pokemon = input("¿Qué Pokémon quieres buscar? ")
#ApiPokemon(pokemon)

print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")

import csv

pacientes = [
    {"nombre": "Ana", "edad": 34, "diagnostico": "HTA"},
    {"nombre": "Luis", "edad": 17, "diagnostico": "Asma"},
    {"nombre": "María", "edad": 52, "diagnostico": "DM2"},
]

import csv

pacientes = [
    {"nombre": "Ana", "edad": 34, "diagnostico": "HTA"},
    {"nombre": "Luis", "edad": 17, "diagnostico": "Asma"},
    {"nombre": "María", "edad": 52, "diagnostico": "DM2"},
]

with open("Pacientes.csv", "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["nombre", "edad", "diagnostico"])

    for paciente in pacientes:
        writer.writerow(paciente.values())


with open("Pacientes.csv", "r", encoding="utf-8") as r:
    print(r.read())

print("_____________________________________________________")
print("_____________________________________________________")
print("_____________________________________________________")
import PIL
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
rx_gris = Image.open("rx_gris.jpg")

# 1. Aumentar contraste primero
enhancer = ImageEnhance.Contrast(rx_gris)
rx_mejorada = enhancer.enhance(2.5)

# 2. Luego detectar bordes
rx_bordes = rx_mejorada.filter(ImageFilter.FIND_EDGES)
rx_bordes.save("rx_bordes_mejorada.jpg")

# 3. También prueba nitidez antes de bordes
rx_nitida = ImageEnhance.Sharpness(rx_gris).enhance(3.0)
rx_bordes_nitida = rx_nitida.filter(ImageFilter.FIND_EDGES)
rx_bordes_nitida.save("rx_bordes_nitida.jpg")

rx = Image.open("rx_torax.jpg").convert("L")

# Divide la imagen en una cuadrícula para orientarte
ancho, alto = rx.size
print(f"Tamaño: {ancho} x {alto}")

# Cuadrantes
print(f"Centro: ({ancho//2}, {alto//2})")
print(f"Cuadrante superior izquierdo: (0,0) a ({ancho//2}, {alto//2})")
print(f"Cuadrante superior derecho: ({ancho//2},0) a ({ancho}, {alto//2})")
print(f"Cuadrante inferior izquierdo: (0,{alto//2}) a ({ancho//2}, {alto})")
print(f"Cuadrante inferior derecho: ({ancho//2},{alto//2}) a ({ancho}, {alto})")

rx = Image.open("rx_torax.jpg").convert("L")
draw = ImageDraw.Draw(rx)

# Primer intento — cuadrante superior izquierdo
draw.rectangle([(30, 450), (380, 720)], outline=255, width=3)
draw.text((35, 435), "Infiltracion LID", fill=255)

rx.save("rx_anotada.jpg")

rx = Image.open("rx_torax.jpg").convert("L")
draw = ImageDraw.Draw(rx)

# Infiltración LSD y LMD
draw.rectangle([(30, 200), (380, 600)], outline=255, width=3)
draw.text((35, 185), "Infiltracion LSD/LMD", fill=255)

# Dextrocardia
draw.ellipse([(450, 300), (750, 600)], outline=255, width=3)
draw.text((455, 285), "Dextrocardia", fill=255)

rx.save("rx_anotada_final.jpg")
print("""____________""" * 20)

from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps


def rx_info(rx_image):
    return f"Format: {rx_image.format}, Size: {rx_image.size}, Mode: {rx_image.mode}"


def rx_enhance(rx_image):
    rx_grises = rx_image.convert("L")
    rx_contrast = ImageOps.autocontrast(rx_grises)
    rx_contrast.save("rx_contrast.png")
    return rx_contrast


def rx_equalize(rx_image):
    rx_equalized = ImageOps.equalize(rx_image)
    rx_equalized.save("rx_image_equalized.png")
    return rx_equalized


def rx_shaper(rx_image):
    # Corregido: uso de .filter()
    rx_sharped = rx_image.filter(ImageFilter.SHARPEN)
    rx_sharped.save("rx_sharper.png")
    return rx_sharped


def show_rx_comparativa(rx_img, img_en, img_eq, img_sh):
    ancho, alto = rx_img.size
    lienzo = Image.new("L", (ancho * 4, alto))

    # Aseguramos que la original también sea escala de grises para el lienzo
    rx_img_l = rx_img.convert("L")

    lienzo.paste(rx_img_l, (0, 0))
    # Las demás ya vienen como "L" de tus funciones anteriores
    lienzo.paste(img_en, (ancho, 0))
    lienzo.paste(img_eq, (ancho * 2, 0))
    lienzo.paste(img_sh, (ancho * 3, 0))

    # Añadir etiquetas de texto
    draw = ImageDraw.Draw(lienzo)
    etiquetas = ["Original", "Contraste", "Ecualizada", "Nitidez"]
    for i, texto in enumerate(etiquetas):
        # Dibuja el texto en la esquina superior de cada sección
        draw.text((i * ancho + 10, 10), texto, fill=255)

    lienzo.show()
    lienzo.save("comparativa_completa.png")

# Flujo principal
rx_name = input("Introduce the name of your Radiograph (e.g. image.jpg): ")
try:
    rx_img = Image.open(rx_name)  # Usamos la variable rx_name

    print(rx_info(rx_img))

    # Ejecutamos las funciones
    img_en = rx_enhance(rx_img)
    img_eq = rx_equalize(img_en)  # Podemos encadenar procesos
    img_sh = rx_shaper(img_eq)
    show_rx_comparativa(rx_img, img_en, img_eq,img_sh)

    print("¡Procesamiento completado con éxito!")
except FileNotFoundError:
    print("No se encontró el archivo. Asegúrate de incluir la extensión (.jpg, .png).")
