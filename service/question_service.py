from model import question_classify_model, question_template


class QuestionService:

    def __init__(self):
        self.classify_model = question_classify_model.QuestionClassify()
        self.question_template = question_template.QuestionTemplate()

    def get_answer(self, question):
        # 通过分类器获取分类
        question_category = self.classify_model.predict(question)
        # 根据分类获取模板，查询得到答案
        try:
            if question_category in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                answer = self.question_template.get_question_answer(question, question_category)
            else:
                answer = self.question_template.get_question_answer2(question, question_category)
        except BaseException as e:
            answer = "sorry!这个问题问倒我了，我会增进学习提供更好的服务。"
        return answer


question_service_instance = QuestionService()
