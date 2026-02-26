
def check_password():
    while input("Enter password: ") != "1234":
        print("Wrong password")
    print("Access granted")

def factorial():
    n = int(input("Enter number: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)

def guessing_game():
    while int(input("Guess the number: ")) != 7:
        print("Try again")
    print("Correct!")

def check_prime():
    n = int(input("Enter number: "))
    prime = True

    if n <= 1:
        prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False

    if prime:
        print("Prime number")
    else:
        print("Not prime")


# Calling the functions
check_password()
factorial()
guessing_game()

check_prime()
