import requests
import os
import colorama
from colorama import Fore
from tkinter import Tk, filedialog
from colorama import Fore, Style


colorama.init(autoreset=True)

def check_proxy(proxy):
    url = "http://httpbin.org/ip"  
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}

    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

def main():
    print('''\033[92m
=========================================================================
|                                                                       |
| ███╗   ███╗██████╗        ██████╗  ██████╗ ██████╗  ██████╗ ████████╗ |
| ████╗ ████║██╔══██╗       ██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝ |
| ██╔████╔██║██████╔╝       ██████╔╝██║   ██║██████╔╝██║   ██║   ██║    |
| ██║╚██╔╝██║██╔══██╗       ██╔══██╗██║   ██║██╔══██╗██║   ██║   ██║    |
| ██║ ╚═╝ ██║██║  ██║██╗    ██║  ██║╚██████╔╝██████╔╝╚██████╔╝   ██║    |
| ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    |
|      Try to be a puzzle in the system, not a puzzle piece.            |
|        Github Page : https://github.com/burakdevelopment              |
|                                                                       |
|                    -    kali@buraktheroot    -                        |
=========================================================================
''')
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Proxy listesini seçin", filetypes=[("Text files", "*.txt")])

    if not file_path:
        print("Dosya seçilmedi, çıkılıyor...")
        return
 
    with open(file_path, "r") as file:
        proxies = file.readlines()

    print("Proxy Kontrolü Başlatıldı!")

    for proxy in proxies:
        proxy = proxy.strip()
        if proxy:
            status = check_proxy(proxy)
            if status:
                print(f"{proxy} - {Fore.GREEN}AKTİF")
            else:
                print(f"{proxy} - {Fore.RED}PASİF")

if __name__ == "__main__":
    main()
