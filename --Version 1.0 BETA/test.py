import os

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

# Пример использования
system_info()
