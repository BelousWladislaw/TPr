command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlans1 = command1.strip().split()[-1].split(',')
vlans2 = command2.strip().split()[-1].split(',')

print(set(vlans1) & set(vlans2))






