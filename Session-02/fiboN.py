# -- Session 2. Exercise 2
# -- Print the 5th, 10th and 15th term of the fibonacci series
# -- They should be calculated by calling to the fibon(n) function


def fibon(n):

    # -- For the term 0 and 1 no calculation is requiered
    if n in [0, 1]:
        return n

    n1 = 0
    n2 = 1

    # -- parcial result
    term_n = 0

    # -- calculate the nth term
    for i in range(2, n+1):
        term_n = n1 + n2

        # -- update the previous terms
        n1 = n2
        n2 = term_n

    return term_n


# -- Main program
print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term:", fibon(10))
print("15th Fibonacci term:", fibon(15))
