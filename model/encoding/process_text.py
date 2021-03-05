from model.encoding.sentence_to_model_input import SentenceToModelInput
import re
import torch
from pathlib import Path


class TextProcessor():
    def __init__(self):
        self.sentence_processor = SentenceToModelInput()

    def prepare_text(self, text):
        #split_by = ['.', ',', ')', '(']

        all_inputs = []
        all_labels = []

        #TODO: these should come from the config file
        #consider spliting by illegal chars
        split_by = ['.', ',', '\n', '(', ')']
        pattern = '|'.join(map(re.escape, split_by))
        raw_sentences = re.split(pattern, text)

        for sent in raw_sentences:
            inputs, labels = self.sentence_processor.sentence_to_input_and_labels(sent)
            all_inputs.append(torch.tensor(inputs))
            all_labels.append(torch.tensor(labels))

        return all_inputs, all_labels


    def clean_illegal_chars(self, text):
        result = ""
        for c in text:
            if c != '\n':
                result += c
        return result


    def prepare_file(self, path):
        text = Path(path).read_text()
        text = self.clean_illegal_chars(text)
        return self.prepare_text(text)



