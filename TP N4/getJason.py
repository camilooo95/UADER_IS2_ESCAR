# Compiled at: 2023-06-10 18:15:55
import sys
from SingletonGetJson import SingletonGetJson

Version = "{0.1}"
Filename = "sitedata"
arg = sys.argv

if len(arg) == 1:
    s = SingletonGetJson()

    tk = input("Ingrese el token: ")

    try:
        clave = s.getToken(tk)
        print(Version + " " + clave)
        print()
        print('(“copyright IS2 © 2022,2023 todos los derechos reservados).')
    except BaseException:
        print("Error al mostrar el token")
        print()
        print('(“copyright IS2 © 2022,2023 todos los derechos reservados).')

elif arg[1] in ["-h", "--help"]:
    print("Ejemplo de uso")
    print("Ingrese token1")
    print(Version + "XXXX-XXXX-XXXX-XXXX")

    print("")
    print("El archivo json 'sitedata.json'")
    print("debera encontrarse en la misma carpeta de este mismo programa")
    print("En caso de no encontrarse este archivo")
    print("o de que haya algun error al intentar abrirlo aparecera el siguiente mensaje")
    print("Ups, hubo un error al intentar abrir el archivo sitedata.json")
    print('(“copyright IS2 © 2022,2023 todos los derechos reservados).')

    print("")
    print("Si al cargar los datos del json, estan en un formato que no corresponda")
    print("o de cualquier otro error respecto a esto se mostrara el siguiente mensaje")
    print("Error, no se pudieron cargar los datos de " + Filename)

    print("")
    print("printToken recibe los siguiente argumentos printToken(token, json)")
    print("La funcion 'printToken' imprime un token especificado, si este no esta imprimira el siguiente mensaje")
    print("el token " + "'token ingresado por el usuario'" + " no existe")
