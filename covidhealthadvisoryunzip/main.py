from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
  if request.method == 'GET':
    return render_template("index.html")
  else: # POST
    name = request.form.get('name')
    meet = request.form.get('meet')
    sick = request.form.get('sick')

    if name == "Boris Johnson":
      message = "Hi "+ name + "! It seems like the herd immunity plan is very effective. Congratulations. But please stay at home."
    elif name == "Ben":
      message = "Hi "+ name + "! Go home and play Minecraft."
    elif name == "Danny Seah":
      message = "Hi "+ name + "! Please stay in your classroom in block D."
    elif name == "Don":
      message = "Hi "+ name + "! Go home and play Pokemon Sword."
    elif name == "Sam":
      message = "Hi "+ name + "! Go home and stop playing games. Addiction is bad. :>"
    elif name == "Platelet Chan":
      message = "Platelet Chan FTW"

    elif meet == "yes":
      message = "Hi "+ name + "! Please stay at home."
    elif sick == "yes":
      message = "Hi "+ name + "! Please stay at home."
    else: 
      message = "Hi "+ name + "! You may go to school or work but don't forget social distancing. :)"
      
    fout = open("INFO.txt", 'a')
    fout.write(name + ',' + meet + ',' + sick + '\n')
    fout.close()
    fin = open("INFO.txt", 'r')
    fin.close()

    return render_template("output.html", message=message, name=name)

app.run(host='0.0.0.0', port=8080)