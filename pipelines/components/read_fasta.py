from Bio import SeqIO, Seq
from Bio.SeqUtils import GC

from pipelines.classes.fasta_sequence import FastaSequence


def read_fasta(file_path: str) -> FastaSequence:
    default_seq = FastaSequence("", "", 0, "")

    for seq_record in SeqIO.parse(file_path, "fasta"):
        id: str = seq_record.id
        seq: Seq = seq_record.seq
        length: int = len(seq)
        gc_content = GC(seq)

        read_sequence = FastaSequence(id, seq, length, gc_content)
        default_seq.Id = read_sequence.Id
        default_seq.Seq = read_sequence.Seq
        default_seq.Length = read_sequence.Length
        default_seq.Gc_content = read_sequence.Gc_content

    return default_seq


