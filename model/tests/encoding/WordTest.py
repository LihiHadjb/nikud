import unittest
from model.CharIdsSingleton import CharIdsSingleton
from model.encoding.Word import Word


class WordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = "../resources/test_charIdsConfig.xlsx"
        CharIdsSingleton(path)

    def setUp(self):
        self.cid = CharIdsSingleton.get_instance()

    def doTestWord(self, word, expected_chunks):
        actual_chunks = []

        word_iter = iter(Word(word))
        for chunk in word_iter:
            actual_chunks.append(chunk)
        self.assertEqual(expected_chunks, actual_chunks)

    def testSimpleWord(self):
        self.doTestWord("גֱדֱדֲ", ["גֱ", "דֱ", "דֲ"])

    def testWordWithGeresh(self):
        self.doTestWord("גֱגֱ'דֱ", ["גֱ", "גֱ'", "דֱ"])
        self.doTestWord("גֱ'גֱגֱ", ["גֱ'", "גֱ", "גֱ"])
        self.doTestWord("דֱגֱגֱ'", ["דֱ", "גֱ", "גֱ'"])

    def testWordWithTwoNikudAndGeresh(self):
        self.doTestWord("גֱּ'גֱגֱ", ["גֱּ'", "גֱ", "גֱ"])
        self.doTestWord("גֱגֱגֱּ'", ["גֱ", "גֱ", "גֱּ'"])

    def testWordNoNikud(self):
        self.doTestWord("גֱגגֱ", ["גֱ", "ג", "גֱ"])
        self.doTestWord("גגֱגֱ", ["ג", "גֱ", "גֱ"])
        self.doTestWord("גֱגֱג", ["גֱ", "גֱ", "ג"])

