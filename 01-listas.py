
# define list
emtyList = list()
myList = ['test',1,True,['1','two']]

# access to element
print(myList[3])

# add element to end
myList.append('john')

# get index
print('index de test {}'.format(myList.index('test')))

# remove element
myList.remove(1)
print('borrado con remove {}'.format(myList))


# remover usando del (tambien funciona con slices)
del myList[0:2] #elimina del primero al tercer elemento no incluyente
print('borrado con del {}'.format(myList))

# eliminar ultimo elemento y retorna el valor del elemento eliminado
deleted = myList.pop()
print('borrado con pop() {}'.format(deleted))
