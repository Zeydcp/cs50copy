import csv
import sys


def main():
    # TODO: Check for command-line usage
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py databases/size.csv sequences/number.txt")

    # TODO: Read database file into a variable
    dictionaries = []
    with open(sys.argv[1]) as file:
        reader0 = csv.DictReader(file)

        with open(sys.argv[1]) as file:
            reader1 = csv.reader(file)
            row0 = list(reader1)[0]

            for dictionary in reader0:
                for subsequence in row0[1:]:
                    dictionary[subsequence] = int(dictionary[subsequence])
                dictionaries.append(dictionary)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as f:
        sequence = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    counts = {}
    for subsequence in row0[1:]:
        counts[subsequence] = longest_match(sequence, subsequence)

    # TODO: Check database for matching profiles
    for dictionary in dictionaries:
        exact_match = 0
        for subsequence in row0[1:]:
            if counts[subsequence] == dictionary[subsequence]:
                exact_match += 1

        if exact_match == len(row0[1:]):
            print(dictionary["name"])
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
