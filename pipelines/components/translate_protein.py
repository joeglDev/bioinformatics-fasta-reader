from pipelines.classes.fasta_sequence import FastaSequence


def translate_mrna_to_protein(dna_seq: FastaSequence):
    dna_seq.Protein_seq = dna_seq.Mrna_seq.translate()
    dna_seq.Protein_seq_to_stop = dna_seq.Mrna_seq.translate(to_stop=True)