from flask import Flask
app = Flask(__name__)
class User1:
    id :int
    fisrt_name : str
    last_name :str 

part1_user=[User1]

@app.route('/user_part1/{id}')
def hget_part1_user(id : int):
    for user in part1_user:
        if user.id==id:
            return user
    return -1

@app.route('/user_part1/{user}')
def post_part1_user(user : User1):
    part1_user.append(user)
    return '204'

