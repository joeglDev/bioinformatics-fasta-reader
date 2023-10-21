from pipelines.classes.fasta_sequence import FastaSequence


def create_new_file(file_name: str, output: FastaSequence):
    lines = [f"{output.Id}", "DNA sequence length:", f"{output.Length}", "DNA sequence GC content:", f"{str(output.Gc_content)}", "DNA sequence:", f"{str(output.Seq)}", "MRNA coding sequence:", f"{str(output.Mrna_seq)}", "Protein sequence:", f"{str(output.Protein_seq)}"]
    try:
        with open(f'outputs/{file_name}', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')
    except FileNotFoundError:
        print("The directory does not exist")