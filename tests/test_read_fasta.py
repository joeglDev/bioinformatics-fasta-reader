from unittest import TestCase

from Bio.Seq import Seq

from pipelines.components.read_fasta import read_fasta
from tests.test_data import atp_synthase_seq


class TestFastaReader(TestCase):

    # issue does not assert equal for identical seq objects
    def test_good_data(self):
        id = "2|dna:chromosome|chromosome:GRCh38:2:175175658:175182310:-1"
        length = 6653
        seq = Seq(atp_synthase_seq)

        actual = read_fasta("../data/ATP5MC3_ENSG00000154518.fasta")
        TestFastaReader.assertEqual(self, id, actual.Id)
        TestFastaReader.assertEqual(self, length, actual.Length)
        TestFastaReader.assertEqual(self, type(seq), type(actual.Seq))

