import jieba
from pyhanlp import HanLP


text1 = "中共十一届三中全会的具体内容"
text2 = "2015年颁布了哪些文件"
text3 = "2014年召开了哪些会议"
text4 = "林彪简介"
text5 = "周恩来出生日期"
text6 = "邓小平参加了哪些事件"
text7 = "红军第二军团成立内容"
text8 = "中共中央和上海区委组织上海工人连续举行三次武装起义的具体时间"
text9 = "秋收起义的人物有哪些"
text10 = "陕甘宁边区参议会第一届第一次会议的内容"
text11 = "浙江萧山衙前村农民大会的内容"
text12 = "中国人民政治协商会议第一届全国委员会第一次会议的时间"
text13 = "《星星之火，可以燎原》的具体内容"
text14 = "中国共产党第一次全国代表大会的内容"





# CRFnewSegment = HanLP.newSegment("crf")
# words = CRFnewSegment.seg(text)
words = HanLP.segment(text1)
# for w in words:
#     print(w.word)
#     print(w.nature)

# words = jieba.cut(text)
# for w in words:
#     print(w)
words1 = HanLP.segment(text1)
# words2 = HanLP.segment(text2)
# words3 = HanLP.segment(text3)
# words4 = HanLP.segment(text4)
# words5 = HanLP.segment(text5)
# words6 = HanLP.segment(text6)
# words7 = HanLP.segment(text7)
# words8 = HanLP.segment(text8)
# words9 = HanLP.segment(text9)
# words10 = HanLP.segment(text10)
# words11 = HanLP.segment(text11)
# words12 = HanLP.segment(text12)
# words13 = HanLP.segment(text13)
# words14 = HanLP.segment(text14)


print(words1)
# print(words2)
# print(words3)
# print(words4)
# print(words5)
# print(words6)
# print(words7)
# print(words8)
# print(words9)
# print(words10)
# print(words11)
# print(words12)
# print(words13)
# print(words14)


