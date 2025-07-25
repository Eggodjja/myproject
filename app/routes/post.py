from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)

@post.route('/', methods=['POST', 'GET'])
def all():
    posts = Post.query.all()
    return render_template('post/all.html', posts=posts)

@post.route('/post/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        post = Post(first_name=first_name, last_name=last_name, email=email)
        try:
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(str(e))
        return redirect('/')  
    return render_template('post/create.html')

@post.route('/post/<int:id>/update', methods=['POST', 'GET'])
def update(id):
   post = Post.query.get(id)
   if request.method == 'POST':
        post.first_name = request.form['first_name']
        post.last_name = request.form['last_name']
        post.email = request.form['email']
        try:
            db.session.commit()
            return redirect('/')  
        except Exception as e:
            print(str(e))
   return render_template('post/update.html', post=post) 

@post.route('/post/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):
   post = Post.query.get(id)
   try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/')  
   except Exception as e:
        print(str(e))
