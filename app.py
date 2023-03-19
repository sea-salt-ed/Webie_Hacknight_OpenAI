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
    level=" "
    stacks = " "
    
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
        result1 = final_res[1]
        result2 = final_res[2]
        result3 = final_res[3]
        result4 = final_res[4]
        result5 = final_res[5]
    
       
        
        
            
            
        return redirect(url_for("results", result1=result1, result2 = result2, result3=result3, result4=result4, result5=result5))

    return render_template("index.html")

@app.route('/result', methods=["GET"])
def results():
    result1 = request.args.get("result1")
    result2 = request.args.get("result2")
    result3 = request.args.get("result3")
    result4 = request.args.get("result4")
    result5 = request.args.get("result5")
    title = re.split(':', result1)
    title1 = title[0]
    ip = result1.index(title1)
    l = len(title1)
    ip = ip+ l + 1
    explan1 = result1[ip:]
    print(explan1)
    
    title = re.split(':', result2)
    title2 = title[0]
    ip = result2.index(title2)
    l = len(title2)
    ip = ip+ l + 1
    explan2 = result2[ip:]
    print(explan2)

    title = re.split(':', result3)
    title3 = title[0]
    ip = result3.index(title3)
    l = len(title3)
    ip = ip+ l + 1
    explan3 = result3[ip:]
    print(explan3)
    
    title = re.split(':', result4)
    title4 = title[0]
    ip = result4.index(title4)
    l = len(title4)
    ip = ip+ l + 1
    explan4 = result4[ip:]
    print(explan4)
    
    title = re.split(':', result5)
    title5 = title[0]
    ip = result5.index(title5)
    l = len(title5) 
    ip = ip+ l + 1
    explan5 = result5[ip:]
    print(explan5)
    return render_template("result.html", title1 = title1, explan1 = explan1 ,title2 = title2, explan2 = explan2 ,title3 = title3, explan3 = explan3 , title4 = title4, explan4 = explan4 , title5 = title5, explan5 = explan5)
   

def generate(level,stacks):
    return f""" Suggest five {level} level project ideas using {stacks} with explanation in a bulleted format using •  in the following format
    • project name : explanation
    There should be no hypen in the title name 
    
    
    """

if __name__ == '__main__' :
    app.run(debug=True)
