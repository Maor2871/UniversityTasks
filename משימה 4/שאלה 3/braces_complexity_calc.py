from random import randint, choice


def valid_braces_placement(s, L, summ):
    """
        The function receives a list of numbers and operations. It returns True if there exists a braces placement on the expression which produces the results s.
    """
    
    # Check if the current braces placement is valid.
    if len(L) == 1:
        if L[0] == s:
            return True
        return False
    
    # Iterate over the list.
    for i in range(0, len(L) - 1, 2):
        summ[0] += len(L)
        # Place the braces in i.
        braces_in_i = L[:i] + [eval(str(L[i]) + L[i + 1] + str(L[i + 2]))] + L[i+3:]

        # Try to add more braces, check if can reach s.
        if valid_braces_placement(s, braces_in_i, summ):
            return True

    # No braces placement did the job.
    return False

n = 10
A = []

for i in range(n - 1):

    A.append(randint(0, 10))
    A.append(choice(["+", "-", "*"]))

A.append(randint(0, 10))
summ = [0]

print(A)

print(valid_braces_placement(10 ** n, A, summ))

print(summ[0])
