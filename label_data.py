import os

base_dir = 'processed_data/'
file_lists = os.listdir(base_dir)

base_output_dir = 'labelled_data'

header = 'text,is_toxic'
start_index = 0
header_written = False

for file in file_lists:
    with open(base_dir + file, 'r') as data_file:
        with open(base_output_dir + file, 'w') as output_file:
            if not header_written and start_index == 0:
                output_file.write(header)
                header_written = True
            for index, line in enumerate(data_file):
                if index < start_index:
                    continue
                line = line.strip()
                line = line.split(',')
                text = line[-1]
                is_toxic = '-1'
                while is_toxic != '0' or is_toxic != '1':
                    is_toxic = input(f'Index{index}: Is the phrase "{text}" toxic? Press 1 if yes, 0 if not')
                output_file.write(f'{text},{is_toxic}\n')