import openai
from openai import OpenAI
from flask import Flask, request, render_template, redirect, flash, session
from secret import OPENAI_API_KEY
client = OpenAI()
app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
openai.api_key = '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'

sign='gemini'

# @app.route('/')
def test_gpt():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"retrieve the  Daily Horoscope for {sign} ."},
            {"role": "user", "content": f"display a 3 line summary of the horoscope."}
            # {"role": "system", "content": "You are a , skilled in explaining complex programming concepts with creative flair."},
            # {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    msg = completion.choices[0].message
    return print(f'{msg}')
test_gpt()