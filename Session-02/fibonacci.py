# Session 2: Exercise 1: Fibonacci

# -- The first two terms (1 and 2) of the fibonacci series
n1 = 0
n2 = 1

# -- Print the first two initial term:
print("0 1", end=' ')

# -- Calculate the next terms (from 3 to 10)
for i in range(2, 11):

    # -- Calculate the new term
    term_n = n1 + n2

    # -- Print the new term
    print(term_n, end=' ')

    # -- update the previous terms
    n1 = n2
    n2 = term_n
