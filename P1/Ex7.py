from Seq1 import Seq

PRACTICE = 1
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

for i, s in enumerate([s1, s2, s3]):
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    print(f"  Bases: {s.count()}")
    print(f"  Rev:   {s.reverse()}")
