# Ejercicio 1
def numero_mayor(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

# Prueba
numeros = [3, 9, 4, 1, 15]
print("El mayor es:", numero_mayor(numeros))

#*********************************************

# Ejercicio 2
numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#*********************************************

# Ejercicio 3
def lista_unicos(lista):
    return sorted(list(set(lista)))

# Ejemplo
entrada = [4, 2, 7, 4, 2, 1, 9, 7]
print("Lista de entrada: ", entrada)
print("Lista ordenada sin repetir:", lista_unicos(entrada))

#*********************************************

# Ejercicio 4
estudiantes = {}
while True:
    nombre = input("Nombre: ")
    if nombre.lower() == 'fin':
        break
    nota = float(input(f"Nota de {nombre}: "))
    estudiantes[nombre] = nota

print("Datos almacenados:", estudiantes)

#*********************************************

# Ejercicio 5
ventas = {
    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Cantidad': [10, 5, 7, 3, 2, 8]
}

resultado = {}

for i in range(len(ventas['Producto'])):
    producto = ventas['Producto'][i]
    cantidad = ventas['Cantidad'][i]
    
    if producto in resultado:
        resultado[producto] += cantidad
    else:
        resultado[producto] = cantidad

print("Ventas totales:", resultado)

