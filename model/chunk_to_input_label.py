from model.charIds import CharIdsConfig

SPACE = ' '


class ChunkToInputLabel:
    def __init__(self, config_path):
        self.cid = CharIdsConfig(config_path)

    def get_num_letters(self):
        return self.cid.get_num_letters()

    def get_num_nikuds(self):
        return self.cid.get_num_nikuds()

    def find_letter_indices_in_word(self, word):
        result = []
        for i, letter in enumerate(word):
            if self.cid.is_alphabet(letter):
                result.append(i)
        return result

    def get_nikud_in_chunk(self, chunk):
        result = ""
        for c in chunk:
            if self.cid.is_nikud(c):
                result += c
        return result

    def has_geresh(self, chunk):
        for c in chunk:
            if self.cid.is_geresh(c):
                return True
        return False

    def chunk_to_input_label(self, chunk):
        letter_ch = chunk[0]
        nikud = self.get_nikud_in_chunk(chunk)
        nikud_idx = self.cid.get_nikud_to_idx(nikud)
        if self.has_geresh(chunk):
            letter_idx = self.cid.get_letter_with_geresh_to_idx(letter_ch)
        else:
            letter_idx = self.cid.get_letter_no_geresh_to_idx(letter_ch)
        return letter_idx, nikud_idx

    def get_sep_chunk(self):
        return SPACE, self.cid.get_no_nikud_idx()


