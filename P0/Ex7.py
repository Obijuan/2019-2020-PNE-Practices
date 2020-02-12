from Seq0 import *

PRACTICE = 7
FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ['A', 'C', 'T', 'G']

print(f"-----| Exercise {PRACTICE} |------")

GENE = GENES[0]
print(f"Gene {GENE}:")
seq = seq_read_fasta(FOLDER + GENES[0] + EXT)[:20]
comp = seq_complement(seq)
print(f"Frag: {seq}")
print(f"Comp: {comp}")
