import torch
from model.resources.default_locations import DEFAULT_MODEL_PATH
from model.encoding.process_text import TextProcessor
from model.decoding.model_to_text import ModelInputToSentence
from model.CharIdsSingleton import CharIdsSingleton


def predict(inputs, model_path=DEFAULT_MODEL_PATH):
    model = torch.load(model_path)
    model.eval()
    with torch.no_grad():
        #inputs = torch.tensor([20, 10, 30, 32], dtype=torch.long)
        tag_scores = model(torch.tensor(inputs, dtype=torch.long))
        max_indices = torch.argmax(tag_scores, 1)
    return max_indices


def get_prediction_for_text(text):
    #TODO: think where to put this
    path = "C:/nikud/model/resources/config.xlsx"
    CharIdsSingleton(path)

    text_processor = TextProcessor()
    model2text = ModelInputToSentence()

    result = ""
    all_inputs, _ = text_processor.prepare_text(text)
    predictions = []
    for inputs in all_inputs:
        labels = predict(inputs)
        decoded =  model2text.input_and_labels_to_sentence(inputs, labels)
        result += decoded
    return result

