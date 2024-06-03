
def pair_input(msg):
    pair = input(msg)
    return pair

def pair_product(pair_1:list, pair_2:list):
    product = []

    for x in pair_1:
        for y in pair_2:
            product.append([x, y])

    return product

def pair_relation(product:list, condition:str):
    output = []

    try:
        for x, y in product:
            x, y = int(x), int(y)
            if eval(condition):
                output.append([x, y])
    except:
        pass

    return output

def pair_properties(product:list):
    output = 'Relacion vacia'
    if product != []:
        a = symetry(product)
        b = transitivity(product)
        c = reflexivity(product)
        output = {'symmetry':a, 'transitivity':b, 'reflexivity':c}

    return output

def symetry(product:list):
    output = 'No simetrica'
    symetry_counter = 0

    for x, y in product:
        if [y, x] in product:
            symetry_counter += 1

    if symetry_counter == 0:
        output = 'Anti Simetrica'
    elif symetry_counter == len(product):
        output = 'Simetrica'

    return output

def reflexivity(product:list):
    output = 'No Reflexiva'
    reflex_counter = 0

    for x, y in product:
        if [x, x] in product:
            reflex_counter += 1
        if [y, y] in product:
            reflex_counter += 1
    
    if reflex_counter == len(product)*2:
        output = 'Reflexiva'
    elif reflex_counter == 0:
        output = 'Anti Reflexiva'
    
    return output

def transitivity(product:list):
    output = 'No Transitiva'
    transitive_counter = 0

    for x, y in product:
        for p, z in product:
            if [x, y] in product and [y, z] in product:
                if [x, z] in product:
                    transitive_counter += 1
                    break
            else:
                transitive_counter += 1
    
    if transitive_counter == len(product):
        output = 'Transitiva'
    elif transitive_counter == 0:
        output = 'Anti Transitiva'
    
    return output