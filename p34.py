# Given a universal set, set A and Set B of your choice, implement de Morgan’s laws in python

# Define universal set, A, and B
U = set(range(1, 21))  # Universal set with elements 1 to 20
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# De Morgan's laws


complement_A = U - A
complement_B = U - B

# Law 1: Complement of the union = intersection of complement
LHS = U - (A | B)
RHS = complement_A & complement_B

print(LHS == RHS) 

# Law 2: Complement of the intersection = union of complement
LHS = U - (A & B)
RHS = complement_A | complement_B

print(LHS == RHS)  
