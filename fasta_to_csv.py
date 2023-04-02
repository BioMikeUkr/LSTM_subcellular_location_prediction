#run from console in folder with target file as python fasta_to_csv.py сytoplasm.fasta
from Bio import SeqIO
import csv
import sys

# Check that the correct number of arguments were provided
if len(sys.argv) != 2:
    print("Usage: python fasta_to_csv.py <filename.fasta>")
    sys.exit(1)

# Get the input filename from the command line argument
filename = sys.argv[1]

# Get the class name from the input filename
class_name = filename.split(".")[0]

# Open the input and output files
with open(filename, "r") as fasta_file, open(f"{class_name}.csv", "w", newline="") as csv_file:

    # Set up the CSV writer
    writer = csv.writer(csv_file)
    writer.writerow(["class", "sequence"])

    # Loop over each sequence in the input fasta file
    for record in SeqIO.parse(fasta_file, "fasta"):

        # Write the class name and sequence to the CSV file
        writer.writerow([class_name, str(record.seq)])

print(f"Conversion complete. Results saved to {class_name}.csv")

