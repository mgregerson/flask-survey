from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get('/')
def survey_start():
    """Show start of Survey"""

    return render_template('survey_start.html', title = survey.title, instructions = survey.instructions)


@app.get('/questions/<int:question_number>')
def ask_question(question_number):
    """Asks the user a question on a form"""

    print('question-number is', survey.questions[question_number])
    # question = survey.questions[question-number]

    return render_template('question.html', question = survey.questions[question_number])


