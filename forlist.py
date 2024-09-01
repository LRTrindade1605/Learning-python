print(list(range(4)))
# [0, 1, 2, 3]

print(list(range(0, 100, 2)))
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,34,
 #36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64,66,
 # 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

spam = list(range(0, 100, 2))
print(spam)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range (len(supplies)):
    print('Index ' + str(i) + ' in supplies is ' + supplies[i])
#essa lista pode ser de qualquer tamanho que ira funcionar de qualquer forma


#forma normal de atribuicao de valores 
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size)
print(color)
print(disposition)

#forma de multiatribuicao de valores (faz a mesma coisa que o acima, so que com uma linha unica de codigo)
size, color, disposition = cat
print(size)
print(color)
print(disposition)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size)
print(color)
print(disposition)

