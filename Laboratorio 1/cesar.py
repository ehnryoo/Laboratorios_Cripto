# cesar.py

# Función Cifrado Cesar
def cesar(texto, corrimiento):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            if char.islower():
                texto_cifrado += chr((ord(char) - 97 + corrimiento) % 26 + 97)
            else:
                texto_cifrado += chr((ord(char) - 65 + corrimiento) % 26 + 65)
        else:
            texto_cifrado += char
    return texto_cifrado

# Ingresar texto
entrada = input()
entrada_split = entrada.split('"')
texto = entrada_split[1]

# Ingresar corrimiento
corrimiento = int(entrada_split[-1])

# Texto crifrado
output = cesar(texto, corrimiento)
print(output)

