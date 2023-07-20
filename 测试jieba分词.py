import jieba
import jieba.posseg as pseg

from common import constant

if __name__ == '__main__':
    jieba.load_userdict(constant.DATA_DIR + "/MyDictionary.txt")
    words = pseg.cut("林彪等人外逃叛国的具体内容")
    print(words)
    for w in words:
        print(w.word,w.flag)
        # print(w.flag)
