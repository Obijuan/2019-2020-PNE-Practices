class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        """Init method. It creates a new object"""

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

    def __str__(self):
        """Returns a string with the bases"""
        return self.strbases

    def len(self):
        """Calculate the total length of the sequence"""
        return len(self.strbases)

    def count(self, base):
        """Calculate the number of the given base in the sequence"""
        return self.strbases.count(base)

    def rev(self):
        return Seq(self.strbases[::-1])

    def comp(self):
        # -- Dictionary of complement bases
        basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

        res = ""

        for b in self.strbases:
            res += basec[b]

        return Seq(res)


# -- Main program
s1 = Seq("AACTG")
s2 = Seq("TACTA")

for i, s in enumerate([s1, s2]):
    print(f"Sequence {i+1}: {s}")
    print(f"  Length: {s.len()}")
    print(f"  A: {s.count('A')}")
    print(f"  T: {s.count('T')}")
    print(f"  C: {s.count('C')}")
    print(f"  G: {s.count('G')}")
    print(f"  Reverse: {s.rev()}")
    print(f"  Complement: {s.comp()}")
    print()
