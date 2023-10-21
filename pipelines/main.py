from datetime import datetime

from pipelines.classes.fasta_sequence import FastaSequence
from pipelines.components.file_io import create_new_file
from pipelines.components.read_fasta import read_fasta
from pipelines.components.transcribe_mrna import transcribe_dna_to_mrna
from pipelines.components.translate_protein import translate_mrna_to_protein


def main():
    # dna manipulation
    file_path = "../data/ATP5MC3_ENSG00000154518.fasta"
    dna_seq = read_data(file_path)
    get_mrna(dna_seq)
    get_protein(dna_seq)

    # write to file
    file_name = f"{datetime.now()}_output_{dna_seq.Id}"
    create_new_file(file_name, dna_seq)


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


def get_protein(dna_seq):
    translate_mrna_to_protein(dna_seq)
    print(f"Protein sequence: {dna_seq.Protein_seq}")
    print(f"Protein sequence to stop: {dna_seq.Protein_seq_to_stop}")


main()
