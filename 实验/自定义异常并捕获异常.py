# encoding:utf-8
class InvalidInputError(Exception):
    def __init__(self, expression, message):
        self.expression = expression

        self.message = message
try:

    age = input("Please enter your age: ")
    if not age.isdigit():
        raise InvalidInputError(age, "Age must be a number.")
    else:
        print("Thank you for entering your age!")
except InvalidInputError as e:
    print(f"Invalid Input Error: {e.message}")
finally:
    print(age)