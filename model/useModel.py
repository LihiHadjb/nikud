import torch
from model.default_locations import DEFAULT_MODEL_PATH
from model.default_locations import DEFAULT_CONFIG_PATH
from model.lstm import LSTMTagger
import torch.nn as nn
import torch.optim as optim
from model.process_text import TextProcessor
from model.decoding.model_to_text import ModelInputToSentence


def do_train():
    embedding_dim = 50
    hidden_dim = 50
    config_path = DEFAULT_CONFIG_PATH
    bidirectional = False
    num_epochs = 800

    model = LSTMTagger(embedding_dim, hidden_dim, config_path, bidirectional)
    training_data = [(torch.tensor([20, 10, 30, 32], dtype=torch.long), torch.tensor([8, 8, 0, 25], dtype=torch.long))]
    loss_function = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    for epoch in range(num_epochs):
        for sentence, tags in training_data:
            model.zero_grad()
            # sentence_in = prepare_sequence(sentence, word_to_ix)
            # targets = prepare_sequence(tags, tag_to_ix)
            tag_scores = model(sentence)
            loss = loss_function(tag_scores, tags)
            loss.backward()
            optimizer.step()
            print("Loss at epoch %d: %.3f" % (epoch, loss.item()))
    torch.save(model, DEFAULT_MODEL_PATH)


def predict(inputs, model_path=DEFAULT_MODEL_PATH):
    model = torch.load(model_path)
    model.eval()
    with torch.no_grad():
        #inputs = torch.tensor([20, 10, 30, 32], dtype=torch.long)
        tag_scores = model(torch.tensor(inputs, dtype=torch.long))
        max_indices = torch.argmax(tag_scores, 1)
    return max_indices.tolist()


def get_prediction_for_text(text):
    #TODO file name should not be hard-coded!
    text_processor = TextProcessor(DEFAULT_CONFIG_PATH)
    model2text = ModelInputToSentence(DEFAULT_CONFIG_PATH)

    result = ""
    all_inputs, _ = text_processor.prepare_text(text)
    predictions = []
    for inputs in all_inputs:
        labels = predict(inputs)
        result += model2text.input_and_labels_to_sentence(inputs, labels)
    return result

