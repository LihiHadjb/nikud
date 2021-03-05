from model.encoding.process_text import TextProcessor
import unittest
from model.tests.utils import file2list
from model.CharIdsSingleton import CharIdsSingleton
from model.lstm.train import do_train


class ProcessTextTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = "../resources/letters.xlsx"
        CharIdsSingleton(path)

    def setUp(self):
        self.processor = TextProcessor()

    @unittest.skip("expected files are not updated")
    def testBasic(self):
        path = "../resources/textToInputBasic.txt"
        all_inputs, all_labels = self.processor.prepare_file(path)
        self.assertEqual(len(all_inputs), len(all_labels))
        self.assertEqual(25, len(all_inputs))

        exp_inputs = file2list("../resources/textToInputBasic.txt_all_inputs.txt")
        exp_labels = file2list("../resources/textToInputBasic.txt_all_labels.txt")

        self.assertEqual(exp_inputs, all_inputs)
        self.assertEqual(exp_labels, all_labels)



