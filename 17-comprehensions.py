# Comprehensions

# Los comprehensions son una forma de transformar listas (map() en javascript)


# comprehensions en listas
number_list = list(range(100))
print("Lista de numeros {}".format(number_list))


pares = [numero for numero in number_list if numero % 2 == 0]
print ("Lista de numeros pares {}".format(pares))



# comprehensions dictionary
students_uid = [1,2,3]
students = ['juan','jose','larsen']

students_with_uid = {uid: student  for uid, student in zip(students_uid,students)}
print("Dictionary de students con id {}".format(students_with_uid))


# comprehensions set
import random

random_number = []
for i in range(10):
    random_number.append(random.randint(1,3))

print("Lista de numeros {}".format(random_number))

non_repeated = {number for number in random_number}
print("set de numeros sin repetir {}".format(non_repeated))