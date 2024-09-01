myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

#para o dicionario, ordem nao importa:
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
eggs == ham

#checar se existe ou nao dentro do dicionario
if 'name' in eggs: # --> vai dar true
    print('True')
else:
    print('False')
if 'name' not in eggs: # --> vai dar false
    print('True')
else:
    print('False')

############
#comandos de dictonary
print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))
for k in eggs.keys(): 
    print(k) #--> classificacoes
for l in eggs.values(): 
    print(l) #--> valores das classificacoes
for m in eggs.items(): 
    print(m) #--> classificacoes e seus respectivos valores

print(eggs.get('age', 0)) #-----> no comando .get, ele vai procurar 'age' no dict, se nao tiver ira retornar 0.
print(eggs)
eggs.setdefault('color', 'black') #adiciona algo que nao existe no dict
print('depois de usar o .setdefault')
print(eggs)
eggs.setdefault('color', 'orange')
print(eggs) # --> ele nao muda valores ja existentes no dict
