from flask import Flask , render_template, flash,request,abort
from flask_bootstrap import  Bootstrap

app = Flask(__name__)
app.secret_key = '123 for fun ' # a password
Bootstrap(app)

@app.route('/')
def hello_world():
    flash("test")
    return render_template("index.html")

@app.route('/test')
def test():
    return  render_template("test.html")

@app.route('/login',methods=["POST"])
def log_in():
    flash("note success")
    form = request.form
    name = form.get('name')
    message =form.get('message')
    flash(name)
    flash(message)
    return  render_template("index.html")

@app.errorhandler(404)
def error(e):
    return  render_template("404.html")

@app.route('/404')
def e_test():
    abort(404)

@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id) == 1:
        return render_template("user.html")
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
