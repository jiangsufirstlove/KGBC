from flask import Flask, render_template
from flask import request

from service import question_service

app = Flask("基于百年党史知识图谱的智能问答系统")
question_serv = question_service.QuestionService()


def start_server():
    app.run()


@app.route("/")
def index():

    return render_template("qa_robot.html")


@app.route("/get_answer", methods=["GET", "POST"])
def get_answer():
    question = request.args.get('question')
    answer = question_serv.get_answer(question)
    return answer


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10200)
