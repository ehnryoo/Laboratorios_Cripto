from scapy.all import IP, ICMP, send

# Parámetros 
destination_ip = "8.8.8.8"
string_to_send = "larycxpajorj h bnpdarmjm nw anmnb"

# Creación del paquete ICMP (un paquete por cada caracter)
for i, char in enumerate(string_to_send):
    icmp_id = 12345
    icmp_seq = i + 1
    payload = char.encode() + b'\x00' * (48 - 1)
    icmp_packet = IP(dst=destination_ip) / ICMP(type=8, code=0, id=icmp_id, seq=icmp_seq) / payload

    # Envío del paquete
    send(icmp_packet, verbose=False)
    print(".", end="", flush=True)

# Confirmación de envíos exitosos
print(f"\nSe han enviado {len(string_to_send)} paquetes iCMP con el mensaje \n'{string_to_send}'")