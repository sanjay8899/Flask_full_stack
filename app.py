from flask import Flask , render_template , request , make_response , sessions
from flask_cors import CORS 
from models import create_post , get_posts , verify_user

app= Flask(__name__)
CORS(app)

@app.route('/post', methods= ['GET', 'POST'])
def post():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        content = request.form.get('content')
        create_post(name , content)

    posts = get_posts()
    resp = make_response(render_template('posts.html' , posts=posts))
    resp.set_cookie('role','user')
    return resp

@app.route('/login' , methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = verify_user(username,password)
        if not user:
            print("invalid credentials")
            return render_template('login.html')

        if user:
            return render_template('posts.html')


if __name__ == "__main__":
    app.run(debug=True)