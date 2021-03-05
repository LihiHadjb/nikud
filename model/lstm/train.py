import torch
from model.resources.default_locations import DEFAULT_MODEL_PATH
from model.lstm.lstm import LSTMTagger
import torch.nn as nn
import torch.optim as optim


def do_train(training_inputs, training_labels):
    embedding_dim = 50
    hidden_dim = 50
    bidirectional = False
    num_epochs = 800

    model = LSTMTagger(embedding_dim, hidden_dim, bidirectional)
    #training_data = [(torch.tensor([20, 10, 30, 32], dtype=torch.long), torch.tensor([8, 8, 0, 25], dtype=torch.long))]
    loss_function = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)
    model.train()

    for epoch in range(num_epochs):
        for sentence, tags in zip(training_inputs, training_labels):
            model.zero_grad()
            # sentence_in = prepare_sequence(sentence, word_to_ix)
            # targets = prepare_sequence(tags, tag_to_ix)
            tag_scores = model(sentence)
            loss = loss_function(tag_scores, tags)
            loss.backward()
            optimizer.step()
            print("Loss at epoch %d: %.3f" % (epoch, loss.item()))
    torch.save(model, DEFAULT_MODEL_PATH)


