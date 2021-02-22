import unittest
from model.lstm.predict import get_prediction_for_text
from model.tests.utils import remove_nikud, remove_backslash_n
from model.encoding.process_text import TextProcessor
from model.resources.default_locations import DEFAULT_CONFIG_PATH
from model.lstm.train import do_train


class useModelTest(unittest.TestCase):

    def testSimple(self):
        text = "גגג"
        predictions = get_prediction_for_text(text)
        self.assertEqual("גָגָגָ", predictions)

    def testOverfit(self):
        text2input = TextProcessor(DEFAULT_CONFIG_PATH)
        with open('resources/textToInputBasic.txt', 'r') as file:
            text = file.read()
        text_no_nikud = remove_nikud(text)
        text_no_nikud = remove_backslash_n(text)
        train_inputs, train_labels = text2input.prepare_text(text_no_nikud)
        do_train(train_inputs, train_labels)


