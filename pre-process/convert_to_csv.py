import pandas as pd
import pre_process
from sklearn.model_selection import train_test_split
import crf_tokenizer

SELL = '__label__post_ban_hang'
NON_SELL = '__label__post_khong_ban'
sell_ls = []
non_sell_ls = []

#read data line by line and split 
lines = [line.rstrip('\n') for line in open('../data/data_original.txt')]

# for l in lines:
#     line = l.split(" ", 1)
#     if line[0] == SELL:
#         sell_ls.append(pre_process.pre_process(line[1]))
#     elif line[0] == NON_SELL:
#         non_sell_ls.append(pre_process.pre_process(line[1]))


for l in lines:
    line = l.split(" ", 1)
    if line[0] == SELL:
        sell_ls.append(line[1])
    elif line[0] == NON_SELL:
        non_sell_ls.append(line[1])

pr = lambda x: pre_process.pre_process(x)
sell_ls = [pr(x) for x in sell_ls]
non_sell_ls = [pr(x) for x in non_sell_ls]

#write to file
df = pd.DataFrame(sell_ls)
df.to_csv("../data/sell.csv", header=False, index=False)


df = pd.DataFrame(non_sell_ls)
df.to_csv("../data/nonsell.csv", header=False, index=False)