"""Demonstrates the basics of classes in Python."""

"""
    ToDo:
        write more tests
        include file IO
        fix git repositories
"""
import traceback


class Person:
    """Defines a Person."""

    def __init__(self):
        """Initialize a Person object."""
        self.name: str = "Joseph"
        self.age: int = 34
        self.is_alive: int = True

    def double_age(self) -> int:
        """Return double the value of this person's age.."""
        return self.age * 2

    def birthday(self) -> None:
        """Increase this peron's age by 1."""
        self.age += 1

    def birthdays(self, num_birthdays: int) -> int:
        """Increase this peron's age by num_birthdays."""
        self.age += num_birthdays

        return self.age

    def print_yo_self(self) -> None:
        """Print this person in a human readable format."""
        print(f"name: {self.name}, age: {self.age}, is_alive: {self.is_alive}")

    def write(self) -> None:
        try:
            with open(self.name, "w") as output_file:
                output_file.write(self.name + "\n")
                output_file.write(str(self.age) + "\n")
                output_file.write(str(self.is_alive) + "\n")
        except FileNotFoundError as err:
            print("File not found, try again later")
            print(traceback.print_tb(err.__traceback__))
            exit()


def read(filename: str) -> Person:
    
    try:
        with open(filename, "r") as input_file:
            lines = input_file.readlines()
    except FileNotFoundError as err:
        print("File not found, try again later")
        print(traceback.print_tb(err.__traceback__))
        exit()

    new_person = Person()
    new_person.name = lines[0][0:-1]
    new_person.age = lines[1][0:-1]
    new_person.is_alive = lines[2][0:-1]

    return new_person


joseph = Person()
# print(f"joseph.name: {joseph.name}")
# print(f"joseph.age: {joseph.age}")
# print(f"joseph.is_alive: {joseph.is_alive}")
joseph.print_yo_self()
print(joseph.double_age())

num_birthdays_output = joseph.birthdays(10)
print(f"num_birthdays_output: {num_birthdays_output}")
joseph.print_yo_self()

joseph.write()

new_person = read("Joseph")
new_person.print_yo_self()
