from common import nlp_util
from common.neo4j_util import Neo4jQuery


class QuestionTemplate:
    def __init__(self):
        self.q_template_dict = {
            0: self.get_year_event,
            1: self.get_year_file,
            2: self.get_year_meeting,
            3: self.get_person_info,
            4: self.get_person_birth,
            5: self.get_person_event,
            6: self.get_event_content,
            7: self.get_event_time,
            8: self.get_event_person,
            9: self.get_meeting_content,
            10: self.get_meeting_place,
            11: self.get_meeting_time,
            12: self.get_file_time,
            13: self.get_file_content
        }
        self.neo4j_conn = Neo4jQuery()
        self.raw_question = None
        self.question_flag = None
        self.question_word = None

    def get_question_answer(self, question, template_id):
        try:
            question = nlp_util.question_posseg(question)
            question_word, question_flag = [], []
            for one in question:
                # {item.word}/{item.flag}
                word, flag = one.split("/")
                question_word.append(str(word).strip())
                question_flag.append(str(flag).strip())
            self.question_word = question_word
            self.question_flag = question_flag
            self.raw_question = question
            # 根据问题模板来做对应的处理，获取答案
            answer = self.q_template_dict[template_id]()
            if answer == 0:
                answer = "sorry!数据内容不详，我会增进后续的学习！"
        except:
            answer = "sorry！有错误哦，请输入问题或者换个问题试试吧。"
        return answer

    def get_question_answer2(self, question, template_id):
        try:
            question = nlp_util.question_posseg2(question)
            question_word2, question_flag2 = [], []
            for one in question:
                # {item.word}/{item.nature}
                word, flag = one.split("/")
                question_word2.append(str(word).strip())
                question_flag2.append(str(flag).strip())
            self.question_word2 = question_word2
            self.question_flag2 = question_flag2
            self.raw_question = question
            # 根据问题模板来做对应的处理，获取答案
            answer = self.q_template_dict[template_id]()
            if answer == 0:
                answer = "sorry!数据内容不详，我会增进后续的学习！"
        except:
            answer = "sorry！有错误哦，请输入问题或者换个问题试试吧！"
        return answer

    # 获取年份
    def get_year(self):
        tag_index = self.question_flag.index("year")
        year = self.question_word[tag_index]
        return year

    # 获取事件
    def get_event(self):
        tag_index = self.question_flag.index("event")
        event = self.question_word[tag_index]
        return event

    # 获取文件
    def get_file(self):
        tag_index = self.question_flag2.index("file")
        file = self.question_word2[tag_index]
        return file

    # 获取会议
    def get_meeting(self):
        tag_index = self.question_flag.index("meeting")
        meeting = self.question_word[tag_index]
        return meeting

    # 获取人物
    def get_person(self):
        tag_index = self.question_flag.index("nr")
        person = self.question_word[tag_index]
        return person

    # 【0】某年发生了哪些事件
    def get_year_event(self):
        year = self.get_year()
        cql = f"match(e:event)-[r:发生于]->(y:year) where y.year_content='{year}' return e.event_name"
        answer = self.neo4j_conn.run(cql)
        # if answer is None:
        #     return 0
        if len(answer) == 0:
            return 0
        answer_set = set(answer)
        answer_list = list(answer_set)
        answer = "、".join(answer_list)
        final_answer = year + "年发生的重要事件有:" + str(answer) + "等"
        return final_answer

    # 【1】某年颁布了哪些文件
    def get_year_file(self):
        year = self.get_year()
        cql = f"match(f:file)-[r:颁布于]->(y:year) where y.year_content='{year}' return f.file_name"
        answer = self.neo4j_conn.run(cql)
        # if answer is None:
        #     return 0
        if len(answer) == 0:
            return 0
        answer_set = set(answer)
        answer_list = list(answer_set)
        answer = "、".join(answer_list)
        final_answer = year + "年颁布的重要文件有：" + str(answer) + "等"
        return final_answer

    # 【2】某年召开了哪些会议
    def get_year_meeting(self):
        year = self.get_year()
        cql = f"match(m:meeting)-[r:召开于]->(y:year) where y.year_content='{year}' return m.meeting_name"
        answer = self.neo4j_conn.run(cql)
        # if answer is None:
        #     return 0
        if len(answer) == 0:
            return 0
        answer_set = set(answer)
        answer_list = list(answer_set)
        answer = "、".join(answer_list)
        final_answer = year + "年召开的重要会议有：" + str(answer) + "等"
        return final_answer

    # 【3】人物简介
    def get_person_info(self):
        person = self.get_person()
        cql = f"match(p:person)-[]->() where p.person_name='{person}' return p.person_introduce"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = person + "的简介：" + str(answer)
        return final_answer

    # 【4】人物出生日期
    def get_person_birth(self):
        person = self.get_person()
        cql = f"match(p:person)-[]->() where p.person_name='{person}' return p.person_date"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = person + "的出生年月：" + str(answer)
        return final_answer

    # 【5】人物参加了哪些事件
    def get_person_event(self):
        person = self.get_person()
        cql = f"match(p:person)-[r:参与了]->(e:event) where p.person_name='{person}'return e.event_name"
        print(cql)
        answer = self.neo4j_conn.run(cql)
        # if answer is None:
        #     return 0
        if len(answer) == 0:
            return 0
        answer_set = set(answer)
        answer_list = list(answer_set)
        answer = "、".join(answer_list)
        final_answer = person + "参加的重要事件有：" + str(answer) + "等"
        return final_answer

    # 【6】事件的内容
    def get_event_content(self):
        event = self.get_event()
        cql = f"match(e:event)-[]->() where e.event_name='{event}' return e.event_content"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = event + "的内容：" + str(answer)
        return final_answer

    # 【7】事件的具体时间
    def get_event_time(self):
        event = self.get_event()
        cql = f"match(e:event)-[]->() where e.event_name='{event}' return e.event_date"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = event + "的具体时间：" + str(answer)
        return final_answer

    # 【8】事件的人物
    def get_event_person(self):
        event = self.get_event()
        cql = f"match(p:person)-[r:参与了]->(e:event) where e.event_name='{event}'return p.person_name"
        print(cql)
        answer = self.neo4j_conn.run(cql)
        # if answer is None:
        #     return 0
        if len(answer) == 0:
            return 0
        answer_set = set(answer)
        answer_list = list(answer_set)
        answer = "、".join(answer_list)
        final_answer = event + "重点人物有：" + str(answer)
        return final_answer

    # 【9】会议的具体内容
    def get_meeting_content(self):
        meeting = self.get_meeting()
        cql = f"match(m:meeting)-[]->() where m.meeting_name='{meeting}' return m.meeting_content"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = meeting + "的具体内容：" + str(answer)
        return final_answer

    # 【10】会议的地点
    def get_meeting_place(self):
        meeting = self.get_meeting()
        cql = f"match(m:meeting)-[]->() where m.meeting_name='{meeting}' return m.meeting_place"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = meeting + "召开的地点：" + str(answer)
        return final_answer

    # 【11】会议的具体时间
    def get_meeting_time(self):
        meeting = self.get_meeting()
        cql = f"match(m:meeting)-[]->() where m.meeting_name='{meeting}' return m.meeting_date"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = meeting + "的具体内容：" + str(answer)
        return final_answer

    # 【12】文件的颁布时间
    def get_file_time(self):
        file = self.get_file()
        cql = f"match(f:file)-[]->() where f.file_name='{file}' return f.file_date"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = file + "颁布的时间：" + str(answer)
        return final_answer

    # 【13】文件的内容
    def get_file_content(self):
        file = self.get_file()
        cql = f"match(f:file)-[]->() where f.file_name='{file}' return f.file_content"
        print(cql)
        answer = self.neo4j_conn.run(cql)[0]
        if answer is None:
            return 0
        final_answer = file + "的内容：" + str(answer)
        return final_answer
