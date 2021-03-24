
def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    #open files
    database_file = open("./" + argv[1])
    dna_file = open ("./" + argv[2])

    #get STRs from header of databse
    database_reader = csv.DictReader(database_file)
    strs = database_reader.fieldnames[1:]

    #copy contents and close the file
    dna = dna_file.read()
    dna_file.close()

    #count how many times each STR appears
    dna_fingerprint = {}
    for str in strs:
        dna_fingerprint[str] = consec_repeats(str, dna)

    #find match in csv file
    for row in database_reader:
        if match(strs, dna_fingerprint, row):
            print(f"{row['name']}")
            database_file.close()
            return
        else:
            print("No match")
            database_file.close()

def consec_repeats(str, dna):
    i = 0
    while str*(i + 1) in dna:
        i += 1
    return i


