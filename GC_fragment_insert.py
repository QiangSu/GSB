import sys

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = (gc_count / len(sequence)) * 100
    return gc_content

def process_sam_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('@'):
                continue  # Skip header lines
            fields = line.strip().split()
            read_id = fields[0]
            sequence = fields[9]
            gc_content = calculate_gc_content(sequence)
            print(f"{read_id}\t{gc_content:.2f}%")

if __name__ == "__main__":
    sam_file = sys.argv[1]
    process_sam_file(sam_file)