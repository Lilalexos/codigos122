class Persona:
    totalPersonas = 0
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.totalPersonas +=1
    
    def saludar(self):
        print(f"hola, mi nombre es {self.nombre} y tengo {self.dad} años.")

class estudiante(Persona):
    contadorestudiantes = 0
    
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        estudiante.contadorestudiantes += 1
    
    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")

class Trabajador():
    totalTrabajadores = 0
    
    def __init__(self, nombre, edad, cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        Trabajador.totalTrabajadores += 1
    
    def mostrar_info_trabajador(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Cargo: {self.cargo}")

class estudianteTrabajador(Estudiante, Trabajador):
    estudianteTrabajador = 0
    def __init__(self, nombre, edad, carrera, cargo):
        estudiante.__init__(self, nombre, edad, carrera)
        Trabajador.__init__(self, nombre, edad, cargo)
        estudiante.EstudianteTrabajador =+1
        

persona1 = Persona("jorge torres", 30)
persona2 = Persona("brayam  velez", 28)
estudiante1 = estudiante(" daniel ruiz", 27, "Contaduria ")
estudiante2 = estudiante("sofia  Palacios", 30, "Licenciatura")
trabajador1 = Trabajador("sebastian Paez", 25, "Ingeniero")
trabajador2 = Trabajador("Lina Tejeiro", 35, "Secretaria")
estudiante_trabajador3 = estudianteTrabajador("valentina Alarcon", 22, "Matematico", "Profesor")
a = estudiante.contadorEstudiantes
b = Trabajador.totalTrabajadores
c = estudiante.estudianteTrabajador
totalpersonas = a+b+c 
persona1.saludar()
estudiante1.imprimir_informacion()
trabajador1.mostrar_info_trabajador()

persona2.saludar()
estudiante2.imprimir_informacion()
trabajador2.mostrar_info_trabajador()

estudiante_trabajador3.mostrar_info_trabajador()
estudiante_trabajador3.imprimir_informacion()

print(f"Total de personas: {totalpersonas}")
print(f"Total de estudiantes: {estudiante.contadorEstudiantes}")
print(f"Total de trabajadores: {Trabajador.totalTrabajadores}")
print(f"Total de estudiantes trabajadores: {estudiante.estudianteTrabajador}")
