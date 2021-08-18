import os, platform
#lol
def ip():
    os.system("clear")
    os.system('pip2 install requests')
    bit=platform.architecture()[0]
    if bit=="64bit":
        import ipb
        ipb.menu()
    elif bit=="32bit":
        import ips
        ips.menu()
ip()#INSTALLING IPS
