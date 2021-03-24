# argv.py
from sys import argv
import csv


def main():
    # read dna db into memory as dict, by name
    database = {}
    with open(argv[1], newline='') as dbFile:
        reader = csv.reader(dbFile)

        # get STR sequence from headers
        STRseq = next(reader, None)[1:]
        for row in reader:
            database[row[0]] = row[1:]

    # read dna sequence into memory as string
    with open(argv[2], "r") as seqFile:
        sequence = seqFile.read().rstrip('\n')

    repetitions = []

    # for each STR defined in the DB file, repetitions are counted and stored
    for STR in STRseq:
        repetitions.append(countRepeatedStrSequences(STR, sequence))

    # using set to compare the two lists with each other
    for name, strValues in database.items():
        if set(strValues) == set(repetitions):
            print(name)
            return

    print("No match")
    return


def countRepeatedStrSequences(STR, sequence):
    """Walks over the DNA sequence and returns continues STR sequences as stringified value"""
    counter = 0
    for i in range(len(sequence)):
        if sequence[i: i + len(STR)] == STR:
            reps = strSearch(sequence, i, STR)
            if reps > counter:
                counter = reps
    return str(counter)


def strSearch(seq, pos, STR, repeatedStrSequences=0):
    """checks if STR sequence matches
    if match is found, continue until the last matching sequence is found
    repeatedStrSequences is increased with every call
    once the last STR sequence is found, we return the value of repeatedStrSequences
    """
    if seq[pos: pos + len(STR)] == STR:
        return strSearch(seq, pos + len(STR), STR, repeatedStrSequences + 1)
    return repeatedStrSequences


main()