from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Cofigure the client
c = Client(IP, PORT)
print(c)

# -- Test 1: Ping
print("* Testing PING...")
print(c.talk("PING"))

# -- Test 2: Get
print("* Testing GET...")
for i in range(5):
    cmd = f"GET {i}"
    print(f"{cmd}: {c.talk(cmd)}", end="")

# -- Test 3: INFO
# -- Get the sequence 0 for testing
seq = c.talk("GET 0")
print()
print("* Testing INFO...")
cmd = f"INFO {seq}"
print(c.talk(cmd))

# -- Test 4: COMP
print("* Testing COMP...")
cmd = f"COMP {seq}"
print(cmd, end="")
print(c.talk(cmd))

# -- Test 5: REV
print("* Testing REV...")
cmd = f"REV {seq}"
print(cmd, end="")
print(c.talk(cmd))

# -- Test 6: GENE
print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    cmd = f"GENE {gene}"
    print(cmd)
    print(c.talk(cmd))
