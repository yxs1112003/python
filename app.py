from flask import Flask, request
from flask_restful import abort
from util import CommonUtil
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://172.27.12.67:27017/sun',
)

logger = CommonUtil.logger

mongo = PyMongo(app)


@app.route('/')
def index():
    return "Hello Flask"

@app.route('/addUser', methods=['GET', 'POST'])
def add_user():
    # user = {'name': 'Michael', 'age': 18, 'scores': [{'course': 'Math', 'score': 76}]}
    post_data = request.get_json()
    if post_data['username'] is None or post_data['password'] is None:
        abort(400)
    # if User.query.filter_by(username=username).first() is not None:
    #     abort(400)  # existing user
    # mongo.db.users.insert_one(post_user)
    return ""


if __name__ == '__main__':
    app = app.run(debug=True)
