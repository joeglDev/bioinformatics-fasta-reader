from components.read_fasta import read_fasta
from pipelines.classes.fasta_sequence import FastaSequence


def main():
    file_path = "../data/ATP5MC3_ENSG00000154518.fasta"
    initial_seq = read_data(file_path)


def read_data(file_path: str) -> FastaSequence:
    seq = read_fasta(file_path)
    print(f"FASTA Metadata: {seq.Id}")
    print(f"DNA Sequence: {seq.Seq}")
    print(f"DNA Sequence length: {seq.Length}")
    print(f"DNA GC content: {seq.Gc_content}")

    return seq


main()
