import datetime
import calendar

contacts = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "Контакт не знайдено"
        except ValueError:
            return "Невірний формат вводу"
        except IndexError:
            return "Невірний формат вводу"
    return inner

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"{name} було додано до контактів з номером {phone}"

@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return f"Номер телефону для {name} було змінено на {phone}"

@input_error
def phone_contact(name):
    return f"Номер телефону для {name}: {contacts[name]}"

def show_all():
    for name, phone in contacts.items():
        print(name, phone)

def main():
    while True:
        command = input("Введіть команду: ").lower()
        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "show all":
            show_all()
        elif command.startswith("add"):
            name, phone = command.split()[1:]
            print(add_contact(name, phone))
        elif command.startswith("change"):
            name, phone = command.split()[1:]
            print(change_contact(name, phone))
        elif command.startswith("phone"):
            name = command.split()[1]
            print(phone_contact(name))
        elif command == "hello":
            print("How can I help you?")
        elif command == "today":
            today = datetime.date.today()
            print(f"Сьогоднішня дата: {today}")
        elif command == "calendar":
            year = int(input("Введіть рік: "))
            month = int(input("Введіть місяць: "))
            print(calendar.month(year, month))
        else:
            print("Невідома команда")

if __name__ == "__main__":
    main()