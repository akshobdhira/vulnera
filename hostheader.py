import requests
from colorama import Fore, Style, Back

cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT


def HostHeader():
    url = input(Back.BLACK + Fore.CYAN + "Enter host >> ")
    url = (url)
    headers = {'Host': 'http://evil.com'}
    response = requests.get(url, headers=headers)

    if 'evil.com' in response.headers:
        print(green + "Vulnerable to Host Header Injection")
    else:
        print(Back.BLACK + Fore.RED + Style.NORMAL +
              "NOT VULNERABLE TO HOST HEADER INJECTION")


if __name__ == "__main__":
    HostHeader()