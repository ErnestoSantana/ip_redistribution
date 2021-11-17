import os.path
import random

strPath = os.path.dirname(__file__)


# Generate random ip octet
def random_value():
    return random.sample(range(0, 256), 1)[0]


######################################################
# (Optional) Generate IPs file to read
######################################################
input_len_ip = input("Enter number of IP addresses: ")


def generate_txt_ip(len_ip):
    try:
        while not len_ip.isnumeric():
            print("Enter only whole numbers")
            len_ip = input("Enter number of IP addresses: ")
    except ValueError as e:
        print(e)

    ip = str()
    ip_list = list()

    for e in range(int(len_ip)):
        ip = f'{random_value()}.{random_value()}.{random_value()}.{random_value()}'
        ip_list.append(ip)

    with open(strPath + "/text_ip_input.txt", "w") as f:
        for ips in ip_list:
            f.write(ips + '\n')


generate_txt_ip(input_len_ip)
######################################################

# READ TEXT FILE (text_ip_input.txt)
with open(strPath + "/text_ip_input.txt") as f:
    a = f.read()
    ip_read = a.strip().split('\n')

# WRITE NEW TEXT FILE (text_ip_output.txt)
with open(strPath + "/text_ip_output.txt", "w") as f:
    f.write("config firewall address")
    datacenter = 1
    count = 0
    for i in ip_read:
        count += 1
        f.write(f'''
        edit group.{ip_read.index(i) + 1}
        set subnet {i}/32
        end
        config firewall addrgrp
        edit datacenter.{datacenter}
        append member group.{ip_read.index(i) + 1}
        end''')
        if count > 299:
            datacenter += 1
            count = 0

print("Process finished successfully")
