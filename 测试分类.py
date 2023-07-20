from model.question_classify_model import QuestionClassify


def test_question_classify():
    question = "一二九运动的内容"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify1():
    question = "2009年颁布了哪些文件"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify2():
    question = "2012年召开了哪些会议"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify3():
    question = "邓小平简介"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify4():
    question = "周恩来出生日期"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify5():
    question = "叶剑英参加了哪些事件"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify6():
    question = "南昌起义的具体内容"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify7():
    question = "秋收起义的时间"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify8():
    question = "秋收起义的人物有哪些"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify9():
    question = "十一届三中全会的具体内容"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify10():
    question = "中共八大的地点"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify11():
    question = "遵义会议的时间"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify12():
    question = "《关于加强人民政协工作的意见》的时间"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


def test_question_classify13():
    question = "银河1计算机在长沙通过国家鉴定的具体内容"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")


if __name__ == '__main__':
    test_question_classify()
    # test_question_classify1()
    # test_question_classify2()
    # test_question_classify3()
    # test_question_classify4()
    # test_question_classify5()
    # test_question_classify6()
    # test_question_classify7()
    # test_question_classify8()
    # test_question_classify9()
    # test_question_classify10()
    # test_question_classify11()
    # test_question_classify12()
    # test_question_classify13()





