import curses

# Definición del mensaje transmitido
mensaje_transmitido = "larycxpajorj h bnpdarmjm nw anmnb"

# Función para descifrar un mensaje con cifrado César
def descifrar_cesar(mensaje, corrimiento):
    mensaje_descifrado = ""
    for char in mensaje:
        if char.isalpha():
            if char.islower():
                mensaje_descifrado += chr((ord(char) - 97 - corrimiento) % 26 + 97)
            else:
                mensaje_descifrado += chr((ord(char) - 65 - corrimiento) % 26 + 65)
        else:
            mensaje_descifrado += char
    return mensaje_descifrado

# Función para mostrar las opciones en la terminal y permitir al usuario seleccionar una opción
def seleccionar_opcion(opciones):
    curses.wrapper(_seleccionar_opcion, opciones)

def _seleccionar_opcion(stdscr, opciones):
    # Configurar la terminal
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Inicializar variables
    opcion_seleccionada = 0
    num_opciones = len(opciones)

    # Ciclo principal
    while True:
        stdscr.clear()

        # Mostrar las opciones
        for i, opcion in enumerate(opciones):
            if i == opcion_seleccionada:
                stdscr.addstr(i, 0, opcion, curses.color_pair(1))
            else:
                stdscr.addstr(i, 0, opcion)

        stdscr.refresh()

        # Obtener entrada del usuario
        key = stdscr.getch()

        # Procesar la entrada del usuario
        if key == curses.KEY_DOWN:
            opcion_seleccionada = (opcion_seleccionada + 1) % num_opciones
        elif key == curses.KEY_UP:
            opcion_seleccionada = (opcion_seleccionada - 1) % num_opciones
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break

    # Devolver la opción seleccionada
    return opcion_seleccionada

# Descifrar el mensaje transmitido con todas las combinaciones posibles de corrimiento
opciones = []
for corrimiento in range(1, 26):
    mensaje_descifrado = descifrar_cesar(mensaje_transmitido, corrimiento)
    opciones.append(mensaje_descifrado)

# Seleccionar la opción más probable
indice_opcion_seleccionada = seleccionar_opcion(opciones)

# Mostrar la opción seleccionada
print("La opción seleccionada es:")
print(opciones[indice_opcion_seleccionada])
