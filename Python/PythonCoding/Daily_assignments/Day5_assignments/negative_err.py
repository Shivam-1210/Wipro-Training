
class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed. Please enter a positive number."):
        self.message = message
        super().__init__(self.message)



try:
    num = float(input("Enter a positive number: "))

    if num < 0:
        raise NegativeNumberError

    print(f"You entered a valid positive number: {num}")

except NegativeNumberError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")