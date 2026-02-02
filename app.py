from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/hello/<username>/')
def hello(username):
    # name = request.args.get("name", "Flask")
    return f"Hello, {escape(username) + "\n" + url_for('home')}!"

@app.route('/cal/<int:num>')
def cal(num):
    return  12 + num

@app.route('register',methods=['GET','POST'])
def register():
    return  render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)