from serial import Serial

with Serial("/dev/ttyUSB1", 115200) as sp:
    sp.write(b"t\n")
