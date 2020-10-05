from model.charIds import CharIdsConfig
import unittest


class CharIdsTest(unittest.TestCase):

    def setUp(self):
        path = "test_charIdsConfig.xlsx"
        self.cid = CharIdsConfig(path)


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












