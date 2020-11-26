import unittest
from model.useModel import get_prediction_for_text


class useModelTest(unittest.TestCase):

    def testSimple(self):
        text = "גגג"
        predictions = get_prediction_for_text(text)
        self.assertEqual("גָגָגָ", predictions)
    #
    # def test_overfit(self):
