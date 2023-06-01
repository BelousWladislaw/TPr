ospf_route = 'OSPF 10.0.24.0/24 110/41 10.0.13.3, 3d18h, FastEthernet0/0'
info_route = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
ospf_route = list(ospf_route.strip().split())
info_route = dict(zip(info_route, ospf_route))
print(info_route)