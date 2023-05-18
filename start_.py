from colorama import Fore,Back,Style,init
from clickjack import Clickjacking
from hostheader import HostHeader
from subdomainenum import  subdomain
init(autoreset=True)

cyan=Fore.CYAN + Style.BRIGHT
green=Fore.GREEN + Style.BRIGHT
red=Fore.RED + Back.BLACK + Style.BRIGHT
yellow=Fore.YELLOW + Style.BRIGHT


banner= cyan + '''
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗██████╗  █████╗ 
██║   ██║██║   ██║██║     ████╗  ██║██╔════╝██╔══██╗██╔══██╗
██║   ██║██║   ██║██║     ██╔██╗ ██║█████╗  ██████╔╝███████║
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
--------------Web app Vulnerability Scanner ----------------                                                         
'''
def main():
    print(banner)
    print(green + "")
    print(green + "Availabe Modules !")
    print(green + "")
    print(green + "1 - Clickjacking")
    print(green + "2 - Host Header Injection")
    print(green + "3 - Subdomain Enumeration")
    print(yellow + "Enter the option number ")
    while True:
        inp=input(green + "Enter your input option : ")
        if inp == '1':
            Clickjacking()
        elif inp == '2':
            HostHeader()
        elif inp == '3':
            subdomain()
        else:
            print(red + "Invalid input !! ")


if __name__ == "__main__":
    main()
























