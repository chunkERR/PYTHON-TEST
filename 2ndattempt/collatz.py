def collatz(number):
    if number % 2 == 0:
        value = (number // 2)
        print(value)
        return value
    elif number % 2 != 0:
        value = (3 * number + 1)
        print(value)
        return value


try:
    userInput = input('Enter a number: ')
    while userInput != 1:
        userInput = collatz(int(userInput))
except:
    if userInput != type(int):
        print("You must enter a valid number.")
        


