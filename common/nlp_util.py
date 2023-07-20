import re
import jieba.posseg

from common import constant

from pyhanlp import HanLP


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
    return text_cut


def question_posseg(question):
    jieba.load_userdict(constant.DATA_DIR + "/MyDictionary.txt")
    clean_question = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", question)
    question_seged = jieba.posseg.cut(str(clean_question))
    # question_seged = HanLP.segment(str(clean_question))
    result = []
    question_word, question_flag = [], []
    for w in question_seged:
        temp_word = f"{w.word}/{w.flag}"
        result.append(temp_word)
        # 预处理问题
        word, flag = w.word, w.flag
        question_word.append(str(word).strip())
        question_flag.append(str(flag).strip())
    assert len(question_flag) == len(question_word)
    return result


def question_posseg2(question):
    # jieba.load_userdict(constant.DATA_DIR + "/MyDictionary.txt")
    # clean_question = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", question)
    # question_seged = jieba.posseg.cut(str(clean_question))
    question_seged = HanLP.segment(str(question))
    result = []
    question_word, question_flag = [], []
    for w in question_seged:
        temp_word = f"{w.word}/{w.nature}"
        result.append(temp_word)
        # 预处理问题
        word, flag = w.word, w.nature
        question_word.append(str(word).strip())
        question_flag.append(str(flag).strip())
    assert len(question_flag) == len(question_word)
    return result
