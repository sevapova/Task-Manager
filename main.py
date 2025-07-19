import sys
from utils import print_main, print_status, print_menu
from manager.manager import Manager

def main():
    manager = Manager()

    while True:
        print_main()
        op = input("> ")

        if op == '1':
            if manager.login():
                while manager.user:
                    print_status(f"{manager.user.name} siz tizimdasiz.")
                    print_menu()
                    choice = input("> ")

                    if choice == '1':
                        manager.add_task()
                    elif choice == '2':
                        print("Tasklarni ko'rish funksiyasi hali yozilmagan.")
                    elif choice == '3':
                        print("Taskni bajarildi qilish funksiyasi hali yozilmagan.")
                    elif choice == '4':
                        print("Bajarilmagan tasklar funksiyasi hali yozilmagan.")
                    elif choice == '5':
                        manager.user = None
                    else:
                        print_status("Noto'g'ri tanlov.", "error")
        elif op == '2':
            manager.register()
        elif op == '3':
            sys.exit(0)
        else:
            print_status("Noto'g'ri tanlov.", "error")

if __name__ == "__main__":
    main()
