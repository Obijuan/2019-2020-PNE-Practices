from Seq1 import Seq

PRACTICE = 1
EXERCISE = 9

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FOLDER + GENES[0] + EXT)

print(f"Sequence : (Length: {s.len()}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Rev:   {s.reverse()}")
print(f"  Comp:  {s.complement()}")
