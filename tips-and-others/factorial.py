def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


try:
    number = int(input("Enter the number: "))
    print(f"Factorial : {factorial(number)}")

except ValueError as e:
    print(f"Error : {e}")
