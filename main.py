from itertools import product

n = int(input("Enter n: "))
M = range(1, n + 1)
U = list(product(M, M))

def transitive_condition(relation, a, b, c):
    return (((a, b) in relation) and ((b, c) in relation)) <= ((a, c) in relation)

def is_transitive(relation, n):
    for a, b, c in product(M, repeat=3):
        if not transitive_condition(relation, a, b, c):
            return False
    return True

idx = 1

print("relation", idx, ":" , "empty")
for mask in range(1, 2 ** len(U)):
    s = set()
    for i in range(len(U)):
        if mask & (1 << i):
            s.add(U[i])

    if is_transitive(s, n):
        idx += 1
        print("relation", idx, ":" , *s)

print("Total number of relations:", idx)
