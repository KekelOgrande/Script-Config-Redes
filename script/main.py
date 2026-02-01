import os

def dhcp():
    
    print("\n" * os.get_terminal_size().lines)
    print('='*35)
    print('O dhcp será com sub-interface? S/N')
    print('='*35)
    escolha_dhcp = input('\n> ').lower()
    if escolha_dhcp == "s":
        print("\n" * os.get_terminal_size().lines)
        print('='*41)
        print('Qual Vlan irá passar nessa sub-interface?')
        print('='*41)
        vlan1 = int(input('\n> '))
        
        print("\n" * os.get_terminal_size().lines)
        print('='*65)
        print('Qual será a porta do roteador que ira fazer o link? Ex: g0/0 ou g0/1')
        print('='*65)
        porta_roteador1 = input('\n> ')

        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Qual será o ip dessa porta?')
        print('='*40)
        ip1 = input('\n> ')
        
        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Qual será a mascara de ip?')
        print('='*40)
        mascara_ip1 = input('\n> ')

        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Qual será o nome do dhcp?')
        print('='*40)
        nome_dhcp1 = input('\n> ')

        network_preparando1 = ip1[:-1]
        network_pronta1 = network_preparando1 + "0"
        
        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Adicionar outra vlan? S/N')
        print('='*40)
        vlan_adicional = input('\n> ').lower()

        if vlan_adicional == "s":

            print("\n" * os.get_terminal_size().lines)
            print('='*41)
            print('Qual Vlan irá passar nessa sub-interface?')
            print('='*41)
            vlan2 = int(input('\n> '))
            
            print("\n" * os.get_terminal_size().lines)
            print('='*65)
            print('Qual será a porta do roteador que ira fazer o link? Ex: g0/0 ou g0/1')
            print('='*65)
            porta_roteador2 = input('\n> ')
            
            print("\n" * os.get_terminal_size().lines)
            print('='*40)
            print('Qual será o ip dessa porta?')
            print('='*40)
            ip2 = input('\n> ')
            
            print("\n" * os.get_terminal_size().lines)
            print('='*40)
            print('Qual será a mascara de ip?')
            print('='*40)
            mascara_ip2 = input('\n> ')
            
            print("\n" * os.get_terminal_size().lines)
            print('='*40)
            print('Qual será o nome do dhcp?')
            print('='*40)
            nome_dhcp2 = input('\n> ')

            network_preparando2 = ip2[:-1]
            network_pronta2 = network_preparando2 + "0"

            with open('script_dhcp.txt','w') as arquivo:
                arquivo.write(f'''en
conf t
int {porta_roteador1}.{vlan1}
encapsulation dot1Q {vlan1}
ip add {ip1} {mascara_ip1}
no shut
int {porta_roteador1}
no shut
exit
ip dhcp pool {nome_dhcp1}
network {network_pronta1} {mascara_ip1}
default-router {ip1}
exit
exit
exit

en
conf t
int {porta_roteador2}.{vlan2}
encapsulation dot1Q {vlan2}
ip add {ip2} {mascara_ip2}
no shut
int {porta_roteador2}
no shut
exit
ip dhcp pool {nome_dhcp2}
network {network_pronta2} {mascara_ip2}
default-router {ip2}
exit
exit
exit
    ''')

        elif vlan_adicional == "n":

            print("\n" * os.get_terminal_size().lines)
            with open('script_dhcp.txt','w') as arquivo:
                arquivo.write(f'''en
conf t
int {porta_roteador1}.{vlan1}
encapsulation dot1Q {vlan1}
ip add {ip1} {mascara_ip1}
no shut
int {porta_roteador1}
no shut
exit
ip dhcp pool {nome_dhcp1}
network {network_pronta1} {mascara_ip1}
default-router {ip1}
''')

    elif escolha_dhcp == "n":

        print("\n" * os.get_terminal_size().lines)
        print('='*65)
        print('Qual será a porta do roteador que fara o link? Ex: g0/0 ou g0/1')
        print('='*65)
        porta_roteador = input('\n> ')

        print("\n" * os.get_terminal_size().lines)
        print('='*51)
        print('Qual será o ip dessa porta?')
        print('='*51)
        ip = input('\n> ')

        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Qual será a mascara de ip?')
        print('='*40)
        mascara_ip = input('\n> ')

        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Qual será o nome do dhcp?')
        print('='*40)
        nome_dhcp = input('\n> ')
        
        
        network_preparando = ip[:-1]
        network_pronta = network_preparando + "0"

        print("\n" * os.get_terminal_size().lines)
        print('\nSCRIPT PRONTO')
        with open('script_dhcp.txt','w') as arquivo:
            arquivo.write(f'''en
conf t
int {porta_roteador}
ip add {ip} {mascara_ip}
no shut
exit
int {porta_roteador}
no shut
ip dhcp pool {nome_dhcp}
network {network_pronta} {mascara_ip}
default-router {ip}
''')

def vlan():

    print("\n" * os.get_terminal_size().lines)
    print('='*40)
    print('Qual será o número da Vlan?')
    print('='*40)
    numero_vlan1 = int(input("\n> "))

    print("\n" * os.get_terminal_size().lines)
    print('='*40)
    print('Digite a primeira porta do range')
    print('='*40)
    p1_vlan_inicio = int(input('\n> '))

    print("\n" * os.get_terminal_size().lines)
    print('='*40)
    print('Agora Digite a ultima porta do range')
    print('='*40)
    p1_vlan_final = int(input("\n> "))

    print("\n" * os.get_terminal_size().lines)
    print('='*51)
    print('Qual porta será o link do switch para o roteador?')
    print('='*51)
    porta_link = int(input("\n> "))

    print("\n" * os.get_terminal_size().lines)
    print('='*40)
    print('Adicionar outra vlan? S/N')
    print('='*40)
    pergunta_vlan = input('\n> ').lower()

    if pergunta_vlan == "s":

        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Qual será o número da Vlan?')
        print('='*40)
        numero_vlan2 = int(input("\n> "))

        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Digite a primeira porta do range')
        print('='*40)
        p2_vlan_inicio = int(input('\n> '))

        print("\n" * os.get_terminal_size().lines)
        print('='*40)
        print('Agora digite a ultima porta do range:')
        print('='*40)
        p2_vlan_final = int(input("\n> "))

        with open (f'script_vlan{numero_vlan2}.txt','w') as arquivo:
                    arquivo.write(f'''en
conf t
vlan {numero_vlan1}
exit
interface range f0/{p1_vlan_inicio} - {p1_vlan_final}
switchport mode access
switchport access vlan {numero_vlan1}
exit
exit
exit

en
conf t
vlan {numero_vlan2}
exit
interface range f0/{p2_vlan_inicio} - {p2_vlan_final}
switchport mode access
switchport access vlan {numero_vlan2}
exit
int f0/{porta_link}
switchport mode trunk
switchport trunk allowed vlan {numero_vlan1},{numero_vlan2}
exit
exit
exit
''')

    elif pergunta_vlan == "n":
        with open (f'script_vlan{numero_vlan1}.txt','w') as arquivo:
            arquivo.write(f'''en
conf t
vlan {numero_vlan1}
exit
interface range f0/{p1_vlan_inicio} - {p1_vlan_final}
switchport mode access
switchport access vlan {numero_vlan1}
exit
int f0/{porta_link}
switchport mode trunk
switchport trunk allowed vlan {numero_vlan1}
exit
''')

print("\n" * os.get_terminal_size().lines)
print('''
┌───────────────────────────────────────────────────┐
│ ____            _       _     _  __    _        _ │
│/ ___|  ___ _ __(_)_ __ | |_  | |/ /___| | _____| |│
│\___ \ / __| '__| | '_ \| __| | ' // _ \ |/ / _ \ |│
│ ___) | (__| |  | | |_) | |_  | . \  __/   <  __/ |│
│|____/ \___|_|  |_| .__/ \__| |_|\_\___|_|\_\___|_|│
│                  |_|                              │
└───────────────────────────────────────────────────┘             
''')
print("="*25)
print('Qual será a configuração?')
print('='*25)
escolha = input("- DHCP\n- VLAN\n\n> ").lower()
if escolha == "dhcp":
    dhcp()
elif escolha == "vlan":
    vlan()
else:
    print("\nOpção inexistente!!!\n")