import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="flaskBlogger",
    password="omglol123#",
    hostname="flaskBlogger.mysql.pythonanywhere-services.com",
    databasename="flaskBlogger$flaskBloggerDB",
)