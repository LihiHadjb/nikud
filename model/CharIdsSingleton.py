import pandas as pd

SEPARATOR = ''


class CharIdsSingleton:
    __instance = None

    @staticmethod
    def get_instance():
        if CharIdsSingleton.__instance is None:
            raise Exception("Not initialized!")
        return CharIdsSingleton.__instance

    def __init__(self, path):
        if CharIdsSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CharIdsSingleton.__instance = self
            idx_to_letter, letter_to_idx = self.dict_from_excel(path, "letters")
            idx_to_nikud, nikud_to_idx = self.dict_from_excel(path, "nikud")
            self.path = path
            self.idx_to_letter = idx_to_letter
            self.letter_to_idx = letter_to_idx
            self.idx_to_nikud = idx_to_nikud
            self.nikud_to_idx = nikud_to_idx
            self.GERESH = '\''
            self.NO_NIKUD = "NONE"
            self.idx_to_has_geresh = {i: len(letter) == 2 for i, letter in enumerate(letter_to_idx.keys())}
            self.SPACE_IDX = (len(idx_to_letter) - 1) + 1

    def dict_from_excel(self, xls_path, col):
       xls = pd.ExcelFile(xls_path)
       df = xls.parse()
       col_df = df[col].dropna()
       idx_to_char = col_df.to_dict()
       char_to_idx = {v: k for k, v in idx_to_char.items()}
       return idx_to_char, char_to_idx

    def is_nikud(self, nikud):
       nik_str = SEPARATOR.join(sorted(nikud))
       return nik_str in self.nikud_to_idx.keys()

    def is_geresh(self, ch):
       return ch == self.GERESH

    def is_letter(self, ch):
       return ch in self.letter_to_idx.keys()

    def is_alphabet(self, ch):
       return 'א' <= ch <= 'ת'

    def get_letter_with_geresh_to_idx(self, ch):
       with_geresh = ch + self.GERESH
       return self.letter_to_idx[with_geresh]

    def get_letter_no_geresh_to_idx(self, ch):
       return self.letter_to_idx[ch]

    def get_idx_to_letter(self, idx):
       return self.idx_to_letter[idx]

    def get_nikud_to_idx(self, nikud):
       nik_str = SEPARATOR.join(sorted(nikud))
       if nik_str != '':
           return self.nikud_to_idx[nik_str]
       else:
           return self.nikud_to_idx[self.NO_NIKUD]

    def get_idx_to_nikud(self, idx):
       return self.idx_to_nikud[idx]

    def get_no_nikud_idx(self):
       return self.nikud_to_idx[self.NO_NIKUD]

    def get_num_letters(self):
       return len(self.letter_to_idx.keys())

    def get_num_nikuds(self):
       return len(self.nikud_to_idx.keys())

    def get_idx_to_has_geresh(self, idx):
       return self.idx_to_has_geresh[idx]

    def get_space_idx(self):
       return self.SPACE_IDX

