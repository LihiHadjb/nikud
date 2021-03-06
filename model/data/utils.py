from model.CharIdsSingleton import CharIdsSingleton
from model.encoding.process_text import TextProcessor
from model.lstm.train import do_train

#dir_to_one_file:
    #for %f in (*.txt) do type "%f" >> output.txt
#dir_to_one_file("C:/nikud/model/data/transcipts")


#train!!

path = "../resources/config.xlsx"
CharIdsSingleton(path)

data_path = "train.docx"
processor = TextProcessor()

all_inputs, all_labels = processor.prepare_file(data_path)
do_train(all_inputs, all_labels)