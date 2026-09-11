
from utils import add_numbers, multiply_numbers


def main():
    print("Python Lab")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print(f"Sum: {add_numbers(a, b)}")
    print(f"Product: {multiply_numbers(a, b)}")


if __name__ == "__main__":
    main()
