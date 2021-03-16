from model.CharIdsSingleton import CharIdsSingleton


class Word():
    def __init__(self, str):
        self.str = str;
        self.cid = CharIdsSingleton.get_instance()
        ##self.verify_word(str)
        self.letter_indices = self.find_letter_indices_in_word()

    def find_letter_indices_in_word(self):
        result = []
        for i, letter in enumerate(self.str):
            if self.cid.is_alphabet(letter):
                result.append(i)
        return result

    def verify_word(self):
        for c in self.str:
            if not (self.cid.is_nikud(c) or self.cid.is_geresh(c) or self.cid.is_alphabet(c)):
                return False
        return True

    def __iter__(self):
        self.curr_chunk_start = 0;
        return self

    def __next__(self):
        if self.curr_chunk_start < len(self.letter_indices):
            j = self.curr_chunk_start
        else:
            raise StopIteration

        start_idx = self.letter_indices[j]
        end_idx = self.letter_indices[j + 1] if j != len(self.letter_indices) - 1 else len(self.str)
        self.curr_chunk_start += 1
        return self.str[start_idx:end_idx]






