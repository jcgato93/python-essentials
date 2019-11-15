# los sets (conjuntos) son muy similares a las listas 
# con la diferencia que esta no permite objetos repetidos

s = set([1,2,3])
t = set([3,4,5])

# unir los set
print(s.union(t))

# valores que no se repiten en t
print(s.difference(t))

# valores que no se repiten en s
print(t.difference(s))

# valores que estan en ambos sets
print(s.intersection(t))