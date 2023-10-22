
from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)

#views.py
from models import Todo


@app.route('/',methods = ['GET','POST'])
def home():
    allTodo = Todo.query.all()
    return render_template('home.html', allTodo = allTodo)


@app.route("/add", methods = ['GET','POST'])
def add():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        
        todo = Todo(title = title , desc = desc )
        
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    return render_template("add.html")

@app.route("/update/<int:sno>" , methods = ['GET','POST'])
def update(sno):
    if request.method =="POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno = sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo = Todo.query.filter_by(sno = sno).first()
    return render_template("update.html",todo=todo)


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")



if "__name__"  == "__main__":
    app.run( debug = True )

