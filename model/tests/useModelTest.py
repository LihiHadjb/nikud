import unittest
from model.lstm.predict import get_prediction_for_text
from model.tests.utils import remove_nikud, remove_backslash_n
from model.encoding.process_text import TextProcessor
from model.lstm.train import do_train
from model.CharIdsSingleton import CharIdsSingleton


class useModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = "./resources/letters.xlsx"
        CharIdsSingleton(path)

    def setUp(self):
        self.processor = TextProcessor()

    def testTrain(self):
        path = "./resources/textToInputBasicNoEnglish.txt"
        all_inputs, all_labels = self.processor.prepare_file(path)
        do_train(all_inputs, all_labels)

    def testOverfit(self):
        text = "ואי ואחד ממכן יסאויהא באלבית"
        predictions = get_prediction_for_text(text)
        expected_predictoins = "וָאָיְ וָאחִד מֻמְכִּן יִסָאוִיהָא בִּאלְבֵּית"
        self.assertEqual(expected_predictoins, predictions)


