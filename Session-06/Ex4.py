import termcolor


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


def print_seqs(seqs, color):
    """Print a list of sequences"""
    for seq in seqs:
        termcolor.cprint(f"Sequence {seqs.index(seq)}: (Length: {seq.len()}) {seq}", color)


def generate_seqs(pattern, number):
    """Generate a list of sequences in which the give patter is repeated
       from 1 to number
       Return a list with all the sequences
    """
    seqs = []

    for i in range(1, number + 1):
        seqs.append(Seq(pattern * i))

    return seqs


# -- Main program

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1", 'blue')
print_seqs(seq_list1, "blue")


termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')
