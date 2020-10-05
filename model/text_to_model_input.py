from model.charIds import CharIdsConfig

class TextToModelInput:
    def __init__(self, config_path):
        self.cid = CharIdsConfig(config_path)


    def has_geresh(self, word, idx):
        if idx != len(word) - 1:
            return self.cid.is_geresh(word[idx + 1])
        return False

    def word_to_input_and_labels(self, word):
        inputs = []
        labels = []
        if not self.cid.is_letter(word[0]):
            raise Exception("word " + word + "begins with a non letter character")

        i = 0
        while (i < len(word)):
            if is_nikud(word[i]):
                labels.append(word[i])
            elif has_geresh(word[i]):
                inputs.append(with_geresh_to_idx(word[i]))
                i += 1
            else:
                inputs.append(letter_to_idx[word[i]])
            i += 1
        return inputs, labels

    def text_to_input_and_labels(text):
        inputs = []
        labels = []
        for word in text:
            i = 0
            while i < len(word):
                if is_nikud_char(word[i]):








