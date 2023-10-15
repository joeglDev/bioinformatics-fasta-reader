from Bio import Seq


class FastaSequence:
    def __init__(self, fasta_id: str, seq: Seq, length: int):
        self.Id = fasta_id
        self.Seq = seq
        self.Length = length

