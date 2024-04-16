# pingv4.py

from scapy.all import IP, ICMP, send

# Parámetros
destination_ip = "8.8.8.8"
string_to_send = "larycxpajorj h bnpdarmjm nw anmnb"

# Creación de arreglo de paquetes ICMP
icmp_id = 12345
icmp_packets = [
    IP(dst=destination_ip) / ICMP(type=8, code=0, id=icmp_id, seq=i+1) / (char.encode() + b'\x00' * (48 - 1))
    for i, char in enumerate(string_to_send)
]

# Envío de los paquetes ICMP
send(icmp_packets, verbose=False)

# Confirmación de envíos exitosos
print(f"Se han enviado {len(string_to_send)} paquetes ICMP con el mensaje:\n'{string_to_send}'")




