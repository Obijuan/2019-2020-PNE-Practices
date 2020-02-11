from pathlib import Path

FILENAME = "ADA.txt"

contents = Path(FILENAME).read_text()

# -- Remove the first line
lines = contents.split('\n')

# -- Build the body without \n characteres
body = "".join(lines[1:])

# -- Calculate the number of bases
print(f"Length of the sequence: {len(body)}")
