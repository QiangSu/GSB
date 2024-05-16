def calculate_gc_content(seq):
    """ Returns the GC content percentage for a given DNA sequence. """
    if len(seq) == 0:  # Avoid division by zero
        return 0
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100


def main():
    frequency = {}  # Dictionary to store frequency of each GC content value

    with open('reads.fasta', 'r') as file:
        for line in file:
            line = line.strip()  # Remove newline character
            if line:  # Ensure the line isn't empty
                gc_content = round(calculate_gc_content(line), 1)  # Calculate and round GC content to 1 decimal
                if gc_content in frequency:
                    frequency[gc_content] += 1  # Increment count of this particular GC content
                else:
                    frequency[gc_content] = 1  # Initialize count for this GC content

    # Output the results:
    output_file = 'ENST00000229239_gc_content_distribution.txt'  # Define output file name
    with open(output_file, 'w') as out:
        out.write("GC_Content_Percentage\tCount\n")  # Writing header for the file
        for gc_content, count in sorted(frequency.items()):  # Sort by GC content percentage
            out.write(f"{gc_content}\t{count}\n")  # Write each GC content and its count to file

    print(f"GC Content distribution saved to {output_file}")


if __name__ == '__main__':
    main()
