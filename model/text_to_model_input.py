from model.chunk_to_input_label import ChunkToInputLabel


class TextToModelInput:
    def __init__(self, config_path):
        self.chunk_processor = ChunkToInputLabel(config_path)

    def get_num_letters(self):
        return self.chunk_processor.get_num_letters()

    def get_num_nikuds(self):
        return self.chunk_processor.get_num_nikuds()

    def verify_word(self, word, letter_indices):
        #if not 0 in letter_indices:
            #raise Exception("word " + word + " begins with a non letter character")
        return True

    def word_to_input_and_labels(self, word):
        inputs = []
        labels = []
        letter_indices = self.chunk_processor.find_letter_indices_in_word(word)
        self.verify_word(word, letter_indices)

        for j in range(len(letter_indices)):
            start_idx = letter_indices[j]
            end_idx = letter_indices[j+1] if j != len(letter_indices)-1 else len(word)
            idx, label = self.chunk_processor.chunk_to_input_label(word[start_idx:end_idx])
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
            sep, sep_label = self.chunk_processor.get_sep_chunk()
            inputs.append(sep)
            labels.append(sep_label)
            #inputs.append(SPACE)
            #labels.append(self.cid.get_no_nikud_idx())
        return inputs, labels

