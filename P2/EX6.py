from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.45"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

# -- Create a client object
c = Client(IP, PORT)

# -- Print the IP and PORTs
print(c)

# -- Read the Gene from a file
s = Seq().read_fasta(FOLDER + GENE + EXT)

# -- Get the gene string
bases = str(s)

# -- Print the Gene on the console
print(f"Gene {GENE}: {bases}")

# -- Length of fragments
LENGTH = 10

c.talk(f"Sending {GENE} Gene to the server, in fragments of {LENGTH} bases...")

# -- Create 5 framents and sent them to the server
for i in range(5):

    # -- Create fragment i
    frag = bases[i*LENGTH:(i+1)*LENGTH]

    # -- Print on Client's console
    print(f"Fragment {i+1}: {frag}")

    # -- Send the fragment to the server!
    c.talk(f"Fragment {i+1}: {frag}")

