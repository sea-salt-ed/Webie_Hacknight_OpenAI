import os 
import re
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
        final_res = re.split('•',res)
        pro1 = final_res[1]
        pro2 = final_res[2]
        pro3 = final_res[3]
        pro4 = final_res[4]
        pro5 = final_res[5]
    
       
        
        
            
            
        return redirect(url_for("results", result1=pro1, result2 = pro2, result3=pro3, result4=pro4, result5=pro5))

    return render_template("index.html")

@app.route('/result', methods=["GET"])
def results():
    result1 = request.args.get("result1")
    result2 = request.args.get("result2")
    result3 = request.args.get("result3")
    result4 = request.args.get("result4")
    result5 = request.args.get("result5")
    return render_template("result.html", result1=result1, result2 = result2, result3=result3, result4=result4, result5=result5)
    

def generate(level,stacks):
    return f""" Suggest five {level} level project ideas using {stacks} with explanation and link to a sample repository in a bulleted format using •  and project name , explanation and link with a line gap
    
    
    """

if __name__ == '__main__' :
    app.run(debug=True)
