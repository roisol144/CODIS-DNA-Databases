import re
import sys
import csv
from sys import argv, exit
from csv import reader, DictReader


dbfile = open(sys.argv[1], "r")
seqfile = open(sys.argv[2], "r")

input_sequence = seqfile.read()
dbdictreader = csv.DictReader(dbfile)

# create a dictionary where we will store the sequences we intend to count
sequences = {}

# extract the sequences from the database into a list
with open(argv[1]) as peoplefile:
    people = reader(peoplefile)
    for row in people:
        dnaSequences = row
        dnaSequences.pop(0)
        break

# copy the list in a dictionary where the genes are the keys
for item in dnaSequences:
    sequences[item] = 0

# Find the longest cosecutive run for certain STR


def longest_run(sequence, short_repeat):
    pattern = re.compile(f"((?:{short_repeat})+)")

    matches = pattern.findall(sequence)

    length = [len(i) for i in matches]

    if length == []:
        return 0

    return max(length) // len(short_repeat)


# Copying the STRs to the new dict
final_dict = {}
for gene in sequences:
    final_dict.update(sequences)

# Running longest_run on each DNA to return largest value of reps.
for key in final_dict:
    final_dict[key] = longest_run(input_sequence, key)

# Comparing the to the database values
for person in dbdictreader:
    match = 0
    # compares the sequences to every person and prints name before leaving the program if there is a match
    for dna in final_dict:
        if final_dict[dna] == int(person[dna]):
            match += 1
    if match == len(final_dict):
        print(person['name'])
        exit()

print("No match")
