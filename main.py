from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    Judul = "Homepage"
    return render_template('home.html', web_title= Judul)

@app.route("/about")
def About():
    Judul = "Biodata"
    return render_template('about.html', web_title= Judul)

@app.route("/projects")
def Gallery():
    Judul = "Projects"
    return render_template('projects.html', web_title= Judul)

@app.route("/contacts")
def Contacts():
    Judul = "Contacts"
    return render_template('contacts.html', web_title= Judul)
