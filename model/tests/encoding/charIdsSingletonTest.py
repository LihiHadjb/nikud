from model.CharIdsSingleton import CharIdsSingleton
import unittest

#TODO: remove the word Singleton
class CharIdsSingletonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = "../resources/test_charIdsConfig.xlsx"
        CharIdsSingleton(path)

    def setUp(self):
        self.cid = CharIdsSingleton.get_instance()

    def testBasic(self):
        self.assertEqual(self.cid.get_num_nikuds(), 5)
        self.assertEqual(self.cid.get_num_letters(), 3)

    def testConversion(self):
        self.assertEqual(self.cid.get_letter_no_geresh_to_idx("ג"), 0)
        self.assertEqual(self.cid.get_letter_with_geresh_to_idx("ג"), 1)
        self.assertEqual(self.cid.get_letter_no_geresh_to_idx("ד"), 2)

        self.assertEqual(self.cid.get_idx_to_letter(0), "ג")
        self.assertEqual(self.cid.get_idx_to_letter(1), "ג'")
        self.assertEqual(self.cid.get_idx_to_letter(2), "ד")

        self.assertEqual(self.cid.get_idx_to_nikud(0), 'ֱ')
        self.assertEqual(self.cid.get_idx_to_nikud(1), 'ֲ')

        self.assertEqual(self.cid.get_nikud_to_idx('ֱ'), 0)
        self.assertEqual(self.cid.get_nikud_to_idx('ֲ'), 1)

    def testIdentifyCharType(self):
        self.assertTrue(self.cid.is_geresh("'"))
        self.assertFalse(self.cid.is_geresh(","))

        self.assertTrue(self.cid.is_letter("ג"))
        self.assertTrue(self.cid.is_letter("ג'"))
        self.assertTrue(self.cid.is_letter("ד"))
        self.assertFalse(self.cid.is_letter("ד'"))
        self.assertFalse(self.cid.is_letter("א"))

        self.assertTrue(self.cid.is_nikud("ֱ"))
        self.assertTrue(self.cid.is_nikud("ֲ"))
        self.assertFalse(self.cid.is_nikud("ֳ"))
        self.assertFalse(self.cid.is_nikud("ג"))
        self.assertFalse(self.cid.is_nikud("'"))

    def testDoubleNikud(self):
        self.assertEqual(self.cid.get_nikud_to_idx("ֱּ"), 2)
        self.assertTrue(self.cid.is_nikud("ֱּ"))
        self.assertEqual(self.cid.get_nikud_to_idx("ֱּ"), self.cid.get_nikud_to_idx("ֱּ"))
        self.assertEqual(self.cid.get_idx_to_nikud(2), "ֱּ")














