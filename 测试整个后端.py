
from service.question_service import QuestionService

if __name__ == '__main__':
    getanswer = QuestionService()
    answer = getanswer.get_answer("1943年发生的历史事件")
    print(answer)
