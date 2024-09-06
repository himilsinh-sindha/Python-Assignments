A = {'this', 1, 15, 'is a', 11, 53, 21, 'nice'}
B = {'that', 2, 53, 'was a', 54, 11, 'day'}
C = {'how', 3, 67, 'do you', 53, 2, 54, 24}
D = {'that', 2, 34, 56, 53, 'was a', 54, 12, 11, 'day', 'night'}

# Intersection of A and B
print("Intersection of A and B:", A & B)

# Intersection of A, B, and C
print("Intersection of A, B, and C:", A & B & C)

# Symmetric difference of A and C
print("Symmetric difference of A and C:", A ^ C)

# Union of B and C
print("Union of B and C:", B | C)

# Check if A is a subset of B
print("A is a subset of B:", A.issubset(B))

# Check if B is a proper subset of D
print("B is a proper subset of D:", B < D)

# Difference of B and D
print("Difference of B and D:", B - D)
