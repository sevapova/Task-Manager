from hashlib import sha256
from termcolor import colored

def print_main() -> None:
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Quit")

def print_menu() -> None:
    print("1. Task Yaratish")
    print("2. Tasklarni Ko'rish")
    print("3. Taskni bajarildi qilish")
    print("4. Bajarilmagan tasklarni ko'rish")
    print("5. Quit")

def is_valid_password(password):
    return len(password) >= 8

def is_valid_name(name):
    return name.replace("'", "").replace(" ", "").isalpha()

def make_password(password):
    return sha256(password.encode()).hexdigest()

def print_status(text, status='success'):
    colors = {
        'success': 'green',
        'error': 'red'
    }
    print(colored(text, colors[status]))
