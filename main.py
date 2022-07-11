from tokenize import group
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('профиль.html', name=current_user.name, role = current_user.role,
    faculty = current_user.faculty, email=current_user.email, group=current_user.group)