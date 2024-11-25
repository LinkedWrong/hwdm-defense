from itertools import product

n = int(input("Enter n: "))
M = range(1, n + 1)
U = list(product(M, M))

def transitive_condition(relation, a, b, c):
    return (((a, b) in relation) and ((b, c) in relation)) <= ((a, c) in relation)

def reflexive_condition(relation, a):
    return (a, a) in relation

def symmetric_condition(relation, a, b):
    return ((a, b) in relation) <= ((b, a) in relation)


def is_transitive(relation):
    for a, b, c in product(M, repeat=3):
        if not transitive_condition(relation, a, b, c):
            return False
    return True

def is_reflexive(relation):
    for a in M:
        if not reflexive_condition(relation, a):
            return False
    return True

def is_symmetric(relation):
    for a, b in product(M, repeat=2):
        if not symmetric_condition(relation, a, b):
            return False
    return True

def is_equivalent(relation):
    return is_reflexive(relation) and is_symmetric(relation) and is_transitive(relation)

idx = 0
for mask in range(1, 2 ** len(U)):
    s = set()
    for i in range(len(U)):
        if mask & (1 << i):
            s.add(U[i])

    if is_equivalent(s):
        idx += 1
        print("relation", idx, ":" , *s)

print("Total number of relations:", idx)
