import unittest
from model.chunk_to_input_label import ChunkToInputLabel


class Chunk2InputLabelTest(unittest.TestCase):
    def setUp(self):
        config_path = "..\letters.xlsx"
        self.text2model = ChunkToInputLabel(config_path)


