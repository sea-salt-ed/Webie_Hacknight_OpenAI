import os 
import openai
from flask import Flask, render_template, url_for, redirect
from flask.globals import request
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

app = Flask(__name__)

openai.api_key = os.environ.get('ENV_VAR')






@app.route('/', methods = ("GET", "POST"))
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
        for _  in range(0,3):
            response = openai.Completion.create(
            model="text-davinci-003",prompt = prompt
        )
            res += response.choices[0].text 
            
            
        return redirect(url_for("index", result=res))

    result = request.args.get("result")
    return render_template("index.html", result=result)



def generate(level,stacks):
    return f""" Suggest some {level} level project ideas using {stacks} with explanation
    
    
    """

if __name__ == '__main__' :
    app.run(debug=True)
