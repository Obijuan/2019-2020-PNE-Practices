from pathlib import Path


def seq_ping():
    """
    Test function
    """
    print("OK")


def seq_read_fasta(filename):
    """
    Read a file with a DNA sequence in FASTA format
    :param filename: String
    :return: String
    """

    # -- Read the file
    contents = Path(filename).read_text()

    # -- Remove the head
    body = contents.split('\n')[1:]

    # -- Return the body as a string
    return "".join(body)


def seq_count_base(seq, base):
    """
    Counting the give base on the sequence
    :param seq: String
    :param base: Character
    :return: Integer
    """
    return seq.count(base)


def seq_count(seq):
    """
    Calculate the number of bases in the sequence
    :param seq: String
    :return: Dictionary with the results
    """
    res = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'),
           'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')}
    return res


def seq_len(seq):
    return len(seq)


def seq_perc(seq):
    num = seq_count(seq)
    for b in ['A', 'T', 'C', 'G']:
        num[b] = round(100.0 * num[b] / seq_len(seq), 1)
    return num


def seq_reverse(seq):
    """
    Return the reverse sequence
    :param seq: String
    :return: String
    """
    return seq[::-1]


def seq_complement(seq):
    """
    Return the complement sequence
    :param seq: String
    :return: String
    """

    # -- Dictionary of complement bases
    basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    res = ""

    for b in seq:
        res += basec[b]

    return res
