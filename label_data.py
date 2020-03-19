import langdetect
from multiprocessing import Pool

def filterEnglish(i):
    with open('data/dota2_chat_messages.csv', 'r', encoding="utf8") as file:
        arr = []
        for index, line in enumerate(file):
            if index < i[0]:
                continue
            if index == i[1]:
                break
            if index % 1000 == 0:
                print(index)
            try:
                if langdetect.detect(line) == 'en':
                    arr.append(line)
            except Exception:
                pass
        return arr

def calc(start, end, np):
    split = (end - start) // np
    arr = []
    for i in range(np):
        arr.append([start+split*i, start+split*(i+1)])
    return arr

if __name__ == '__main__':
    # set these variables
    start = 50000
    end = 60000
    np = 4
    with Pool(processes=np) as pool:
        data = pool.map(filterEnglish, calc(start, end, np))
    with open('data/dota2_en_chat_messages.csv', 'a', encoding="utf8") as output_file:
        for arr in data:
            for line in arr:
                output_file.write(line)