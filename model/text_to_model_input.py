from model.charIds import CharIdsConfig

SPACE = ' '


class TextToModelInput:
    def __init__(self, config_path):
        self.cid = CharIdsConfig(config_path)

    def verify_word(self, word, letter_indices):
        #if not 0 in letter_indices:
            #raise Exception("word " + word + " begins with a non letter character")
        return True

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

    def word_chunk_to_input_label(self, chunk):
        letter_ch = chunk[0]
        nikud = self.get_nikud_in_chunk(chunk)
        nikud_idx = self.cid.get_nikud_to_idx(nikud)
        if self.has_geresh(chunk):
            letter_idx = self.cid.get_letter_with_geresh_to_idx(letter_ch)
        else:
            letter_idx = self.cid.get_letter_no_geresh_to_idx(letter_ch)
        return letter_idx, nikud_idx

    def word_to_input_and_labels(self, word):
        inputs = []
        labels = []
        letter_indices = self.find_letter_indices_in_word(word)
        self.verify_word(word, letter_indices)

        for j in range(len(letter_indices)):
            start_idx = letter_indices[j]
            end_idx = letter_indices[j+1] if j != len(letter_indices)-1 else len(word)
            idx, label = self.word_chunk_to_input_label(word[start_idx:end_idx])
            inputs.append(idx)
            labels.append(label)
        return inputs, labels

    def text_to_input_and_labels(self, text):
        inputs = []
        labels = []
        for word in text.split():
            word_inputs, word_labels = self.word_to_input_and_labels(word)
            inputs.extend(word_inputs)
            labels.extend(word_labels)
            inputs.append(SPACE)
            labels.append(self.cid.get_no_nikud_idx())
        return inputs, labels

