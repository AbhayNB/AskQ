from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import openai
data=[(' ',' ')]
app=Flask(__name__)
apik='123456789'
next='/askq'
@app.route('/askq',methods=['GET','POST'])
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
@app.route('/',methods=['GET','POST'])
def nextpage():
    if request.method=='POST':
        key= request.form['key']
        if key==apik:
            return redirect('/askq')
    return render_template('login.html')
if __name__=='__main__':
    app.run(debug=True)