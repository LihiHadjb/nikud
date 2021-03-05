from model.encoding.sentence_to_model_input import SentenceToModelInput
import unittest
from pathlib import Path
from model.decoding.model_to_text import ModelInputToSentence
from model.CharIdsSingleton import CharIdsSingleton
import torch


class Sentence2modelInputTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config_path = "../resources\letters.xlsx"
        CharIdsSingleton(config_path)

    def setUp(self):
        self.sentence2model = SentenceToModelInput()
        self.model2sentence = ModelInputToSentence()

    def testText2InputBasic(self):
        txt_path = "../resources/textToInputBasic.txt"
        txt = Path(txt_path).read_text()
        inputs, labels = self.sentence2model.sentence_to_input_and_labels(txt)

        self.assertEqual(len(labels), len(inputs))

        self.assertEqual([20, 10, 30, 32, 33, 30], inputs[:6])
        self.assertEqual([8, 8, 0, 25, 25, 8], labels[:6])

        self.assertEqual([14, 20, 29], inputs[-3:])
        self.assertEqual([0, 5, 25], labels[-3:])


    def testEncodeDecode(self):
        sent = "וָאָיְ וָאחִד מֻמְכִּן יִסָאוִיהָא בִּאלְבֵּית"
        inputs, labels = self.sentence2model.sentence_to_input_and_labels(sent)
        decoded = self.model2sentence.input_and_labels_to_sentence(torch.tensor(inputs), torch.tensor(labels))
        self.assertEqual(sent, decoded)





