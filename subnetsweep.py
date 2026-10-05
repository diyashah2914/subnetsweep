import ipaddress
import subprocess

# # 192.168.56.1/24
# # create addresses:
# # IPv4Address
# ipaddress.ip_address('192.0.2.1')

# # addresses can also be created directly from integers.
# # Values that will fit within 32 bits are assumed to be IPv4 addresses
# print(ipaddress.ip_address(3221225985))

# # To force the use of IPv4 or IPv6 addresses, the relevant classes can be invoked directly.
# # This is particularly useful to force creation of IPv6 addresses for small integers:

# print(ipaddress.ip_address(1))
# print(ipaddress.IPv4Address(1))
# print(ipaddress.IPv6Address(1))

# print(ipaddress.ip_network('192.0.2.0/24'))

# a var to contain an ip network address. ip network always has 0 in its 4th octet.
subnet_string = ipaddress.ip_network('192.168.56.0/24')


def ping_host(ip):
    command = ["ping", "-n", "1", "-w", "1000", str(ip)]
    result = subprocess.run(
        command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        return True
    return False


live_hosts = []

for i in subnet_string.hosts():
    if ping_host(i):
        print(i)
        live_hosts.append(i)
    continue

print(live_hosts)

ports = [21, 22, 23, 25, 53, 80, 110, 443, 3389, 8080]
