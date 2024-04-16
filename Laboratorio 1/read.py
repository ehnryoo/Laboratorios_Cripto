from scapy.all import rdpcap
import re

# Función para descifrar un mensaje con cifrado César
def descifrar_cesar(texto, corrimiento):
    texto_descifrado = ""
    for char in texto:
        if char.isalpha():
            if char.islower():
                texto_descifrado += chr((ord(char) - 97 - corrimiento) % 26 + 97)
            else:
                texto_descifrado += chr((ord(char) - 65 - corrimiento) % 26 + 65)
        else:
            texto_descifrado += char
    return texto_descifrado

# Cargar el archivo pcapng
cesar_pcapng = "cesar.pcapng"
paquetes = rdpcap(cesar_pcapng)

# Extraer el mensaje transmitido de los paquetes ICMP
mensaje_transmitido = ""
for paquete in paquetes:
    if paquete.haslayer("ICMP"):
        datos = paquete[3].load  # Suponiendo que los datos estén en la capa 3
        mensaje_transmitido += datos.decode()

# Descifrar el mensaje transmitido con todas las combinaciones posibles de corrimiento
for corrimiento in range(1, 26):
    mensaje_descifrado = descifrar_cesar(mensaje_transmitido, corrimiento)
    # Aquí puedes agregar cualquier método adicional para validar si el mensaje descifrado es el correcto
    # Por ejemplo, puedes buscar palabras clave específicas en el mensaje descifrado
    # o utilizar expresiones regulares para buscar un patrón específico en el mensaje
    # Luego, puedes imprimir el mensaje descifrado si cumple con tus criterios de validación


