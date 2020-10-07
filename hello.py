""""
    Demonstrates variables, loops, conditionals, scope, comments, print statements, and input statements.

    This accomplishes our tasks, which also includes input validation by...
    stuff
    things
    ???
    profit!
"""


#this is a comment

"""
    this is a potentially
    multi-line comment
"""
invalid_input = True

while invalid_input:
    try:
        in_value = int(input("please input an integer between 1 and 9 (inclusive): "))
        if in_value not in range(1,10):
            raise ValueError
    except ValueError:
        print(f"That is not a valid integer, please try again!")
        continue
    except:
        print(f"something else went wrong, please contact your system administrator!")
        continue
    invalid_input = False

#in_value must be in the range of 1-9 (inclusive)

print(f"in_value: {in_value}")
print(f"isinstance(in_value, int): {isinstance(in_value, int)}")
