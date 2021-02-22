import torch.nn as nn
import torch.nn.functional as F
from model.encoding.sentence_to_model_input import SentenceToModelInput

#torch.manual_seed(1)


class LSTMTagger(nn.Module):

    def __init__(self, embedding_dim, hidden_dim, config_path, bidirectional):
        super(LSTMTagger, self).__init__()
        self.text2input = SentenceToModelInput(config_path)
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
        tag_scores = F.log_softmax(tag_space, dim=1)
        return tag_scores




