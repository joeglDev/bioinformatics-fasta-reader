from Bio import Seq


class FastaSequence:
    def __init__(self, fasta_id: str, seq: Seq, length: int, gc_content: float):
        self.Id = fasta_id
        self.Seq = seq
        self.Length = length
        self.Gc_content = gc_content
        self.Mrna_seq = None

