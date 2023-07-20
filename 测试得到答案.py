from model import question_template


def test_get_answer1():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("2005年发生了哪些事件", 0)
    print(answer)


def test_get_answer2():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("2005年颁布了哪些文件", 1)
    print(answer)


def test_get_answer3():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("2009年召开了哪些会议", 2)
    print(answer)


def test_get_answer4():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("毛泽东简介", 3)
    print(answer)


def test_get_answer5():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("林彪出生日期", 4)
    print(answer)


def test_get_answer6():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("毛泽东参加了哪些事件", 5)
    print(answer)


def test_get_answer7():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("秋收起义里面用到了什么武器", 6)
    print(answer)


def test_get_answer8():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("南昌起义时间", 7)
    print(answer)


def test_get_answer9():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("广州起义人物", 8)
    print(answer)


def test_get_answer10():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("中共七大的内容", 9)
    print(answer)


def test_get_answer11():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("中共八大的地点", 10)
    print(answer)


def test_get_answer12():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("中共七大的时间", 11)
    print(answer)


def test_get_answer13():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer2("《星星之火，可以燎原》的具体内容", 13)
    print(answer)


def test_get_answer14():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer2("《星星之火，可以燎原》的颁布时间", 12)
    print(answer)


if __name__ == '__main__':
    # test_get_answer1()
    # test_get_answer2()
    # test_get_answer3()
    # test_get_answer4()
    # test_get_answer5()
    # test_get_answer6()
    test_get_answer7()
    # test_get_answer8()
    # test_get_answer9()
    # test_get_answer10()
    # test_get_answer11()
    # test_get_answer12()
    # test_get_answer13()
    # test_get_answer14()
