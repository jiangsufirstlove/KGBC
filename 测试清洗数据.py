import re

import jieba.posseg

from common import constant


def posseg(text):
    jieba.load_userdict(constant.DATA_DIR + "/MyDictionary.txt")
    # 清洗数据
    clean_text = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", text)
    result = []
    question_word, question_flag = [], []
    # 分词

    # text_cut = HanLP.Newsegment(clean_text)
    text_cut = jieba.posseg.cut(clean_text)
    # for item in text_cut:
    #     temp_word = f"{item.word}/{item.flag}"
    #     result.append(temp_word)
    #     word, flag = item.word, item.flag
    #     question_word.append(word)
    #     question_flag.append(flag)
    print(clean_text)


if __name__ == '__main__':
    posseg("今天,真是个好日子啊！")

