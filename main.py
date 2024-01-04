import time
import os
import sys
from colorama import init, Fore, Style
from tkinter import messagebox as msg
from pySmartDL import SmartDL
from urllib.error import HTTPError
import subprocess as sbp
from prompt_toolkit import prompt
import webbrowser
import toolsard as ard

class initConvertingSuite:
    init(strip=True)
    init(autoreset=True, convert=True)

def temui():
    license = 'Basic User Licence'
    print(f'TEmui Version : 1.0.1726.241223.0')
    print(f'License: {license}')
    start()

def check_debug(content, file_name, now, command, os_version):
    mode = 'a' if 'starting' in content.lower() else 'w'
    with open(file_name, mode) as file:
        file.write(f'{now} Starting {command.upper()}-command for {time.time()}, OS Version: {os_version.major}.{os_version.minor}\n')

def create_download_folder(download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

class DownloadManager:
    def __init__(self, download_folder):
        self.download_folder = download_folder
        create_download_folder(self.download_folder)

    def download_file(self, url, filename):
        try:
            full_path = os.path.join(self.download_folder, filename)
            obj = SmartDL(url, full_path)
            obj.start()
        except HTTPError as e:
            print(Fore.RED(f"HTTP Error: {e}"))
            debux()
        except Exception as e:
            print(Fore.RED(f"An error occurred: {e}"))
            debux()

def manager():
    url = input('Enter url: ')
    if url == '0':
        debux()

    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    download_manager = DownloadManager(os.path.join(script_directory, 'Download'))
    filename = input('Enter filename: ')
    download_manager.download_file(url, filename)
    debux()

def debux():
    command = input('$ ')

    if 'help' in command.lower():
        print('1.abort status /info/ - Clearing debugging info txt')
        print('2.debux Info - Showing DebuX version.')
        print('3.debmode \'mode\' - Changes DebuX working mode(CMD emulator or smthg)')
        debux()

    elif command.lower().startswith('debmode '):
        debuxMode = command[8:].strip()
        if debuxMode.lower() == 'cmd':
            print(Fore.GREEN+f'DebMode was successfully changed to {debuxMode} value')
            def mode_check():
                module = prompt(f'{debuxMode}@{os.getlogin()} ', multiline=False)
                if module == 'debmode reset':
                    print(Fore.GREEN+'DebMode was successfully reset to normal values')
                    debux()
                elif module == 'cmd':
                    print('Microsoft Windows Terminal core [Version 11.0.2226.3693] modded by Joumsad')
                    print('(c) TEmui Framework module (Joumsadd Github). All rights reserved.')
                    print()
                    mode_check()
                else:
                    os.system(module)
                    mode_check()
            mode_check()

    elif command.lower().startswith('dll set '):
        dllCoGroup = command[8:].strip()
        if dllCoGroup.lower() == 'shell:startup' or dllCoGroup.lower() == 'autostart':
            startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            os.startfile(startup_folder)
            print(Fore.GREEN+f'Succsessfully completed to open AutoStart!')
            debux()
        elif 'ping' in dllCoGroup.lower():
            pingSite = command[13:].strip()
            ping = f'ping + {pingSite}'
            sbp.run(ping, shell=True)
            url = "pingSite"
            webbrowser.open(url)
            debux()
        else:
            print(Fore.RED+'An Unexpexted Command!')
            debux()

    elif 'cls' in command.lower():
        os.system('cls')
        print()
        debux()

    elif 'import' in command.lower():
        manager()
        debux()

    elif 'abort status /info/' in command.lower():
        try:
            file_name = 'LocalDeb_Temp-USER.txt'
            with open(file_name, 'w'):
                pass
            def checkFileContent(fileName):
                with open(fileName, 'r') as file:
                    content = file.read()
                if content == '':
                    return True
                else:
                    return False
            checkFileContent(file_name)
            if checkFileContent(file_name) == True:
                print(Fore.GREEN+'Debugging info has been successfully cleared!')
                debux()
        except Exception as e:
            print(Fore.RED+f'Error : {e}')
                

    elif 'debux' in command.lower():
        print('DebuX v1.0.19045.3693 by Joumsadd')
        print()
        debux()

    elif command.lower().startswith('cd '):
        try:
            path = command[3:].strip()
            os.chdir(path)
            print(f"Current directory: {os.getcwd()}")
        except FileNotFoundError:
            print(Fore.RED+f"Directory '{path}' not found.")
        except Exception as e:
            print(Fore.RED+f"Error changing directory: {e}")
        debux()

    elif 'exit' in command.lower():
        yesno = msg.askyesno(title='Exiting DebuX', message='Do you want to close DebuX? ')
        if yesno:
            start()
        else:
            debux()

    else:
        print(Fore.RED+'An unexpected command!')
        debux()

def su():
    path = input('Enter file directory: ')
    if path.lower() == 'exit':
        start()
    else:
        pass

    def su_system(path):
        print(f"[{os.path.basename(path)}/]")
        for idx, item in enumerate(os.listdir(path), start=1):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                su_system(item_path)
            else:
                print(f"  {idx}-{item}")

    su_system(path)
    print()
    su()

def start():
    command = input('Enter based command ~')
    debug_file(command)
    if command.lower() == 'help':
        print('Showing command list:')
        print('1. SU - System Unity Mode, u can use this for checking file paths and contents')
        print('2. Info - Showing device info')
        print('3. Debux - Terminal Emulator with some modules')
        print('4. Exit - Do I explain what this command does? ;)')
        start()
    elif command.lower() == 'pr':
        sbp.run('cls', shell=True)
        print()
        input('Enter based command: ')
    elif command.lower() == 'su':
        print('System Utility Mode on')
        print('Connecting')
        time.sleep(0.4)
        yesno = msg.askyesno(title='Connection', message='Do you want to connect to System Utility Mode\'s server? ')
        if yesno:
            print(Fore.GREEN+'Done')
            su()
            debug_file(command)
        else:
            print(Fore.RED+'Connecting ERROR, aborting..')
            start()
    elif 'temui info' in command.lower():
        temui()
        print()
        start()
    elif command.lower() == 'debux':
        print('Loading Debug Xposed...')
        time.sleep(0.4)
        debux()
    elif command.lower() == 'info':
        system_info()
    elif command.lower() == 'exit':
        sys.exit()
    else:
        print(Fore.RED+'Unknown Command!')
        start()

def debug_file(command):
    file_name = 'LocalDeb_Temp-USER.txt'
    now = time.strftime('%H:%M:%S', time.localtime())
    os_version = os.sys.getwindowsversion()
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            check_debug(content, file_name, now, command, os_version)

    except FileNotFoundError:
        with open(file_name, 'w'):
            pass

def system_info():
    username = os.getlogin()
    computer_name = os.environ['COMPUTERNAME']
    os_version = os.sys.getwindowsversion()

    print(f"User name: {username}")
    print(f"PC name: {computer_name}")
    print(f"OS version: {os_version.major}.{os_version.minor}")
    start()

ard.gradual_art('TEmui','ogre')
start()