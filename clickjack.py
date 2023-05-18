import colorama
from colorama import Fore, Style,Back
from urllib.request import urlopen

colorama.init(autoreset=True)

def Clickjacking():
    url = input(Back.BLACK + Fore.CYAN + "Enter host >> ")
    data = urlopen(url)
    header = data.info()

    if not "X-Frame-Option" in header:
        print(Fore.GREEN + "Website is vulnerable to clickjacking ")
    else:
        print(Fore.RED + "Website is not vulnerable to clickjacking")


if __name__ == "__main__":
    clickjacking()

