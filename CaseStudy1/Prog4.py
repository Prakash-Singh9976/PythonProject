'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose if the entered string is: Python0325
Then the output will be:LETTERS: 6
DIGITS:4'''

def countLetters_Numbers(sentence):
    lettersCount = 0
    numbersCount = 0
    for char in sentence:
        if char.isalpha():
            lettersCount += 1
        if char.isdigit():
            numbersCount += 1


    return lettersCount , numbersCount

inputString = input("Enter the sentence : ")

letters , digits = countLetters_Numbers(inputString)

print('Letters : ',letters)
print('Digits : ',digits)

