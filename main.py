import random
import string

# Función para evaluar la seguridad de la contraseña
def evaluar_seguridad(contrasena):
    longitud = len(contrasena)
    tiene_letras = any(c.isalpha() for c in contrasena)
    tiene_numeros = any(c.isdigit() for c in contrasena)
    tiene_simbolos = any(c in string.punctuation for c in contrasena)

    if longitud >= 12 and tiene_letras and tiene_numeros and tiene_simbolos:
        return "Fuerte"
    elif longitud >= 8 and tiene_letras and tiene_numeros:
        return "Media"
    else:
        return "Débil"


# Función para generar la contraseña
def generar_contrasena(longitud, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_letters

    if incluir_numeros == "s":
        caracteres += string.digits

    if incluir_simbolos == "s":
        caracteres += string.punctuation

    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


# Programa principal
print("====================================")
print(" GENERADOR SEGURO DE CONTRASEÑAS")
print("====================================")

continuar = "s"

while continuar == "s":
    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))

        if longitud <= 0:
            print("La longitud debe ser mayor a 0.")
        else:
            incluir_numeros = input("¿Desea incluir números? (s/n): ").lower()
            incluir_simbolos = input("¿Desea incluir símbolos? (s/n): ").lower()

            contrasena = generar_contrasena(longitud, incluir_numeros, incluir_simbolos)
            seguridad = evaluar_seguridad(contrasena)

            print("\nContraseña generada:", contrasena)
            print("Nivel de seguridad:", seguridad)

    except ValueError:
        print("Error: debe ingresar un número válido.")

    continuar = input("\n¿Desea generar otra contraseña? (s/n): ").lower()

print("\nGracias por usar el generador de contraseñas seguras.")