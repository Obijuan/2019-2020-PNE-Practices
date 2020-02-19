from Seq1 import *

PRACTICE = 1
EXERCISE = 10

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'T', 'C', 'G']

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

for gene in GENES:

    # -- Create the sequence from a file
    s = Seq().read_fasta(FOLDER + gene + EXT)

    # -- Dictionary with the values
    d = s.count()

    # -- Create a list with all the values
    ll = list(d.values())

    # -- Calculate the maximum
    m = max(ll)

    # -- Print the base
    print(f"Gene {gene}: Most frequent Base: {BASES[ll.index(m)]}")
