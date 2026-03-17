#funciones --bloques de codigo que realize una tarea especifica
# funcio n sin parametros
def saludar():
    print("hola bienvenido al curso de python")

# funcion con parametros
def saludo(nombre):
    print("hola "+nombre+" bienvenido a clases")
# funcion q devuelve valores
def suma (a,b):
    return a+b


# establecer valores x defecto para los parametros de una funcion

def bienvenida (nombre="estudiante"):
    print("bienvenido",nombre)

# funcion con argumentos variables

def sumador (*args):
    return sum(args)
# llamda a la funcion
saludo("bruno dias")
saludo("ricardo tapia")

resultado=suma(10,20)
print("la suma es :",resultado)

bienvenida()
bienvenida("susana")

print(sumador(1,2,3,4,5))
print(sumador(4,5,6))