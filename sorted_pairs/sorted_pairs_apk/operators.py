
def pair_input(msg):
    pair = input(msg)
    return pair

def pair_product(pair_1:list, pair_2:list):
    product = []

    for x in pair_1:
        for y in pair_2:
            product.append([x, y])

    return product

def pair_relation(product:list, condition:str, l1:list, l2:list):
    output = []
    output_matrix = [[0]*len(l2) for _ in range(len(l1))]
    cont_h = 0
    cont_v = 0

    for x, y in product:
        x, y = int(x), int(y)
        try:
            if eval(condition):
                output.append([x, y])
                output_matrix[cont_v][cont_h] = 1
        except:
            pass
        cont_h += 1
        if cont_h == len(l2):
            cont_h = 0
            cont_v += 1

    return {'relation':output, 'relation_matrix':output_matrix}

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
    anti_counter = 0

    for x, y in product:
        if [y, x] in product:
            symetry_counter += 1
            if [x, x] in product:
                anti_counter += 1

    if symetry_counter == 0:
        output = 'Asimetrica'
    elif symetry_counter == anti_counter:
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
            if [y, z] in product:
                if [x, z] in product:
                    transitive_counter += 1
                    break
            else:
                transitive_counter += 1
                break
    
    if transitive_counter == len(product):
        output = 'Transitiva'
    elif transitive_counter == 0:
        output = 'Anti Transitiva'
    
    return output