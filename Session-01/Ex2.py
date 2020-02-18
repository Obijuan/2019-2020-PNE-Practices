class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object

        # -- Valid bases
        bases = ['A', 'C', 'G', 'T']

        # -- Check that the string used for the initialization
        # -- only contains valid bases
        for b in strbases:
            if b not in bases:
                print("ERROR!!")
                self.strbases = "ERROR"
                return

        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


def print_seqs(seqs):
    """Print a list of sequences"""
    for seq in seqs:
        print(f"Sequence {seqs.index(seq)}: (Length: {seq.len()}) {seq}")


# -- Main program
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)
