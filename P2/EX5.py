from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.45"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "U5"

# -- Create a client object
c = Client(IP, PORT)

# -- Print the IP and PORTs
print(c)

# -- Read the Gene from a file
s = Seq().read_fasta(FOLDER + GENE + EXT)

# -- Send the Gene
c.debug_talk(f"Sending {GENE} Gene to the server...")
c.debug_talk(str(s))
