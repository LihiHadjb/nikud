from model.encoding.charIds import CharIdsConfig


class ModelInputToSentence:
    def __init__(self, config_path):
        self.cid = CharIdsConfig(config_path)

    def chunk_from_input_label(self, input_idx, label_idx):
        label_char = self.cid.get_idx_to_nikud(label_idx)

        try:
            input_char = self.cid.get_idx_to_letter(input_idx)
            if label_char != "NONE":
                if self.cid.get_idx_to_has_geresh(input_idx):
                    result = input_char[0] + label_char + self.cid.GERESH
                else:
                    result = input_char + label_char
            else:
                result = input_char


        except KeyError:
            input_char = input_idx
            result = input_char
        return result



    def input_and_labels_to_sentence(self, inputs, labels):
        result = ""
        for input_idx, label_idx in zip(inputs, labels):
            chunk = self.chunk_from_input_label(input_idx, label_idx)
            result += chunk
        return result
