ip_address = input("Введите IP-адрес: ")

# Разделяем IP-адрес на отдельные октеты
octets = ip_address.split(".")

# Проверяем класс IP-адреса
first_octet = int(octets[0])

if first_octet >= 1 and first_octet <= 127:
    print("unicast")
elif first_octet >= 128 and first_octet <= 191:
    print("unicast")
elif first_octet >= 192 and first_octet <= 223:
    print("unicast")
elif first_octet >= 224 and first_octet <= 239:
    print("multicast")
elif ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
