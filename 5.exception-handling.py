try:
    num = int(input("Enter a number: "))
    divider_num = int(input("Enter a second number: "))
    result = num / divider_num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print("Result:", result)
finally:
    print("Execution complete.")


class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__("Negative numbers not allowed: " + str(value))


def process_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    return num**2


try:
    num = float(input("Enter a positive number: "))
    result = process_number(num)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print("Result:", result)
finally:
    print("Execution complete.")
