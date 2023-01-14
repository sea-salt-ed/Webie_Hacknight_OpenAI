import os 
import openai
from flask import Flask, render_template, url_for, redirect
from flask.globals import request



app = Flask(__name__)

openai.api_key = os.getenv('ENV_VAR')







@app.route('/', methods = ("POST", "GET"))
def index():
    res = " "
    if request.method == "POST":
        level = request.form["level"]
        print(level)
        stacks = request.form["stacks"]
        print(stacks)
        prompt = generate(level,stacks)
        print(prompt)
        
        res = " "
        response = openai.Completion.create(
            model="text-davinci-003",prompt = prompt,
            max_tokens = 1000 
        )
        res = response.choices[0].text 
            
            
        return redirect(url_for("results", result=res))

    return render_template("index.html")

@app.route('/result', methods=["GET"])
def results():
    result = request.args.get("result")
    return render_template("result.html", result=result)
    

def generate(level,stacks):
    return f""" Suggest some {level} level project ideas using {stacks} with explanation
    
    
    """

if __name__ == '__main__' :
    app.run(debug=True)
