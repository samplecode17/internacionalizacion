
import gettext

import locale



# Configuración de gettext
locale.setlocale(locale.LC_ALL, '')  # Configura la localización del sistema
lang = locale.getdefaultlocale()[0][:2]  # Detecta el idioma del sistema (p.ej., 'en', 'ca')
translations = gettext.translation('traduction', localedir='locale', languages=[lang], fallback=True)
translations.install()
_ = translations.gettext  # Alias para simplificar el uso de traducciones

# Concatenar dos cadenas
def concatenar(cadena1, cadena2):
    return cadena1 + cadena2

# Cambiar a mayúsculas
def cambiar_mayusculas(cadena):
    return cadena.upper()

# Cambiar a minúsculas
def cambiar_minusculas(cadena):
    return cadena.lower()

# Contar caracteres
def contar_caracteres(cadena):
    return len(cadena)

# Buscar palabra o carácter
def buscar(cadena, palabra):
    if palabra in cadena:
        return _("'{palabra}' se encuentra en la posición {pos}").format(palabra=palabra, pos=cadena.find(palabra))
    else:
        return _("'{palabra}' no se encuentra en la cadena.").format(palabra=palabra)

# Reemplazar palabra o carácter
def reemplazar(cadena, antiguo, nuevo):
    return cadena.replace(antiguo, nuevo)

# Dividir la cadena
def dividir(cadena, delimitador=" "):
    return cadena.split(delimitador)
