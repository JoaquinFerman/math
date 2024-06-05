from sorted_pairs_apk.operators import *

m1 = input('Ingrese la primera matriz separando los numeros con espacios: ')
m2 = input('Ingrese la segunda matriz separando los numeros con espacios: ')

product = pair_product(m1, m2)

relation = pair_relation(product, m1, m2)

properties = pair_properties(product)

print(product)
print(relation)
print(properties)