import os

word_cloud = {}
sentence_list = []
current_index  = 0
# Generate 
with open('combined_data/data.csv', 'r', encoding="utf8") as combined_file:
    for line in combined_file:
        line = line.strip()
        sentence_list.append(line)
        line = line.split()
        for word in line:
            if word not in word_cloud:
                word_cloud[word] = current_index
                current_index += 1

def is_toxic(sentence):
    return 'lingpin' in sentence

for sentence in sentence_list:
    is_toxic()