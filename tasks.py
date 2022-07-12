from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import current_user
from app import db
from models import User, Files, Tasks


tasks = Blueprint('tasks', __name__)

@tasks.route('/tasks')
def tasks_init():
    tasks = Tasks.query.order_by(Tasks.date)
    files = Files.query.order_by(Files.task_id)
    return render_template("tasks.html", tasks=tasks, files=files)

@tasks.route('/create')
def create_task():
    users = User.query.filter(User.role == "Преподаватель").all()
    return render_template('create.html', users=users)

@tasks.route('/create', methods=['POST'])
def create_task_post():
    user_to = request.form['user']
    title = request.form['title']
    text = request.form['text']
    files = request.files.getlist('file')
    task = Tasks(title=title, text=text, user_to=user_to, user_from=current_user.name)
    for file in files:
        print(file)
        add = Files(task_id=1, file=file.read())
        try:
            db.session.add(add)
            db.session.commit()
    
        except:
            print('ошибка в файлах')
            return redirect('/tasks')
    
    try:
        db.session.add(task)
        db.session.commit()
    
    except:
        print('ошибка в таске')
        return redirect('/tasks')
    
    return render_template("create.html")