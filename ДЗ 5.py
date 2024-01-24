from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        # Валідація формату номера телефону (10 цифр)
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    # # Старий варіанд коду
    # def edit_phone(self, old_phone, new_phone):
    #     self.remove_phone(old_phone)
    #     self.add_phone(new_phone)

    # Внесена зміна в код.
        def edit_phone(self, old_phone, new_phone):
            if self.find_phone(old_phone):
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
            else:
                raise ValueError(f"Phone {old_phone} not found in the record")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    # def add_record(self, record):
    #     self.data[record.name.value] = record

    # Внесена друга зміна. Досвідчені програмувальники порадили. Додав як підвищення знання.
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError(f"Record with name {record.name.value} already exists")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
