from pathlib import Path


class Seq:

    # -- Identification string for the Null and Invalid sequences
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):
        """Constructor:
        :type strbases: string with the bases of the sequence
        """

        # -- Check if it is the null seq
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL Seq created")
            return

        # -- Check if the string passed by the user is valid
        if not self.valid_str(strbases):
            self.strbases = self.ERROR
            print("INVALID Seq!")
            return

        # -- Store the string in the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    @staticmethod
    def ping():
        print("PING OK")

    @staticmethod
    def valid_str(strbases):
        """Check if the string is valid or not"""

        # -- Valid bases
        valid_bases = ['A', 'C', 'T', 'G']

        for b in strbases:

            # -- IF one base is not valid...
            if b not in valid_bases:
                return False

        # -- All the bases are valid --> the string is valid
        return True

    def len(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0
        else:
            return len(self.strbases)

    def read_fasta(self, filename):
        """
            Read a file with a DNA sequence in FASTA format
            :param filename: String
            """

        # -- Read the file
        contents = Path(filename).read_text()

        # -- Remove the head
        body = contents.split('\n')[1:]

        # -- Store the sequence read from the file
        self.strbases = "".join(body)

    def count_base(self, base):
        """
        Counting the given base on the sequence
        :param base: Character
        :return: Integer
        """
        return self.strbases.count(base)

    def count(self):
        """
        Calculate the number of bases in the sequence
        :return: Dictionary with the results
        """
        res = {'A': self.count_base('A'), 'T': self.count_base('T'),
               'C': self.count_base('C'), 'G': self.count_base('G')}
        return res

    def reverse(self):
        """
        Return the reverse sequence
        :return: String
        """
        return self.strbases[::-1]

    def complement(self):
        """
        Return the complement sequence
        :return: String
        """

        # -- Dictionary of complement bases
        basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

        res = ""

        for b in self.strbases:
            res += basec[b]

        return res
