import pickle
# import torch
# from summarizer import Summarizer,TransformerSummarizer

# torch.load('f',map_location=torch.device('cpu'))

# device=torch.device("cpu")

def bert_summarizer(input_text, min_sentences):
  # torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  with open('bert_model_stored', 'rb') as f:
    bm = pickle.load(f)
  bert_summary = ''.join(bm(input_text, num_sentences = min_sentences))
  return bert_summary

# print("Please enter the keyword: ")
# input_keyword = input()
# print("Please enter the minimum number of sentences for summary: ")
# min_sentences = int(input())
# output = bert_summarizer(input_keyword,min_sentences)
# print("\n\n"+output)