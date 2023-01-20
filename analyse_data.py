import pandas as pd
from tqdm import tqdm

# get the number of lines of a file
def get_num_lines(file):
    with open(file, encoding='utf-8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

file = './data/train.txt'

# csv_strucuture: BERT format
# sentence id, word, tag
# Create a new dataframe with the columns sentence id, word tag
df = pd.DataFrame(columns=['sentence_id', 'word', 'tag'])

label_splitter = ' _ _ '

# split ny newline
cnt = 0
log = True
log = False
small = True
num_lines = get_num_lines(file)
with open(file, encoding='utf-8') as f:
    # split by newline
    str = ""
    sentence_id = 0

    for line in tqdm(f, total=num_lines):
        # split by space
        # print(line)
        if line == "\n":
            if log: print("New line")
            sentence_id += 1
        else:
            word, tag = line.strip().split(label_splitter)
            if log: print("Not new line:", word, tag)
            df = df.append({'sentence_id': sentence_id, 'word': word, 'tag': tag}, ignore_index=True)

        cnt += 1
        if cnt == 1000 and small: break

# save the dataframe to a csv file named train bert.csv
if small: df.to_csv('./data/train_generic_small.csv', index=False)
else: df.to_csv('./data/train_generic.csv', index=False)

print(df.head(20))