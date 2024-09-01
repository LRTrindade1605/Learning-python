def div42By(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42By(2))
print(div42By(12))
print(div42By(0))
print(div42By(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats. ')
    else:
        print('Thats is not that many cats. ')
except ValueError:
    print('You did not enter a number. ')
if int (numCats) <= 0:
    print('It is impossible to have this number of cats. ')
