import unittest
from model.CharIdsSingleton import CharIdsSingleton
from model.encoding.word import Word
from model.encoding.sentence_to_model_input import SentenceToModelInput



class WordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = "../resources/test_charIdsConfig.xlsx"
        CharIdsSingleton(path)

    def setUp(self):
        self.cid = CharIdsSingleton.get_instance()
        self.sentence2model = SentenceToModelInput()


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





    def doTestWordToInputsLabels(self, word, expected_input, expected_labels):
        actual_input, actual_labels = self.sentence2model.word_to_input_and_labels(word)
        self.assertEqual(expected_input, actual_input)
        self.assertEqual(expected_labels, actual_labels)

    def testSimpleWordToInputsLabels(self):
        self.doTestWordToInputsLabels("גֱדֱדֲ", [0, 2, 2], [0, 0, 1])

    def testWordWithGereshToInputsLabels(self):
        self.doTestWordToInputsLabels("גֱגֱ'דֱ", [0, 1, 2], [0, 0, 0])
        self.doTestWordToInputsLabels("גֱ'גֱגֱ", [1, 0, 0], [0, 0, 0])
        self.doTestWordToInputsLabels("דֱגֱגֱ'", [2, 0, 1], [0, 0, 0])

    def testWordWithTwoNikudToInputsLabels(self):
        self.doTestWordToInputsLabels("ג'ֱג'ֱג'ֱ", [1, 1, 1], [0, 0, 0])
        self.doTestWordToInputsLabels("גֱּגֱגֱ", [0, 0, 0], [2, 0, 0])
        self.doTestWordToInputsLabels("גֱגֱגֱּ", [0, 0, 0], [0, 0, 2])

    def testWordWithTwoNikudAndGereshToInputsLabels(self):
        self.doTestWordToInputsLabels("גֱּ'גֱגֱ", [1, 0, 0], [2, 0, 0])
        self.doTestWordToInputsLabels("גֱגֱגֱּ'", [0, 0, 1], [0, 0, 2])

    def testWordNoNikudToInputsLabels(self):
        self.doTestWordToInputsLabels("גֱגגֱ", [0, 0, 0], [0, 4, 0])
        self.doTestWordToInputsLabels("גגֱגֱ", [0, 0, 0], [4, 0, 0])
        self.doTestWordToInputsLabels("גֱגֱג", [0, 0, 0], [0, 0, 4])