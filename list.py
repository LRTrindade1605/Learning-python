spam = ['cat', 'bat', 'dog', 'elephant']
for listNum in range (0, 4):
    print(spam[listNum])

spam = [['cat', 'bat'], [1, 2, 3, 4, 5]]
for listNum in range (0, 2):
    try:
        for numElement in range (0,5):
            print(spam[listNum][numElement])
    except IndexError:
        continue

##################################


# sobreposicao de elementos
spam = [10, 20, 30]
spam[1] = 'Hello'
print(spam) #hello sobrepos o 20

#adicao e sobreposicao de elementos
spam[1:3] = ['cat', 'dog', 'mouse'] 
print(spam) #sobrepoe elementos de 1 a 2 e adiciona o elemento 3

#deletar elemento
del spam[2]
print(spam)

#soma de listas diferentes
spam1 = [5, 6, 7]
spam2 = spam1 + spam
print(spam2)

#multiplicacao de listas
spam3 = spam1 * 3
print(spam3) #[5, 6, 7, 5, 6, 7, 5, 6, 7]

##################
list('hello')
'howdy' in ['hello', 'hi', 'howdy'] #true - howdy esta nessa lista
##################
