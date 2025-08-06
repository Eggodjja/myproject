from flask import Blueprint, render_template, request, redirect
from ..extensions import db, csrf
from ..models.user import User

user = Blueprint('user', __name__)

@user.route('/', methods=['POST', 'GET'])
def all():
    posts = User.query.all()
    return render_template('user/all.html', posts=posts)

@user.route('/user/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        post = User(first_name=first_name, last_name=last_name, email=email)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')  
        except Exception as e:
            print(str(e))
            return "Something went wrong!"
    return render_template('user/create.html')

@user.route('/user/<int:id>/update', methods=['POST', 'GET'])
def update(id):
   post = User.query.get(id)
   if request.method == 'POST':
        post.first_name = request.form['first_name']
        post.last_name = request.form['last_name']
        post.email = request.form['email']
        try:
            db.session.commit()
            return redirect('/')  
        except Exception as e:
            print(str(e))
            return "Something went wrong!"
   return render_template('user/update.html', post=post) 

@user.route('/user/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):
   post = User.query.get(id)
   try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/')  
   except Exception as e:
        print(str(e))
        return "Something went wrong!"
