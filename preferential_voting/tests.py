# checking dictionary equality

A ={'A': None, 'B': 2, 'C': 3, 'D': 1, 'E': None, 'F': None}

B = {'A': None, 'B': 1, 'C': None, 'D': 3, 'E': 2, 'F': None}
C = {'A': 4, 'B': 1, 'C': None, 'D': 3, 'E': 5, 'F': 2}

Aa = A
Ab = {'A': None, 'B': 2, 'C': 3, 'D': 1, 'E': None, 'F': None}

print(A is Aa)
print(A == Aa)
print(A is Ab)
print(A == Ab)
print(B)
D=B.copy()
D['A'] = 1
print(B)
print(D)