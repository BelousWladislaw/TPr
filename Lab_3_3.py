CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

comands = CONFIG.split()
vlans = comands[-1].split(',')

print(vlans)
