def count_gc_content(filename):
    gc_content_count = {}
    total_count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                parts = line.split()
                gc_content = float(parts[1].replace('%', ''))
                # Round GC content to reduce variability
                gc_content = round(gc_content, 1)

                if gc_content in gc_content_count:
                    gc_content_count[gc_content] += 1
                else:
                    gc_content_count[gc_content] = 1

                total_count += 1

    return gc_content_count, total_count


def write_gc_frequency_to_file(gc_counts, output_file):
    with open(output_file, 'w') as f:
        for gc_content, count in sorted(gc_counts.items()):
            f.write(f"GC Content: {gc_content}% - Frequency: {count}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python3 calc_gc_frequency.py <input_file> <output_file>")
        sys.exit(1)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    gc_counts, total_reads = count_gc_content(input_filename)
    write_gc_frequency_to_file(gc_counts, output_filename)
    print(f"Results written to {output_filename}")
