import os, sys, time, webbrowser, subprocess as sbp
from colorama import init, Fore, Style
from tkinter import messagebox as msg
from pySmartDL import SmartDL
from urllib.error import HTTPError
from prompt_toolkit import prompt
from frameworks.toolsard import gradual_art
from frameworks.sumode import su

def dfc():
    file_name = "LocalDeb_Temp-USER.txt"
    if os.path.isfile(file_name):
        pass
    else:
        debugfileControl = input('Do you want to activate debug file?(Y/N) --> ')
        if debugfileControl.lower() == 'y':
            return True
        elif debugfileControl.lower() == 'n':
            return False
        else:
            print(Fore.RED+f'Unexpected choose {debugfileControl} !')

Control = dfc()
os.system('cls')

class initConvertingSuite:
    init(strip=True)
    init(autoreset=True, convert=True)

def temui():
    license = 'Basic User Licence, MIT'
    print(f'TEmui Version : 1.2.2125.120124.0')
    print(f'License: {license}')
    start()

def check_debug(content, file_name, now, command, os_version) -> bool:
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

def manager() -> bool:
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
        print('4.dll set \'command\' - New features for DebuX' )
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

        elif 'help' in dllCoGroup.lower():
            print('1. dll set shell:startup or autostart - Opens Autostart folder in Windows')
            print('2. ping \'site\' - opens and shows ping of the writed site')
            print('3. wlan props \'WIFI-NAME or SSID\' - shows wifi properties(password, ip, name etc.)')
            print('4. ii \'ANSCII LOGO CODENAME\' - generate and shell ASCII logos')
            debux()
        
        elif 'wlan props'in dllCoGroup.lower():
            wlanName = command[19:].strip()
            print(wlanName)
            wlanProps = f'netsh wlan show profiles name={wlanName} key=clear'
            sbp.run(wlanProps, shell=True)
            debux()
            

        elif 'ping' in dllCoGroup.lower():
            pingSite = command[13:].strip()
            ping = f'ping {pingSite}'
            sbp.run(ping, shell=True)
            url = "pingSite"
            webbrowser.open(url)
            debux()

        elif 'ii' in dllCoGroup.lower():
            ImageProps = command[10:].strip()
            if 'parrot' in ImageProps.lower():
                asciiCommand = 'curl parrot.live'
                os.system(asciiCommand)
                debux()
            elif 'rick' in ImageProps.lower():
                asciiCommand = 'curl ascii.live/rick'
                os.system(asciiCommand)
                debux()
            elif 'forrest' in ImageProps.lower():
                asciiCommand = 'curl ascii.live/forrest'
                os.system(asciiCommand)
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
        start()

    else:
        print(Fore.RED+'An unexpected command!')
        debux()

def start():
    command = input('Enter based command ~')
    debug_file(command, Control)
    if 'help' in command.lower():
        print('Showing command list:')
        print('1. SU - System Unity Mode, u can use this for checking file paths and contents')
        print('2. Info - Showing device info')
        print('3. Debux - Terminal Emulator with some modules')
        print('4. Cln - Cleans teminal inputs and outputs, like cls in bash')
        print('5. Temui Info - Shows last release version of TEmui')
        print('6. Exit - Do I explain what this command does? ;)')
        start()

    elif 'cln' in command.lower():
        sbp.run('cls', shell=True)
        print()
        start()

    elif 'su' in command.lower():
        print('System Utility Mode on')
        print('Connecting')
        time.sleep(0.4)
        yesno = msg.askyesno(title='Connection', message='Do you want to connect to System Utility Mode\'s server? ')
        if yesno:
            print(Fore.GREEN+'Done')
            if su() == True:
                start()
            else:
                pass
            debug_file(command)
        else:
            print(Fore.RED+'Connecting ERROR, aborting..')
            start()
    elif 'temui info' in command.lower():
        temui()
        print()
        start()
    elif 'debux' in command.lower():
        print('Loading Debug Xposed...')
        time.sleep(0.4)
        debux()
    elif 'info' in command.lower():
        system_info()
    elif 'exit'  in command.lower():
        yesno = msg.askyesno(title='Exit TEmui', message='Do you want to exit TEmui ?')
        if yesno:
            os.exit()
        else:
            start()
    else:
        print(Fore.RED+'Unknown Command!')
        start()

def debug_file(command, power):
    if power == True:
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
    else:
        pass
def system_info():
    username = os.getlogin()
    computer_name = os.environ['COMPUTERNAME']
    os_version = os.sys.getwindowsversion()

    print(f"User name: {username}")
    print(f"PC name: {computer_name}")
    print(f"OS version: {os_version.major}.{os_version.minor}")
    start()

gradual_art('Temui', 'ogre')
start()