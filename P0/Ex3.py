from Seq0 import *

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "U5"]

print("-----| Exercise 3 |------")

for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + EXT)
    print(f"Gene {gene} ---> Length: {seq_len(seq)}")
