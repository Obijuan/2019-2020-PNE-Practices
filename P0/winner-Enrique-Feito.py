from Seq0 import *

print("-----| Exercise 8 |------")

FOLDER = "../Session-04/"
bases = ["A", "C", "T", "G"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for file in files_list:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    dict_bases = seq_count(sequence)
    min_value = 0
    best_base = ""
    for base, value in dict_bases.items():
        while value > min_value:
            min_value = value
            best_base = base

    print("Gene", file, " : Most frequent Base: ", best_base)
