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
    url = []
    x = result1.split()
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            url.append(i)
    url1 = url[0]
    if 'Link to the repository' in result1:
        k = result1.index('Link')
    else:
        k = result1.index(url1)
    ip = result1.index(title1)
    l = len(title1)
    ip = ip+ l + 1
    explan1 = result1[ip:k:]
    print(explan1)
    
    title = re.split(':', result2)
    title2 = title[0]
    url = []
    x = result2.split()
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            url.append(i)
    url2 = url[0]
    if 'Link to the repository' in result2:
        k = result2.index('Link')
    else:
        k = result2.index(url2)
    ip = result2.index(title2)
    l = len(title2)
    ip = ip+ l + 1
    explan2 = result2[ip:k:]
    print(explan2)
    # print(title1)
    title = re.split(':', result3)
    title3 = title[0]
    url = []
    x = result3.split()
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            url.append(i)
    url3 = url[0]
    if 'Link to the repository' in result3:
        k = result3.index('Link')
    else:
        k = result3.index(url3)
    ip = result3.index(title3)
    l = len(title3)
    ip = ip+ l + 1
    explan3 = result3[ip:k:]
    print(explan3)
    
    title = re.split(':', result4)
    title4 = title[0]
    url = []
    x = result4.split()
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            url.append(i)
    url4 = url[0]
    if 'Link to the repository' in result4:
        k = result4.index('Link')
    else:
        k = result4.index(url4)
    ip = result4.index(title4)
    l = len(title4)
    ip = ip+ l + 1
    explan4 = result4[ip:k:]
    print(explan4)
    
    title = re.split(':', result5)
    title5 = title[0]
    url = []
    x = result5.split()
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            url.append(i)
    url5 = url[0]
    if 'repository' in result5:
        k = result5.index('Link')
    else:
        k = result5.index(url5)
    ip = result5.index(title5)
    l = len(title5) 
    ip = ip+ l + 1
    explan5 = result5[ip:k:]
    print(explan5)
    return render_template("result.html", title1 = title1, explan1 = explan1 , url1=url1, title2 = title2, explan2 = explan2 , url2=url2, title3 = title3, explan3 = explan3 , url3=url3, title4 = title4, explan4 = explan4 , url4=url4, title5 = title5, explan5 = explan5 , url5=url5)
   

def generate(level,stacks):
    return f""" Suggest five {level} level project ideas using {stacks} with explanation and link to a sample repository in a bulleted format using •  in the following format
    • project name : explanation
    Link to the repository
    There should be no hypen in the title name 
    
    
    """

if __name__ == '__main__' :
    app.run(debug=True)
