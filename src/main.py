import os

from operations import *
import gettext
import locale




# Configura la localización del sistema
locale.setlocale(locale.LC_ALL, '')
# Detecta el idioma del sistema (p.ej., 'en', 'ca')
lang = os.getenv('LANGUAGE', locale.getdefaultlocale()[0][:2])
translations = gettext.translation('traduction', localedir='locale', languages=[lang], fallback=True)
translations.install()

# Alias para simplificar el uso de traducciones
_ = translations.gettext


# Función para mostrar el menú
def menu():
    print("\n" + _("Seleccione una operación con cadenas:"))
    print("1.", _("Concatenar dos cadenas"))
    print("2.", _("Cambiar a mayúsculas"))
    print("3.", _("Cambiar a minúsculas"))
    print("4.", _("Contar caracteres"))
    print("5.", _("Buscar palabra o carácter"))
    print("6.", _("Reemplazar palabra o carácter"))
    print("7.", _("Dividir la cadena"))
    print("8.", _("Salir"))


# Función main para ejecutar el programa principal
def main():
    while True:
        menu()
        opcion = input(_("Seleccione una opción: "))

        if opcion == "1":
            cadena1 = input(_("Ingrese la primera cadena: "))
            cadena2 = input(_("Ingrese la segunda cadena: "))
            print(_("Resultado:"), concatenar(cadena1, cadena2))

        elif opcion == "2":
            cadena = input(_("Ingrese la cadena: "))
            print(_("Resultado:"), cambiar_mayusculas(cadena))

        elif opcion == "3":
            cadena = input(_("Ingrese la cadena: "))
            print(_("Resultado:"), cambiar_minusculas(cadena))

        elif opcion == "4":
            cadena = input(_("Ingrese la cadena: "))
            print(_("Número de caracteres:"), contar_caracteres(cadena))

        elif opcion == "5":
            cadena = input(_("Ingrese la cadena: "))
            palabra = input(_("Ingrese la palabra o carácter a buscar: "))
            print(buscar(cadena, palabra))

        elif opcion == "6":
            cadena = input(_("Ingrese la cadena: "))
            antiguo = input(_("Ingrese la palabra o carácter a reemplazar: "))
            nuevo = input(_("Ingrese el nuevo texto: "))
            print(_("Resultado:"), reemplazar(cadena, antiguo, nuevo))

        elif opcion == "7":
            cadena = input(_("Ingrese la cadena: "))
            delimitador = input(_("Ingrese el delimitador (dejar en blanco para espacio): "))
            if delimitador == "":
                delimitador = " "
            print(_("Resultado:"), dividir(cadena, delimitador))

        elif opcion == "8":
            print(_("Saliendo del programa..."))
            break
        else:
            print(_("Opción no válida, intente nuevamente."))

        input("")


# Llamada a la función main para iniciar el programa
if __name__ == "__main__":
    main()
