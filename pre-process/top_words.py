import collections
import re
import matplotlib.pyplot as plt


def top_words(data, stopwords = [], file_name = "chart", to_print = 20):
    wordcount = collections.defaultdict(int)
    for line in data:
        for word in str(line).lower().split():
            if word not in stopwords:
                wordcount[word] += 1
          
    mc = sorted(wordcount.items(), key=lambda k_v: k_v[1], reverse=True)[:to_print]
    for word, count in mc:
        print(word, ":", count)

    mc = dict(mc)
    names = list(mc.keys())
    values = list(mc.values())

    plt.barh(range(len(mc)),values,tick_label=names)
    plt.savefig(file_name + ".png")
    plt.show()

def two_top_words(data1, data2, stopwords = [], file_name = "chart", to_print = 20):
    wordcount = collections.defaultdict(int)
    for line in data1:
        for word in str(line).lower().split():
            if word not in stopwords:
                wordcount[word] += 1
          
    mc = sorted(wordcount.items(), key=lambda k_v: k_v[1], reverse=True)[:to_print]
    for word, count in mc:
        print(word, ":", count)

    mc = dict(mc)
    names = list(mc.keys())
    values = list(mc.values())
 
    plt.barh(range(len(mc)),values,tick_label=names)
    plt.savefig(file_name + "_1.png")
    plt.show()


    wordcount = collections.defaultdict(int)
    for line in data1:
        for word in str(line).lower().split():
            if word not in stopwords:
                wordcount[word] += 1
          
    mc = sorted(wordcount.items(), key=lambda k_v: k_v[1], reverse=True)[:to_print]
    for word, count in mc:
        print(word, ":", count)

    mc = dict(mc)
    names = list(mc.keys())
    values = list(mc.values())
    # plt.subplot(1,1,2)
    plt.barh(range(len(mc)),values,tick_label=names)
    plt.savefig(file_name + "_2.png")
    plt.show()