from Seq0 import *

PRACTICE = 5
FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ['A', 'C', 'T', 'G']

print(f"-----| Exercise {PRACTICE} |------")

for gene in GENES:
    seq = seq_read_fasta(FOLDER + GENES[0] + EXT)
    print(f"Gene {gene}: {seq_count(seq)}")
