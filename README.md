# Toxic-Behaviour-Detector
Modern Video Games are plagued with a toxic community and oftenly enough they go unpunished which only cultivates this issue. To counteract this, we have made a R-NN that detects this kind of behaviour. We processed a dataset for a game called Dota 2 which was available on Kaggle and then trained a R-NN on it.

Limitations:
1) Provoked people may generally be otherwise friendly. Unfortunately due to the limitation of the chat data, we were unable to process if people were truly provoked prior to their toxic behaviour
2) The large size of the dataset led us to just using a simple toxic word/phrase cloud that did the labeling.
3) Sarcasms may also misinterpreted.
4) Due to the need of zero padding and limitations of our RAM, we have only used a maximum padding of length 10, so sequences of length more than 10 are split into multiples of 10.

Contributors:
1) Loh Zhun Yew
2) Goh Wei Kang
3) Tuang Ling Pin

TODO:
1) Use State-of-the-art classifiers such as BERT and ERNIE to classifies
2) Try attention models
3) Implement the models in TensorFlow(Almost done, to be uploaded soon)
4) Use Word2Vec Embeddings trained on game chats
5) Fix PyTorch models
6) Implement PyTorch-Lightning model and train with TPUs
