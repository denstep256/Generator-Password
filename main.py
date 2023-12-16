import random
import string

symbols = list(string.punctuation)
numbers = list('0123456789')
letters = list(string.ascii_letters)
final_line = ""

# Generate a random symbol, letter, or number and add them to final_line
for i in range(20):
    choice = random.choice([symbols, numbers, letters]*2 + [letters]) # adding letters twice to have more chance of getting letters
    if choice == symbols:
        symbol = random.choice(symbols)
        final_line += symbol
        symbols.remove(symbol)
    elif choice == numbers:
        number = random.choice(numbers)
        final_line += number
        numbers.remove(number)
    else:
        letter = random.choice(letters)
        final_line += letter
        letters.remove(letter)

print(final_line)
