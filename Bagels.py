# Користувач вводить з клавіатури двозначне число. Наприклад, 26. Покажіть на різних рядках значення першого та другого розряду. У нашому випадку це виглядатиме так

# number = int(input("Enter number"))
# print(number//10)
# print(number%10)

# Користувач вводить з клавіатури тризначне число. Наприклад, 891. Покажіть на різних рядках значення першого, другого та третього розряду. Також виведіть на окремий рядок суму цих трьох чисел. У нашому випадку це виглядатиме так:

# number = int(input("Enter number"))
# c = number % 10
# number //=10
# b = number % 10
# a = number//10
# print(a)
# print(b)
# print(c)
# print((a + b + c))

# Користувач вводить з клавіатури дві цифри. Створіть
# число, яке містить ці цифри. Наприклад, якщо з клавіатури
# введено 9 та 7, ви маєте сформувати число 97.
# a = int(input("Enter first digit"))
# b = int(input("Enter second digit"))
# print(a * 10 + b)


# Користувач вводить з клавіатури температуру за
# шкалою Цельсія. Конвертуйте температуру в градуси за
# Фаренгейтом і виведіть показник на екран.

# deg = int(input("Enter value"))
# print(int(deg * 9 / 5 + 32) , "F")

# import os, sys
# os.system(sys.executable + ' -m pip install --user bigbookpython')

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game.
    By AL Sweigart 
    I am thinking of a {} - digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say :    That means:
        Pico        One digit is correct but in the wrong position
        Fermi       One digit is correct and in the right position
        Bagels      One digit is correct
        
    For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{} : '.format(numGuesses))
                guess = input('>')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You run out of guesses.')
                print('The answer was {}'.format(secretNum))
        print('Do you want to play again? (yes or no)')
        if not input('>').lower().startswith('y'):
            break


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main()
