from pipelines.classes.fasta_sequence import FastaSequence
from pipelines.components.read_fasta import read_fasta
from pipelines.components.transcribe_mrna import transcribe_dna_to_mrna


def main():
    file_path = "../data/ATP5MC3_ENSG00000154518.fasta"
    dna_seq = read_data(file_path)
    print(dna_seq.Mrna_seq)
    get_mrna(dna_seq)
    print(dna_seq.Mrna_seq)


def read_data(file_path: str) -> FastaSequence:
    seq = read_fasta(file_path)
    print(f"FASTA Metadata: {seq.Id}")
    print(f"DNA Sequence: {seq.Seq}")
    print(f"DNA Sequence length: {seq.Length}")
    print(f"DNA GC content: {seq.Gc_content}")

    return seq


def get_mrna(dna_seq: FastaSequence):
    transcribe_dna_to_mrna(dna_seq)
    print(f"MRNA sequence: {dna_seq.Mrna_seq}")


main()
