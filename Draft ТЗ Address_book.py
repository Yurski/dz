class Address_book:
    def __init__(self):
        self.contacts = []  # Список контактів (Contact list)
        self.notes = []  # Список нотаток (Note)

    def add_contact(self, name, address, phone_number, email, birthday):
        """Додати новий контакт до книги контактів."""
        contact = {
            'name': name,
            'address': address,
            'phone_number': phone_number,
            'email': email,
            'birthday': birthday
        }
        self.contacts.append(contact)

    def list_contacts(self):
        """Вивести список контактів."""
        for contact in self.contacts:
            print(f"Ім'я: {contact['name']}, Телефон: {contact['phone_number']}")

    def search_contacts_by_birthday(self, days_until_birthday):
        """Знайти контакти, у яких день народження через задану кількість днів."""
        # Логіка пошуку за днем народження (Search logic by birthday)

    def validate_phone_number(self, phone_number):
        """Перевірити правильність введеного номера телефону."""
        # Логіка перевірки номера телефону (Search logic by phone numbre)

    def validate_email(self, email):
        """Перевірити правильність введеної адреси електронної пошти."""
        # Логіка перевірки email (Logic of email verification)

    def add_note(self, text, tags):
        """Додати нову нотатку."""
        note = {
            'text': text,
            'tags': tags
        }
        self.notes.append(note)

    def search_notes_by_tags(self, search_tags):
        """Знайти нотатки за ключовими словами (тегами)."""
        # Логіка пошуку нотаток за тегами (Logic for searching for notes by tags)

    def sort_files_by_category(self, folder_path):
        """Сортувати файли у зазначеній папці за категоріями."""
        # Логіка сортування файлів за категоріями (Logic for sorting files by category)

