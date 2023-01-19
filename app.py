from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key1993'

debug = DebugToolbarExtension(app)


@app.route('/')
def ask_question():
    '''Show form to input words to create a story'''
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)


@app.route('/story')
def create_story():
    '''Create a story from inputs from a form'''

    generated_story = story.generate(request.args)
    return render_template('story.html', text=generated_story)
