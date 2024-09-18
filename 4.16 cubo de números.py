print("Programa para calcular el cubo de los números ingresados por el usuario.")
cantidad_numeros = int(input("¿Cuántos números desea ingresar?: "))

cubos = []

for j in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {j + 1}: "))
    cubo = numero ** 3
    cubos.append(cubo)

print("Los cubos de los números ingresados son:")
for j, cubo in enumerate(cubos):
    print(f"Número {j + 1}: {cubo}")
