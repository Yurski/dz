from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    def validate(self, value):
        pass

    def __str__(self):
        return str(self._value)

class Name(Field):
    pass

class Phone(Field):
    def validate(self, value):
        # Валідація формату номера телефону (10 цифр)
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")

class Birthday(Field):
    def validate(self, value):
        # Валідація формату дня народження (YYYY-MM-DD)
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid birthday format")

class Record:
    def __init__(self, name, phones, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones]
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
            return (next_birthday - today).days
        return None

    def __str__(self):
        phones_str = '; '.join(str(p) for p in self.phones)
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, batch_size=1):
        records = list(self.data.values())
        for i in range(0, len(records), batch_size):
            yield records[i:i + batch_size]




# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John", ["1234567890", "5555555555"], "1990-05-15")
book.add_record(john_record)

# Виведення днів до наступного дня народження для John
print(f"Days to John's birthday: {john_record.days_to_birthday()}")