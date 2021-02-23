import unittest
from model.encoding.chunk_to_input_label import ChunkToInputLabel

from model.CharIdsSingleton import CharIdsSingleton

class Chunk2InputLabelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = "../resources/test_charIdsConfig.xlsx"
        CharIdsSingleton(path)

    def setUp(self):
        self.chunk2inputLabel = ChunkToInputLabel()

    def testIsvalidChunk(self):
        valid_chunk = "גֱ'"
        invalid_chunk = "ג(ֱ'"
        self.assertTrue(self.chunk2inputLabel.is_valid_chunk(valid_chunk))
        self.assertFalse(self.chunk2inputLabel.is_valid_chunk(invalid_chunk))

    def doTestChunkToInputLabel(self, chunk, expected_input, expected_label):
        self.assertEqual(self.chunk2inputLabel.chunk_to_input_label(chunk), (expected_input, expected_label))

    def testValid(self):
        self.doTestChunkToInputLabel("גֱ", 0, 0)
        self.doTestChunkToInputLabel("גֱ'", 1, 0)

    def testInvalid(self):
        self.doTestChunkToInputLabel("גֱ)", 0, 4)
        self.doTestChunkToInputLabel("גֱ')", 1, 4)



