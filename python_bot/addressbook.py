import re
import pickle
from datetime import date
from collections import UserDict
from python_bot import NoteBook, UserInterface
from .abstract_classes import BaseRecordStorage, _Field


class _Name(_Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value) -> None:
        name_value_pattern = r"^[A-Za-zА-Яа-яїЇєЄ]{2,25}$"
        if re.match(name_value_pattern, value):
            self._value = value
        else:
            raise ValueError(
                "Name is not valid. It should contain only letters and be no longer than 25 characters."
            )


class _Phone(_Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        if not re.compile(r"^\+(?:\d[\s-]?){9,14}\d$|\d{9,10}$").match(value):
            raise ValueError("Phone number is not valid!")
        self._value = value

    def __eq__(self, _obj) -> bool:
        return self.value == _obj.value


class _Email(_Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        if not re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$").match(
            value
        ):
            raise ValueError("Provided email is not valid")
        self._value = value

    def __str__(self) -> str:
        return self._value


class _Birthday(_Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self) -> date:
        return self._value

    @value.setter
    def value(self, value) -> None:
        email_value_pattern = r"[-|_|\\|/]"
        day, month, year = map(int, re.split(email_value_pattern, value))
        birthday = date(year, month, day)
        if birthday >= date.today():
            raise ValueError(f"Birthday must be in the past")
        self._value = birthday

    def __str__(self) -> str:
        return self._value.strftime("%d-%m-%Y")


class _Record:
    def __init__(self, name: str):
        self.name = _Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

    def add_phone(self, phone: str):
        phone = _Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            raise ValueError(
                f"Phone {phone.value} already exists in {self.name.value} record"
            )

    def change_phone(self, old_phone: str, new_phone: str):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise KeyError(f"Phone {old_phone} is not found in record")

    def del_phone(self, phone: str):
        phone = _Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise KeyError(
                f"Phone {phone.value} does not exist in {self.name.value} record"
            )

    def set_birthday(self, birthday: str):
        birthday = _Birthday(birthday)
        self.birthday = birthday

    def del_birthday(self):
        self.birthday = None

    def set_email(self, email: str):
        email = _Email(email)
        self.email = email

    def del_email(self):
        self.email = None

    def days_to_birthday(self) -> int | None:
        if not self.birthday:
            return None
        today = date.today()
        try:
            birthday_this_year = self.birthday.value.replace(year=today.year)
        except ValueError:
            birthday_this_year = self.birthday.value.replace(
                year=today.year, day=today.day - 1
            )
        if birthday_this_year < today:
            birthday_this_year = self.birthday.value.replace(year=today.year + 1)
        days_to_birthday = (birthday_this_year - today).days
        return days_to_birthday

    def __str__(self):
        str_phones = " ".join(phone.value for phone in self.phones)
        str_email = self.email.value if self.email else str()
        str_birthday = str(self.birthday) if self.birthday else str()
        return "|".join((self.name.value, str_email, str_phones, str_birthday))


class FileHandler:
    @staticmethod
    def save_to_file(filename, address_book):
        with open(filename, "wb") as f:
            pickle.dump(address_book, f)

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("File not found.")
            return None


class AddressBook(BaseRecordStorage, UserDict):

    notebook = UserInterface(NoteBook())

    def add_record(self, name: str):
        if name not in self.data:
            self.data[name] = _Record(name)
        else:
            raise KeyError("Record with this name already exists.")

    def del_record(self, name: str):
        if name in self.data:
            self.data.pop(name)
        else:
            raise KeyError(f"Record with name {name} does not exist")

    def show_records(self):
        results = ""
        for record in self.data.values():
            str_phones = (
                ", ".join(phone.value for phone in record.phones)
                if record.phones
                else "No records"
            )
            str_birthday = record.birthday if record.birthday else "No records"
            str_email = record.email if record.email else "No records"
            formatted_record = f"\n Name: {record.name.value}\n Phones: {str_phones}\n Birthday: {str_birthday}\n Email: {str_email}\n"
            results += formatted_record
        print(results)

    def search(self, query):
        results = ""
        for record in self.data.values():
            if query in str(record):
                str_phones = (
                    ", ".join(phone.value for phone in record.phones)
                    if record.phones
                    else "No records"
                )
                str_birthday = record.birthday if record.birthday else "No records"
                str_email = record.email if record.email else "No records"
                formatted_record = f"\n Name: {record.name.value}\n Phones: {str_phones}\n Birthday: {str_birthday}\n Email: {str_email}\n"
                results += formatted_record
        founded_notes = self.notebook.search(query)
        formatted_notes = [str(note) for note in founded_notes]
        results += "".join(formatted_notes)
        return results

    def contacts_with_days_to_bday(self, days):
        days = int(days)
        results = ""
        for record in self.data.values():
            if record.days_to_birthday() is None:
                continue
            elif record.days_to_birthday() <= days:
                str_phones = (
                    ", ".join(phone.value for phone in record.phones)
                    if record.phones
                    else "No records"
                )
                str_birthday = record.birthday if record.birthday else "No records"
                str_email = record.email if record.email else "No records"
                formatted_record = f"\n Name: {record.name.value}\n Phones: {str_phones}\n Birthday: {str_birthday}\n Email: {str_email}\n"
                results += formatted_record
        return results

    def save_records(self, filename):
        data = {"address_book": self.data, "notebook": self.notebook}
        FileHandler.save_to_file(filename, data)

    def load_records(self, filename):
        loaded_data = FileHandler.load_from_file(filename)
        if loaded_data is not None:
            self.data = loaded_data["address_book"]
            self.notebook = loaded_data["notebook"]

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
        raise KeyError(f"No contact with name {key}")


if __name__ == "__main__":
    print("let's add some contacts to the address book")
