import langdetect

with open('data/dota2_chat_messages.csv', 'r', encoding="utf8") as file:
    with open('data/dota2_en_chat_messages.csv', 'a', encoding="utf8") as output_file:
        for index, line in enumerate(file):
            if index < 2119000:
                continue
            if index == 4000000:
                break
            if index % 1000 == 0:
                print(index)
            try:
                if langdetect.detect(line) == 'en':
                    output_file.write(line)
            except Exception:
                pass    