from flask import render_template,jsonify
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
    user = {'nickname': 'Vinay'}  



    return render_template("index.html",
                           title='Home',
                           user=user,
                           blogs=blogs)


blogs = [
    {
        'id': 1,
        'title': u'china town',
        'content': u'Chinese market going down'
        
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'content': u'Need to find a good Python tutorial on the web'
        
    }
]

@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify({'blogs': blogs})
