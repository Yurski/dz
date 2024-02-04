import pickle  

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            # Якщо файл не знайдено, не робимо нічого
            pass

    def search_contacts(self, keyword):
        matching_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                matching_contacts.append(contact)
        return matching_contacts


def main():
    address_book = AddressBook()

    # Завантаження даних з файлу при старті програми
    address_book.load_from_file('address_book_data.pkl')

    while True:
        print("1. Додати контакт")
        print("2. Пошук контактів")
        print("3. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            new_contact = Contact(name, phone)
            address_book.add_contact(new_contact)
            print("Контакт додано!")

        elif choice == '2':
            keyword = input("Введіть ключове слово для пошуку: ")
            matching_contacts = address_book.search_contacts(keyword)
            if matching_contacts:
                for contact in matching_contacts:
                    print(f"Ім'я: {contact.name}, Телефон: {contact.phone}")
            else:
                print("Контакти не знайдено.")

        elif choice == '3':
            # Зберігання даних у файл перед виходом
            address_book.save_to_file('address_book_data.pkl')
            print("Дані збережено. Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте знову.")


if __name__ == "__main__":
    main()