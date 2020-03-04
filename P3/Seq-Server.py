import socket
import termcolor
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8080

# -- Sequences for the GET command
SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


def get_cmd(n):
    """GET command
    returns: a sequence
    """
    return SEQ_GET[n]


def info_cmd(strseq):
    """INFO seq
    returns: The string with the information
    """
    # -- Create the object sequence from the string
    s = Seq(strseq)
    sl = s.len()
    ca = s.count_base('A')
    pa = "{:.1f}".format(100 * ca / sl)
    cc = s.count_base('C')
    pc = "{:.1f}".format(100 * cc / sl)
    cg = s.count_base('G')
    pg = "{:.1f}".format(100 * cg / sl)
    ct = s.count_base('T')
    pt = "{:.1f}".format(100 * ct / sl)

    resp = f"""Sequence: {s}
Total length: {sl}
A: {ca} ({pa}%)
C: {cc} ({pc}%)
G: {cg} ({pg}%)
T: {ct} ({pt}%)"""
    return resp


def comp_cmd(strseq):
    # -- Create the object sequence from the string
    s = Seq(strseq)
    return s.complement()


def rev_cmd(strseq):
    # -- Create the object sequence from the string
    s = Seq(strseq)
    return s.reverse()


def gene_cmd(name):
    s = Seq()
    s.read_fasta(FOLDER + name + EXT)
    return str(s)


# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # -- Receive the request message
        req_raw = cs.recv(2000)
        req = req_raw.decode()

        # ------ Process the command
        # -- Remove the \n
        lines = req.split("\n")
        line0 = lines[0].strip()

        # -- Separate the line into command an argument
        # -- Eliminate the blank spaces
        lcmds = line0.split(' ')

        # -- The first element is the command
        cmd = lcmds[0]

        # -- Get the first argument
        try:
            arg = lcmds[1]
        except IndexError:
            # -- No arguments
            arg = ""

        # -- Response message
        response = ""

        if cmd == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!"
        elif cmd == "GET":
            termcolor.cprint("GET", 'green')
            response = get_cmd(int(arg))
        elif cmd == "INFO":
            termcolor.cprint("INFO", 'green')
            response = info_cmd(arg)
        elif cmd == "COMP":
            termcolor.cprint("COMP", 'green')
            response = comp_cmd(arg)
        elif cmd == "REV":
            termcolor.cprint("REV", 'green')
            response = rev_cmd(arg)
        elif cmd == "GENE":
            termcolor.cprint("GENE", 'green')
            response = gene_cmd(arg)
        else:
            termcolor.cprint("Unknown command!!!", 'red')
            response = "Unkwnown command"

        # -- Send the response message
        response += '\n'
        print(response)
        cs.send(response.encode())
        cs.close()
