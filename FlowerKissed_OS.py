class Paciente:
    def __init__(self, name, age, gender, weight=None, height=None): #tal vez convenga agregar escoalridad, ocupacion previa y ocupacion actual como opcionales
        self.name        = name
        self.age         = age
        self.gender      = gender
        self.weight      = weight
        self.height      = height
        self.vital_signs = None
        self.labs        = {}
        self.history = None

    def BMI(self):
        if self.weight and self.height:
            return round(self.weight / (self.height ** 2), 2)
        return "No weight/height data"

    def add_vital_signs(self, vital_signs):
        self.vital_signs = vital_signs

    def add_lab(self, name, lab):
        self.labs[name] = lab

    def add_history(self, history):
        self.history= history

    def __str__(self):
        lines = ["Patient: {} | Age: {} | Gender: {}".format(self.name, self.age, self.gender)]
        if self.weight and self.height:
            lines.append("BMI: {}".format(self.BMI()))
        if self.vital_signs:
            lines.append(str(self.vital_signs))
        if self.labs:
            for lab_name, lab in self.labs.items():
                lines.append("{}: {}".format(lab_name, str(lab)))
        if self.history:
            lines.append(str(self.history))
        return "\n".join(lines)

    def __repr__(self):
        return "Paciente('{}', {}, '{}', {}, {})".format(
            self.name, self.age, self.gender, self.weight, self.height)

    @classmethod
    def from_input(cls):
        name   = input("Patient name: ")
        age    = int(input("Patient age: "))
        gender = input("Patient gender: ")
        weight = float(input("Patient weight (kg): "))
        height = float(input("Patient height (m): "))
        return cls(name, age, gender, weight, height)


class VitalSigns:
    def __init__(self, bpm, rpm, temp, bp, spo2, glucose):
        self.bpm     = bpm
        self.rpm     = rpm
        self.temp    = temp
        self.bp      = bp
        self.spo2    = spo2
        self.glucose = glucose

    def __str__(self):
        return "BPM: {} | RPM: {} | Temp: {}°C | BP: {} | SpO2: {}% | Glucose: {} mg/dL".format(
            self.bpm, self.rpm, self.temp, self.bp, self.spo2, self.glucose)

    def __repr__(self):
        return "VitalSigns({}, {}, {}, '{}', {}, {})".format(
            self.bpm, self.rpm, self.temp, self.bp, self.spo2, self.glucose)

    @classmethod
    def from_input(cls):
        bpm     = float(input("BPM: "))
        rpm     = float(input("RPM: "))
        temp    = float(input("Temperature (°C): "))
        bp      = input("Blood pressure (e.g. 120/80): ")
        spo2    = float(input("SpO2 (%): "))
        glucose = float(input("Glucose (mg/dL): "))
        return cls(bpm, rpm, temp, bp, spo2, glucose)


class RedBloodCount:
    def __init__(self, hemoglobin, hematocrit, VCM, HCM):
        self.hemoglobin  = hemoglobin
        self.hematocrit  = hematocrit
        self.VCM         = VCM
        self.HCM         = HCM

    def __str__(self):
        return "Hgb: {} g/dL | Hct: {}% | VCM: {} fL | HCM: {} pg".format(
            self.hemoglobin, self.hematocrit, self.VCM, self.HCM)

    def __repr__(self):
        return "RedBloodCount({}, {}, {}, {})".format(
            self.hemoglobin, self.hematocrit, self.VCM, self.HCM)

    @classmethod
    def from_input(cls):
        hemoglobin = float(input("Hemoglobin (g/dL): "))
        hematocrit = float(input("Hematocrit (%): "))
        VCM        = float(input("VCM (fL): "))
        HCM        = float(input("HCM (pg): "))
        return cls(hemoglobin, hematocrit, VCM, HCM)


class WhiteBloodCount:
    def __init__(self, total, neutrophils, basophils, eosinophils, lymphocytes):
        self.total       = total
        self.neutrophils = neutrophils
        self.basophils   = basophils
        self.eosinophils = eosinophils
        self.lymphocytes = lymphocytes

    def __str__(self):
        return "WBC: {} | Neut: {}% | Baso: {}% | Eosino: {}% | Lympho: {}%".format(
            self.total, self.neutrophils, self.basophils, self.eosinophils, self.lymphocytes)

    def __repr__(self):
        return "WhiteBloodCount({}, {}, {}, {}, {})".format(
            self.total, self.neutrophils, self.basophils, self.eosinophils, self.lymphocytes)

    @classmethod
    def from_input(cls):
        total       = float(input("Total leukocytes (x10³/µL): "))
        neutrophils = float(input("Neutrophils (%): "))
        basophils   = float(input("Basophils (%): "))
        eosinophils = float(input("Eosinophils (%): "))
        lymphocytes = float(input("Lymphocytes (%): "))
        return cls(total, neutrophils, basophils, eosinophils, lymphocytes)


class UrineTest:
    def __init__(self, urea, creatinine, leukocytes, bacteria):
        self.urea       = urea
        self.creatinine = creatinine
        self.leukocytes = leukocytes
        self.bacteria   = bacteria

    def __str__(self):
        return "Urea: {} | Creatinine: {} | Leukocytes: {} | Bacteria: {}".format(
            self.urea, self.creatinine, self.leukocytes, self.bacteria)

    def __repr__(self):
        return "UrineTest({}, {}, '{}', '{}')".format(
            self.urea, self.creatinine, self.leukocytes, self.bacteria)

    @classmethod
    def from_input(cls):
        urea       = float(input("Urea (mg/dL): "))
        creatinine = float(input("Creatinine (mg/dL): "))
        leukocytes = input("Leukocytes: ")
        bacteria   = input("Bacteria: ")
        return cls(urea, creatinine, leukocytes, bacteria)


class BloodChemistry:
    def __init__(self, cholesterol, triglycerides, BUN, glucose, urea, creatinine):
        self.cholesterol   = cholesterol
        self.triglycerides = triglycerides
        self.BUN           = BUN
        self.glucose       = glucose
        self.urea          = urea
        self.creatinine    = creatinine

    def __str__(self):
        return "Chol: {} | Trig: {} | BUN: {} | Gluc: {} | Urea: {} | Creat: {}".format(
            self.cholesterol, self.triglycerides, self.BUN,
            self.glucose, self.urea, self.creatinine)

    def __repr__(self):
        return "BloodChemistry({}, {}, {}, {}, {}, {})".format(
            self.cholesterol, self.triglycerides, self.BUN,
            self.glucose, self.urea, self.creatinine)

    @classmethod
    def from_input(cls):
        cholesterol   = float(input("Cholesterol (mg/dL): "))
        triglycerides = float(input("Triglycerides (mg/dL): "))
        BUN           = float(input("BUN (mg/dL): "))
        glucose       = float(input("Glucose (mg/dL): "))
        urea          = float(input("Urea (mg/dL): "))
        creatinine    = float(input("Creatinine (mg/dL): "))
        return cls(cholesterol, triglycerides, BUN, glucose, urea, creatinine)


class History():
    def __init__ (self, motivo, padecimiento_actual, ahf, apnp, app,ago = None,aan= None):
        self.motivo = motivo
        self.padecimiento_actual = padecimiento_actual
        self.ahf = ahf
        self.apnp = apnp
        self.app = app
        self.ago = ago
        self.aan = aan


    def __str__(self):
        return (("motivo: {} \n Padecimiento Actual: {} \n Antecedentes Heredo Familiares: {} \n Antecedentes Personales no patologícos: {} \n "
                "Antecedentes personales patologicos {}, \n Antecedentes Gineco-Obstetricos: {} \n Antedecentes Andrologicos: {} ").format(self.motivo,self.padecimiento_actual, self.ahf, self.apnp, self.app, self.ago, self.aan))

    def indice_tabaquico(self):
        cigarros_dia = int(input("Cigarrillos por día: "))
        años_fumando = int(input("Años fumando: "))
        return cigarros_dia * años_fumando / 20

    @classmethod
    def take_history(cls):
        motivo = input("Causas por las que acude: ")
        padecimiento_actual = input("\n ------Padecimiento Actual------\n"
                                    "Aparición (Fecha y modo de inicio) \n Localización (¿Dónde duele o se siente?) \n "
                                    "Irradiación (¿Hacia dónde se mueve?) \n Característica (¿Es opresivo, punzante, ardoroso?) \n "
                                    "Intensidad (Escala 1-10) \n Atenuantes o Agravantes (¿Qué lo mejora o empeora?):\n ")
        ahf = input("\n ------Antecedentes Heredo Familiares------\n"
                    "Abuelos, padres, tíos, hermanos e hijos. \n "
                    "Diabetes Mellitus, Hipertensión Arterial, Cardiopatías, Neoplasias (cáncer), "
                    "Nefropatías, enfermedades mentales o genéticas. \n "
                    "Si viven o fallecieron (causa y edad del deceso):\n ")
        apnp = input("\n ------Antecedentes Personales No Patologicos------\n"
                     "Vivienda: Tipo de construcción, número de habitantes, servicios básicos (agua, luz, drenaje), "
                     "presencia de animales (zoonosis). \n Higiene: Baño y cambio de ropa (frecuencia), aseo dental. \n "
                     "Alimentación: Frecuencia de grupos alimenticios (proteínas, carbohidratos, verduras) y litros de agua al día. \n "
                     "Tabaquismo: Edad de inicio, cigarrillos al día. \n Alcoholismo: Tipo de bebida, frecuencia, cantidad y si hay pérdida del conocimiento. \n"
                     " Toxicomanías: Sustancia, vía de administración, frecuencia y última dosis. \n "
                     "Inmunizaciones: Esquema de vacunación completo o incompleto (especificar refuerzos recientes como Influenza o COVID-19).:\n ")
        app = input("\n ------Antecedentes Personales Patologicos------\n"
                    "Enfermedades de la infancia: Sarampión, rubeola, varicela, parotiditis, etc. (incluir secuelas).\n"
                    "Enfermedades crónico-degenerativas: Diagnóstico, tiempo de evolución, tratamiento actual y grado de control.\n"
                    "Antecedentes Quirúrgicos: Tipo de cirugía, fecha, motivo, técnica, complicaciones trans/postoperatorias y hospital donde se realizó.\n"
                    "Antecedentes Traumáticos: Fracturas, esguinces o luxaciones (mecanismo de lesión, tratamiento y secuelas funcionales).\n"
                    "Antecedentes Alérgicos: Fármacos, alimentos, sustancias ambientales o látex (especificar tipo de reacción: rash, anafilaxia, etc.)\n"
                    "Antecedentes Transfusionales: Tipo de hemoderivado, fecha, cantidad y si hubo reacciones febriles o hemolíticas.\n"
                    "Hospitalizaciones previas: Motivo, fecha y duración.:\n ")
        ago = input("\n ------Antecedentes GinecoObstetricos------\n"
                    "Menarquia \n"
                    " ritmo menstrual (días/ciclo)\n "
                    "Fecha de Última Menstruación (FUM) \n "
                    "Inicio de Vida Sexual Activa (IVSA) \n"
                    "número de parejas \n"
                    " GESTAS (G: embarazos, P: partos, C: cesáreas, A: abortos) \n"
                    "métodos anticonceptivos \n"
                    " última citología (Papanicolaou) \n"
                    "última mastografía \n"
                    "Enfermedades de Transmisión Sexual (ETS): Cuáles, cuándo y si recibió tratamiento completo: \n ")
        aan = input("\n ------Antecedentes Andrologicos------\n"
                    "Inicio de Vida Sexual Activa (IVSA) \n"
                    "Métodos anticonceptivos: Uso de preservativo (siempre, a veces, nunca) y vasectomía (fecha).\n"
                    "Enfermedades de Transmisión Sexual (ETS): Cuáles, cuándo y si recibió tratamiento completo \n "
                    "Función Sexual: Calidad de la erección (logro y mantenimiento) y trastornos de la eyaculación (precoz o retardada).\n"
                    "Somas Prostáticos: Dificultad para iniciar la micción, chorro débil, goteo o necesidad de orinar muchas veces de noche (nicturia).\n"
                    "Autoexploración Testicular: Presencia de masas, dolor o inflamación en el escroto:\n ")
        return cls (motivo, padecimiento_actual, ahf, apnp, app,ago,aan)


if __name__ == "__main__":

    # 1. Crear paciente
    p1 = Paciente.from_input()

    # 2. Signos vitales
    print("\n--- Signos Vitales ---")
    p1.add_vital_signs(VitalSigns.from_input())

    # 3. Historia clínica
    print("\n--- Historia Clínica ---")
    p1.add_history(History.take_history())

    # 4. Labs — el usuario elige cuáles agregar
    print("\n--- Laboratorios ---")
    labs_disponibles = {
        "1": ("BHC", RedBloodCount),
        "2": ("BLC", WhiteBloodCount),
        "3": ("QS",  BloodChemistry),
        "4": ("EGO", UrineTest),
    }

    while True:
        print("\n¿Qué laboratorio deseas agregar?")
        print("1. BHC  2. BLC  3. QS  4. EGO  0. Terminar")
        opcion = input("Opción: ")

        if opcion == "0":
            break
        elif opcion in labs_disponibles:
            nombre, clase = labs_disponibles[opcion]
            p1.add_lab(nombre, clase.from_input())
        else:
            print("Opción no válida")

    # 5. Imprimir resumen
    print("\n========= RESUMEN DEL PACIENTE =========")
    print(p1)