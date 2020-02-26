from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.45"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

# -- Create the client objects for connecting to the servers
c1 = Client(IP, PORT)
c2 = Client(IP, PORT + 1)

# -- Print the IP and PORTs
print(c1)
print(c2)

# -- Read the Gene from a file
s = Seq().read_fasta(FOLDER + GENE + EXT)

# -- Get the gene string
bases = str(s)

# -- Print the Gene on the console
print(f"Gene {GENE}: {bases}")

# -- Length of fragments
LENGTH = 10

# -- Send the initial message to both servers
init_msg = f"Sending {GENE} Gene to the server, in fragments of {LENGTH} bases..."

c1.talk(init_msg)
c2.talk(init_msg)

# -- Create the framents and sent them to the servers
for i in range(10):

    # -- Create fragment i
    frag = bases[i*LENGTH:(i+1)*LENGTH]

    # -- Print on Client's console
    print(f"Fragment {i+1}: {frag}")

    # -- Message to send to the server
    msg = f"Fragment {i+1}: {frag}"

    # -- even fragments (counting from 0) are sent to server 1
    if i % 2:
        c1.talk(msg)

    # -- Odd segments are sent to server 2
    else:
        c2.talk(msg)
