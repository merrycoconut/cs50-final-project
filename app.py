from cs50 import SQL
from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///instance/questionbank.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/question", methods=["GET", "POST"])
def question():

    # Get a dic of questions
    questions = db.execute("SELECT id,question_text FROM questions")

    # Get a list of answer_text
    selections = db.execute("SELECT id,question_id,answer_text FROM answers")

    if request.method == "GET":
        # Pass the questions and answers to html
        return render_template("question.html", questions=questions, selections=selections)

@app.route("/result", methods=["GET", "POST"])
def result():

    if request.method == "POST":
        questions = db.execute("SELECT id,question_text FROM questions")
        selections = db.execute("SELECT id,question_id,answer_text FROM answers")

        # Get user's answers.
        answerIDs = [int(value) for key, value in request.form.items()]

        # Apology if the user didn't finish the questions.
        if len(answerIDs) < 7:
            apology = "请您确认完成所有题目。"
            return render_template("apology.html", apology=apology)

        # Get the correct answers.
        correct_answerIDs = []
        for questionID, answerID in request.form.items():
             correct_answerID = db.execute("SELECT id FROM answers WHERE is_correct='TRUE' AND question_id IN (SELECT question_id FROM answers WHERE id=?)", answerID)[0]["id"]
             correct_answerIDs.append(correct_answerID)

        return render_template("result.html", questions=questions, selections=selections, answerIDs=answerIDs, correct_answerIDs=correct_answerIDs)
