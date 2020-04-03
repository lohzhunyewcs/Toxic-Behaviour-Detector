import os

def get_word_lists():
    words_filter_dir = './words_filter/'
    word_files = os.listdir(words_filter_dir)
    words = set()
    for word_files in word_files:
        with open(words_filter_dir + word_files, 'r') as word_file:
            for line in word_file:
                line = line.strip()
                words.add(line)
    return words

def is_toxic(words, x_data):
    for word in words:
        if word in x_data:
            return True
    return False

def label_data():
    base_dir = 'combined_data/'
    file_lists = os.listdir(base_dir)

    base_output_dir = 'labelled_data/'

    header = 'text,is_toxic\n'
    start_index = 0
    header_written = False

    words = get_word_lists()

    for file in file_lists:
        with open(base_dir + file, 'r', encoding="utf8") as data_file:
            with open(base_output_dir + file, 'a', encoding="utf8") as output_file:
                if not header_written and start_index == 0:
                    output_file.write(header)
                    header_written = True
                for index, line in enumerate(data_file):
                    line = line.strip()
                    line = line.split(',')[-1]
                    if is_toxic(words, line):
                        output_file.write(f'{line.strip()},1\n')
                    else:
                        output_file.write(f'{line.strip()},0\n')

if __name__ == "__main__":
    label_data()
