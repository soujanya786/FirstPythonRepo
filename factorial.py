"""This function is to define factorial of a user input number"""


def main():
    fact_num = int(input("Enter the number for which you want the factorial:"))
    result = factorial(fact_num)
    print("The factorial of", fact_num, "is", result)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


if __name__ == '__main__':
    main()
