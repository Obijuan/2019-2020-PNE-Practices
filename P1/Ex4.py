from Seq1 import Seq

PRACTICE = 1
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(f"Sequence 3: (Length: {s3.len()}) {s3}")
