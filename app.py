from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import openai
data=[(' ',' ')]
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        openai.api_key = "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"
        start_sequence = "\nAdua:"
        restart_sequence = "\nYou: "
        query= request.form['book']
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" You:", " Adua:"]
        )
        data.insert(0,(query,response.choices[0].text ))
    return render_template('home2.html',data=data)
@app.route('/next')
def nextpage():
    return """This is next page <br>
Abhi kuch ni h isme <br>
<a href="/">back</a>"""
if __name__=='__main__':
    app.run(debug=True)
