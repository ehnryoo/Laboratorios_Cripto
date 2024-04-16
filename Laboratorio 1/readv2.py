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

# Función para determinar la probabilidad de un mensaje descifrado
def evaluar_probabilidad(mensaje_descifrado):
    # Contamos la frecuencia de cada letra en el mensaje descifrado
    frecuencias = {}
    for char in mensaje_descifrado:
        if char.isalpha():
            frecuencias[char] = frecuencias.get(char, 0) + 1
    
    # Encontramos la letra más frecuente
    letra_mas_frecuente = max(frecuencias, key=frecuencias.get)
    
    # Retornamos el mensaje descifrado y la letra más frecuente
    return mensaje_descifrado, letra_mas_frecuente

print("Opciones -->")
for corrimiento in range(1, 26):
    mensaje_descifrado = descifrar_cesar(mensaje_transmitido, corrimiento)    
    print(f"{corrimiento}: {mensaje_descifrado}")

eleccion = int(input("\nEscoger opción: "))

for corrimiento in range(1, 26):
    mensaje_descifrado = descifrar_cesar(mensaje_transmitido, corrimiento)    
    if corrimiento == eleccion:
        print(f"Opción escogida: \033[92m{mensaje_descifrado}\033[0m")   

        
