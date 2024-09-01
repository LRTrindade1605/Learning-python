cat = {'name': 'Zophie', 'age': '7', 'color': 'gray'}
allCats = []
allCats.append({'name': 'Zophie', 'age': '7', 'color': 'gray'})
allCats.append({'name': 'Pooka', 'age': '5', 'color': 'black'})
allCats.append({'name': 'Fat-Tail', 'age': '5', 'color': 'gray'})
allCats.append({'name': '???', 'age': '-1', 'color': 'orange'})
print(allCats)

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
import pprint
pprint.pprint(theBoard)
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print(printBoard(theBoard))
print('Will you play as X or O?')
XorO = input()
if XorO == 'X':
    OorX = 'O'
else:
    OorX = 'X'
for i in range(0, 18):
    print('Which square do you want to put your ' + XorO + '?')
    print('you can choose the X axis by typing top-, mid- or low-,'
          'and the Y axis by typing L, M or R, after the X axis.'
          'example: low-R')
    squarePos = input()
    if ['top-L'] == 'X' or ['top-L'] == 'O':
        print('this place has already been marked. Try again.')
    elif ['top-M'] == 'X' or ['top-M'] == 'O':
        print('this place has already been marked. Try again.')
    elif ['top-R'] == 'X' or ['top-R'] == 'O':
        print('this place has already been marked. Try again.')
    elif ['mid-L'] == 'X' or ['mid-L'] == 'O':
        print('this place has already been marked. Try again.')
    elif ['mid-M'] == 'X' or ['mid-M'] == 'O':
        print('this place has already been marked. Try again.')
    elif ['mid-R'] == 'X' or ['mid-R'] == 'O':
        print('this place has already been marked. Try again.')
    elif ['low-L'] == 'X' or ['low-L'] == 'O':
        print('this place has already been marked. Try again.')
    elif ['low-M'] == 'X' or ['low-M'] == 'O':
        print('this place has already been marked. Try again.')
    elif ['low-R'] == 'X' or ['low-R'] == 'O':
        print('this place has already been marked. Try again.')
    elif squarePos == 'top-L':
        theBoard['top-L'] = XorO
        printBoard(theBoard)
    if squarePos == 'top-M':
        theBoard['top-M'] = XorO
        printBoard(theBoard)
    if squarePos == 'top-R':
        theBoard['top-R'] = XorO
        printBoard(theBoard)
    if squarePos == 'mid-L':
        theBoard['mid-L'] = XorO
        printBoard(theBoard)
    if squarePos == 'mid-M':
        theBoard['mid-M'] = XorO
        printBoard(theBoard)
    if squarePos == 'mid-R':
        theBoard['mid-R'] = XorO
        printBoard(theBoard)
    if squarePos == 'low-L':
        theBoard['low-L'] = XorO
        printBoard(theBoard)
    if squarePos == 'low-M':
        theBoard['low-M'] = XorO
        printBoard(theBoard)
    if squarePos == 'low-R':
        theBoard['low-R'] = XorO
        printBoard(theBoard)
    print('Which square do you want to put your ' + OorX + '?')
    print('you can choose the X axis by typing top-, mid- or low-,'
          'and the Y axis by typing L, M or R, after the X axis.'
          'example: low-R')
    squarePos = input()
    if ['top-L'] == 'X' or ['top-L'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if ['top-M'] == 'X' or ['top-M'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if ['top-R'] == 'X' or ['top-R'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if ['mid-L'] == 'X' or ['mid-L'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if ['mid-M'] == 'X' or ['mid-M'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if ['mid-R'] == 'X' or ['mid-R'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if ['low-L'] == 'X' or ['low-L'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if ['low-M'] == 'X' or ['low-M'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if ['low-R'] == 'X' or ['low-R'] == 'O':
        print('this place has already been marked. Try again.')
        continue
    if squarePos == 'top-L':
        theBoard['top-L'] = OorX
        printBoard(theBoard)
    if squarePos == 'top-M':
        theBoard['top-M'] = OorX
        printBoard(theBoard)
    if squarePos == 'top-R':
        theBoard['top-R'] = OorX
        printBoard(theBoard)
    if squarePos == 'mid-L':
        theBoard['mid-L'] = OorX
        printBoard(theBoard)
    if squarePos == 'mid-M':
        theBoard['mid-M'] = OorX
        printBoard(theBoard)
    if squarePos == 'mid-R':
        theBoard['mid-R'] = OorX
        printBoard(theBoard)
    if squarePos == 'low-L':
        theBoard['low-L'] = OorX
        printBoard(theBoard)
    if squarePos == 'low-M':
        theBoard['low-M'] = OorX
        printBoard(theBoard)
    if squarePos == 'low-R':
        theBoard['low-R'] = OorX
        printBoard(theBoard)
        

    
