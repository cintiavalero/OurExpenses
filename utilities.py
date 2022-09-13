# LIBRERIA DE utilities

import platform, os, random, string, signal, time

# CTRL + O - PARA HACER ZOOM

#-------------------------------------------------------------------------------------------------------
#   LIMPIAR PANTALLA
#-------------------------------------------------------------------------------------------------------
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
#-------------------------------------------------------------------------------------------------------
#   CAMBIAR TITULO CMD
#-------------------------------------------------------------------------------------------------------
# os.system("Titulo nuevo")
def tituloConsola(titulo):
    comando = "title " + titulo
    os.system(comando)
#-------------------------------------------------------------------------------------------------------
#   CTRL+C 
#-------------------------------------------------------------------------------------------------------
# funcion handler
def handler(signum, frame):
    print("\nCtrl-C detectado. Finalizando la ejecucion...\n")
    time.sleep(0.2)
    exit()
# llamo a la funcion handler
def callHandler(): signal.signal(signal.SIGINT, handler)
#-------------------------------------------------------------------------------------------------------
#   GENERADOR DE CODIGOS
#-------------------------------------------------------------------------------------------------------
def codRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(tamanio_cadena))
    return x
def codMayusRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.ascii_uppercase) for _ in range(tamanio_cadena))
    return x
def codMinusRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.ascii_lowercase) for _ in range(tamanio_cadena))
    return x
def codLetrasRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.ascii_letters) for _ in range(tamanio_cadena))
    return x
def codExaRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.hexdigits) for _ in range(tamanio_cadena))
    return x
def codNumRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.digits) for _ in range(tamanio_cadena))
    return x
#-------------------------------------------------------------------------------------------------------
# MANEJO DE ERRORES
#-------------------------------------------------------------------------------------------------------
def ManejoDeErrores(modulo):
    try:
        modulo
    except Exception as ex:
        print("\n>>>>> ERROR >>>>>", ex)
        input()
#-------------------------------------------------------------------------------------------------------
# MOSTRAR TITULO EN PANTALLA
#-------------------------------------------------------------------------------------------------------
def setTittle(titulo, char):
    l = len(titulo)
    print(char*l)
    print(titulo)
    print(char*l)