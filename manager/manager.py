import json
from datetime import datetime
from getpass import getpass
from utils import is_valid_password, is_valid_name, make_password, print_status
from models import User


class Manager:
    def __init__(self):
        self.user = None
        self.users = self.load_users()

    def register(self):
        name = input("name: ").strip()
        username = input("username: ")
        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")

        if not is_valid_name(name):
            print("Ism xato!\n")
        elif self.check_username(username):
            print(f"{username} band.\n")
        elif password != confirm_password:
            print("Parollar mos emas.\n")
        elif not is_valid_password(password):
            print("Parol kamida 8 ta belgidan iborat bo‘lishi kerak.")
        else:
            self.users.append(User(name, username, make_password(password)))
            self.save_users()
            print("Muvaffaqiyatli ro'yxatdan o'tdingiz.")

    def login(self):
        username = input("username: ")
        password = getpass("password: ")
        hashed_password = make_password(password)

        for user in self.users:
            if user.username == username and user.password == hashed_password:
                print_status("Tizimga muvaffaqiyatli kirdingiz.")
                self.user = user
                return True
        print_status("Foydalanuvchi topilmadi.", "error")
        return False

    def check_username(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def save_users(self):
        with open('data/users.json', 'w') as f:
            json.dump([user.to_dict() for user in self.users], f, indent=4)

    @staticmethod
    def load_users():
        try:
            with open('data/users.json') as f:
                data = json.load(f)
                return [User.from_dict(item) for item in data]
        except:
            return []

    def add_task(self):
        title = input("Title: ")
        description = input("Description: ")
        created_at = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        deadline = input("Deadline: ")

        task = {
            "user_id": self.user.user_id,
            "title": title,
            "description": description,
            "created_at": created_at,
            "deadline": deadline,
            "completed": False
        }

        try:
            with open('data/tasks.json') as f:
                tasks = json.load(f)
        except:
            tasks = []

        tasks.append(task)

        with open('data/tasks.json', 'w') as f:
            json.dump(tasks, f, indent=4)
        print_status("Task qo'shildi.")
