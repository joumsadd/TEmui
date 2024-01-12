import os, sys
from colorama import init,Fore
class init:
    init(strip=True)
    init(autoreset=True, convert=True)

def su_system(path):
    try:
        print(f"[{os.path.basename(path)}/]")
        for idx, item in enumerate(os.listdir(path), start=1):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                su_system(item_path)
            else:
                print(f"  {idx}-{item}")

    except Exception as e:
        print(Fore.RED + 'System Utility mode OFF..')

def su():
    try:
        path = input('Enter file directory: ')
        if path.lower() == 'exit':
            return True
        else:
            pass
        su_system(path)
        print()
        su()
    except Exception as e:
        print(Fore.RED + 'System Utility mode OFF..')
