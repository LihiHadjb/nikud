import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from model.text_to_model_input import TextToModelInput

#torch.manual_seed(1)


class LSTMTagger(nn.Module):

    def __init__(self, embedding_dim, hidden_dim, config_path, bidirectional):
        super(LSTMTagger, self).__init__()
        self.text2input = TextToModelInput(config_path)
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim

        num_letters = self.text2input.get_num_letters()
        num_nikuds = self.text2input.get_num_nikuds()

        self.letter_embeddings = nn.Embedding(num_letters, embedding_dim)
        self.lstm = nn.LSTM(self.embedding_dim, self.hidden_dim, bidirectional=bidirectional)
        self.hidden2tag = nn.Linear(self.hidden_dim, num_nikuds)

    def forward(self, sentence):
        embeds = self.letter_embeddings(sentence)
        lstm_out, _ = self.lstm(embeds.view(len(sentence), 1, -1))
        tag_space = self.hidden2tag(lstm_out.view(len(sentence), -1))
        tag_scores = F.softmax(tag_space, dim=1)
        return tag_scores

embedding_dim = 50
hidden_dim = 50
config_path = "letters.xlsx"
bidirectional = False
num_epochs = 8000
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


# with torch.no_grad():
#     inputs = torch.tensor([20, 10, 30, 32], dtype=torch.long)
#     tag_scores = model(inputs)
#
#     # The sentence is "the dog ate the apple".  i,j corresponds to score for tag j
#     # for word i. The predicted tag is the maximum scoring tag.
#     # Here, we can see the predicted sequence below is 0 1 2 0 1
#     # since 0 is index of the maximum value of row 1,
#     # 1 is the index of maximum value of row 2, etc.
#     # Which is DET NOUN VERB DET NOUN, the correct sequence!
#     for i in [20, 10, 30, 32]:
#         print(tag_scores)