from model.encoding.chunk_to_input_label import ChunkToInputLabel
from model.encoding.Word import Word


class SentenceToModelInput:
    def __init__(self):
        self.chunk_processor = ChunkToInputLabel()

    def get_num_letters(self):
        return self.chunk_processor.get_num_letters() + 1

    def get_num_nikuds(self):
        return self.chunk_processor.get_num_nikuds()

    def word_to_input_and_labels(self, word):
        inputs = []
        labels = []
        word_iter = iter(Word(word))

        for chunk in word_iter:
            idx, label = self.chunk_processor.chunk_to_input_label(chunk)
            inputs.append(idx)
            labels.append(label)
        return inputs, labels

    def sentence_to_input_and_labels(self, sentence):
        inputs = []
        labels = []
        for word in sentence.split():
            word_inputs, word_labels = self.word_to_input_and_labels(word)
            inputs.extend(word_inputs)
            labels.extend(word_labels)
            sep, sep_label = self.chunk_processor.get_sep_chunk()
            inputs.append(sep)
            labels.append(sep_label)

        #remove the last space
        inputs = inputs[:-1]
        labels = labels[:-1]
        return inputs, labels
