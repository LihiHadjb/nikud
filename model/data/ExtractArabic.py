from model.CharIdsSingleton import CharIdsSingleton
from model.encoding.chunk_to_input_label import ChunkToInputLabel
from model.encoding.word import Word
import docx
import os
from pathlib import Path

class ExtractArabicFromFiles:

    def __init__(self):
        self.cid = CharIdsSingleton.get_instance()
        self.cp = ChunkToInputLabel();

    def isArabicInHebrewLetters(self, word):
        ##TODO: replace with a word iterator
        letter_indices = Word(word).find_letter_indices_in_word();
        for j in range(len(letter_indices)):
            start_idx = letter_indices[j]
            end_idx = letter_indices[j+1] if j != len(letter_indices)-1 else len(word)
            try:
                idx, label = self.cp.chunk_to_input_label(word[start_idx:end_idx])
                if label != self.cid.get_no_nikud_idx():
                    return True
            except KeyError:
                return False

        return False


    def get_text_from_docx_file(self, path):
        document = docx.Document(path)
        docText = '\n'.join(paragraph.text for paragraph in document.paragraphs)
        return docText

    # def get_text_from_txt_file(self, path):
    #     with open(path, 'r') as file:
    #         text = file.read()
    #     return text

    def get_text(self, path):
        ext = os.path.splitext(path)[-1].lower()
        if ext == ".docx":
            text = self.get_text_from_docx_file(path)
        else:
            raise ValueError("This file's extension is not supported: " + path + "(supported extensions: .docx")
        return text

    def collect_from_file(self, path):
        file_name = Path(path).stem
        new_file_path = "C:/nikud/model/data/transcipts/" + file_name + "_arabic.txt"
        new_file = open(new_file_path, "w", encoding="utf8")
        text = self.get_text(path)
        for word in text.split():
            if self.isArabicInHebrewLetters(word):
                new_file.write(" " + word)
        new_file.close()

    def collect_from_dir(self, dir_path):
        directory = os.fsencode(dir_path)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            self.collect_from_file(dir_path + "/" + filename)


path = "../resources/config.xlsx"
CharIdsSingleton(path)
abuGal = ExtractArabicFromFiles()
abuGal.collect_from_dir("sources/חיאת עילתנא/docx")
