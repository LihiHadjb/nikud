from model.text_to_model_input import TextToModelInput
import unittest
from pathlib import Path


class Word2modelInputTest(unittest.TestCase):

    def setUp(self):
        path = "test_charIdsConfig.xlsx"
        self.text2model = TextToModelInput(path)

    def doTestWord(self, word, expected_input, expected_labels):
        actual_input, actual_labels = self.text2model.word_to_input_and_labels(word)
        self.assertEqual(expected_input, actual_input)
        self.assertEqual(expected_labels, actual_labels)

    def testSimpleWord(self):
        self.doTestWord("גֱדֱדֲ", [0, 2, 2], [0, 0, 1])

    def testWordWithGeresh(self):
        self.doTestWord("גֱגֱ'דֱ", [0, 1, 2], [0, 0, 0])
        self.doTestWord("גֱ'גֱגֱ", [1, 0, 0], [0, 0, 0])
        self.doTestWord("דֱגֱגֱ'", [2, 0, 1], [0, 0, 0])

    def testWordWithTwoNikud(self):
        self.doTestWord("ג'ֱג'ֱג'ֱ", [1, 1, 1], [0, 0, 0])
        self.doTestWord("גֱּגֱגֱ", [0, 0, 0], [2, 0, 0])
        self.doTestWord("גֱגֱגֱּ", [0, 0, 0], [0, 0, 2])

    def testWordWithTwoNikudAndGeresh(self):
        self.doTestWord("גֱּ'גֱגֱ", [1, 0, 0], [2, 0, 0])
        self.doTestWord("גֱגֱגֱּ'", [0, 0, 1], [0, 0, 2])

    def testWordNoNikud(self):
        self.doTestWord("גֱגגֱ", [0, 0, 0], [0, 4, 0])
        self.doTestWord("גגֱגֱ", [0, 0, 0], [4, 0, 0])
        self.doTestWord("גֱגֱג", [0, 0, 0], [0, 0, 4])

class Text2modelInputTest(unittest.TestCase):

    def setUp(self):
        config_path = "..\letters.xlsx"
        self.text2model = TextToModelInput(config_path)

    def testText2InputBasic(self):
        txt_path = "textToInputBasic.txt"
        txt = Path(txt_path).read_text()
        inputs, labels = self.text2model.text_to_input_and_labels(txt)

        print(inputs[-5:])
        print(labels[-5:])
        self.assertEqual(len(labels), len(inputs))

        self.assertEqual(inputs[:6], [20, 10, 30, 32, ' ', 30])
        self.assertEqual(labels[:6], [8, 8, 0, 25, 25, 8])

        self.assertEqual(inputs[-4:], [14, 20, 29, ' '])
        self.assertEqual(labels[-4:], [0, 5, 25, 25])




