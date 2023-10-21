from pipelines.classes.fasta_sequence import FastaSequence


def transcribe_dna_to_mrna(dna_seq: FastaSequence):

    mrna_seq = dna_seq.Seq.transcribe()
    dna_seq.Mrna_seq = mrna_seq

    return mrna_seq
