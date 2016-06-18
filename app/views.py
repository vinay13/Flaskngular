from flask import render_template
from app import app

from .models import Blog
#from flask.ext import restful

#from app import api, db
#from models import  Blog
#from forms import UserCreateForm, SessionCreateForm, PostCreateForm
#from serializers import UserSerializer, PostSerializer

@app.route('/')
@app.route('/index')
def index():
    blogs=Blog.query.all()
    user = {'nickname': 'Vinay'}  # fake user



    return render_template("index.html",
                           title='Home',
                           user=user,
                           blogs=blogs)
"""
class PostView(restful.Resource):
    def get(self):
        posts = Blog.query.all()
        return PostSerializer(posts).data

api.add_resource(PostView, '/api/v1/posts')
"""
