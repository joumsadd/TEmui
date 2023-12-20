#Introducing a new TEmui System Tuner for LOCAL PCs
import time
import subprocess as sbp
import sys, os
from colorama import Fore, Back, Style
from tkinter import messagebox as msg


def sideload():
    command = input('>>> ')
    if command.lower() == '0':
        debux()
    elif command.lower().startswith('cd '):
        # If the command is cd, change the current directory for sideload
        try:
            path = command[3:].strip()  # Get the path after "cd " and remove possible spaces
            os.chdir(path)
            print(f"Current directory for sideload: {os.getcwd()}")
        except FileNotFoundError:
            print(f"Directory '{path}' not found.")
        except Exception as e:
            print(f"Error changing directory: {e}")
        sideload()
    else:
        sbp.run(command, shell=True)
        print()
        sideload()

def debux():
    deb_command = input('--> ')
    if 'help' in deb_command.lower():
        print('Debug Xposed command list :')
        print('1. SIDELOAD - Starting cmd push commands(echo, exit,cls)')
        print('2. Abort status - Clearing debugging info txt')
        print('3. Debux Info - Showing DebuX version.')
        debux()
    elif 'abort status /info/' in deb_command.lower():
        file_name = 'LocalDeb_Temp-USER.txt'
        with open(file_name, 'w') as file:
            write = file.write('')
        with open(file_name, 'r') as file:
            content = file.read()   
        print(Fore.GREEN+'Debugging info has been successfully cleared!')
        print(Style.RESET_ALL)
        debux()
    elif 'sideload' in deb_command.lower():
        print('Cmd Emulator Mode : ONN')
        print('Type 0 for exit')
        time.sleep(0.4)
        sideload()
    elif 'debux' in deb_command.lower():
        print('DebuX v1.0.19045.3693 by Joumsadd')
                
    elif 'exit' in deb_command.lower():
        yesno = msg.askyesno(title='Exiting DebuX', message='Do you want to close DebuX? ')
        if yesno == True:
            start()
        else:
            debux()
    elif deb_command.lower().startswith('cd '):
        # If the command is cd, change the current directory
        try:
            path = deb_command[3:].strip()  # Get the path after "cd " and remove possible spaces
            os.chdir(path)
            print(f"Current directory: {os.getcwd()}")
        except FileNotFoundError:
            print(f"Directory '{path}' not found.")
        except Exception as e:
            print(f"Error changing directory: {e}")
        debux()
    else:
        print(Fore.RED+'An unexpected command!')
        print(Style.RESET_ALL)
        debux()

def su():
    path = input('Enter file directory: ')
    if path.lower() == 'exit':
        start()
    else:
        pass
    def su_system(path):
        """
        Функция для рекурсивного вывода структуры папок и файлов в указанном пути с нумерацией файлов.
        """
        indent=''
        # Выводим текущую папку
        print(f"{indent}[{os.path.basename(path)}/]")

        # Итерируем по всем элементам в текущей папке
        for idx, item in enumerate(os.listdir(path), start=1):
            item_path = os.path.join(path, item)

            # Проверяем, является ли элемент папкой
            if os.path.isdir(item_path):
                # Если это папка, вызываем функцию рекурсивно
                su_system(item_path)
            else:
                # Если это файл, выводим его с номером
                print(f"{indent}  {idx}-{item}")

    su_system(path)
    print()
    su()
    
def start():
    command = input('Enter based command: ')
    debug_file(command)
    if command.lower() == 'help':
        print('Showing command list:')
        print('1. SU - System Unity Mode, u can use this for checking file paths and contents')
        print('2. Info - Showing device info')
        print('3. Debux - Debug Xposed, termux emulator')
        print('4. Exit - Do i explain what this command does? ;)')
        start()
    elif command.lower() == 'su':
        print('System Utility Mode onn')
        print('Connecting')
        time.sleep(0.4)
        yesno = msg.askyesno(title='Connection', message='Do you want to connect to System Utility Mode\'s server? ')
        if yesno == True:
            print(Fore.GREEN+'Done')
            time.sleep(0.4)
            su()
            debug_file(command)
        else:
            print(Fore.RED+'Connecting ERROR, aborting..')
            print(Style.RESET_ALL)
            sys.exit(SystemError)
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
        print(Style.RESET_ALL)

def debug_file(command):
    file_name = 'LocalDeb_Temp-USER.txt'
    now = time.strftime('%H:%M:%S', time.localtime())
    os_version = os.sys.getwindowsversion()

    with open(file_name, 'r') as file:
        content = file.read()

    if 'starting' in content.lower():
        with open(file_name, 'a') as file:
            file.write(f'{now} Starting {command.upper()}-command for {time.time()}, OS Version: {os_version.major}.{os_version.minor}\n')
    else:
        with open(file_name, 'w') as file:
            file.write(f'{now} Starting {command.upper()}-command for {time.time()}, OS Version: {os_version.major}.{os_version.minor}')

def system_info():
    """
    Функция для вывода информации о системе: имя пользователя, название компьютера и версию операционной системы.
    """
    username = os.getlogin()  # Имя пользователя
    computer_name = os.environ['COMPUTERNAME']  # Название компьютера
    os_version = os.sys.getwindowsversion()  # Версия операционной системы

    print(f"User name: {username}")
    print(f"PCs name: {computer_name}")
    print(f"OS version: {os_version.major}.{os_version.minor}")
    start()

start()
