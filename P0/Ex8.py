from Seq0 import *

PRACTICE = 8
FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ['A', 'T', 'C', 'G']

print(f"-----| Exercise {PRACTICE} |------")

for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + EXT)

    # -- Dictionary with the values
    d = seq_count(seq)

    # -- Create a list with all the values
    ll = list(d.values())

    # -- Calculate the maximum
    m = max(ll)

    # -- Print the base
    print(f"Gene {gene}: Most frequent Base: {BASES[ll.index(m)]}")
