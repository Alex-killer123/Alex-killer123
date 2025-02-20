import subprocess
import platform
# subprocess is used for terminal prompt
# platform is used for system uname
# muzi -h for more informations and options
print("$ muzi -h")
print("") # for more space
# the icon of muzi is a popular icon for make tools
print("|\\    /|  muzi version(1.0)")
print("| \\  / |  muzi is a tool for get osint-information")
print("|  \\/  |  https://github.com/alex-anonymous/muzi")
print("|      |  This script checks file permissions!")

print("")
print("""libpcap version 1.0.0 (with TPACKET_V3)
OpenSSL 3.3.2 3 Sep 2025
64-bit build, 64-bit time_t""")
####################################################
print("--------------------------------------------------")
print("(-a)                         [for see all options]")
print("(-r)                         [for get hostname]")
print("(-p)                         [for network settings]")
print("(-s)                         [for know operator system]")
print("(-V)                         [see version muzi]")
print("--------------------------------------------------")
n = 0
while n != 1:
    prompt = input("prompt: ") # for enter prompt in system
    if prompt.lower() == "muzi -a":
        print("""
(-a)                         [for see all options]
(-h)                         [helping from muzi]
(-r)                         [for get hostname]
(-p)                         [for network settings]
(-s)                         [for know operator system]
(-t)                         [see time date]
(-V)                         [see version muzi]
(-i)                         [save information in info]
(-o)                         [open info.txt]
(-d)                         [delete history]
(-x)                         [exit]""")
    elif prompt.lower() == "muzi -h":
        print("""Muzi is a multifunctional tool with which a huge 
wave of system information can be achieved and is
an essential requirement for OSINT!!""")
    elif prompt.lower() == "muzi -r":
        subprocess.run("hostname") # hostname in system(Linux)
        
    elif prompt.lower() == "muzi -p":
        subprocess.run("ifconfig") # network setting
        
    elif prompt.lower() == "muzi -s":
        print(platform.system()) # operator system
        
    elif prompt.lower() == "muzi -t":
        subprocess.run("date") # time date
        
    elif prompt.lower() == "muzi -v":
        print("muzi version(1.0)") # muzi version
        
    elif prompt.lower() == "muzi -i": # save information in info.txt
        info = open("/home/alex/Coding/Tools/Muzi/V 1.0/info.txt", "a")
        info.write("\nHello World")
        info.close()
        
    elif prompt.lower() == "muzi -o": # open/read info.txt
        info = open("/home/alex/Coding/Tools/Muzi/info.txt", "r")
        print(info.read())
        info.close()
        
    elif prompt.lower() == "muzi -d":
        subprocess.run("clear") # delete from history
        
    elif prompt.lower() == "muzi -x":
        n = 1 # exit
        
    else:
        print("""Could not find command-not-found database. Run 'sudo apt update' to populate it.
ewq: command not found""")








