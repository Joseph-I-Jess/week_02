import pytest
import classes

def test_init_name():
    a_person = classes.Person()

    assert a_person.name == "Joseph"

def test_init_age():
    a_person = classes.Person()

    assert a_person.age == 34

def test_init_is_alive():
    a_person = classes.Person()

    assert a_person.is_alive == True

def test_double_age():
    a_person = classes.Person()

    assert a_person.double_age() == 68

def test_birthday():
    a_person = classes.Person()
    a_person.birthday()

    assert a_person.age == 35

#should define a test for birthdays
def test_birthdays():
    assert False

def test_double_age_after_birthday():
    a_person = classes.Person()
    a_person.birthday()

    assert a_person.double_age() == 70

def test_print_yo_self(capsys):
    a_person = classes.Person()
    a_person.name = "new_name"

    a_person.print_yo_self()

    actual_output = capsys.readouterr()[0]
    expected_output = "name: new_name, age: 34, is_alive: True\n"

    assert actual_output == expected_output
