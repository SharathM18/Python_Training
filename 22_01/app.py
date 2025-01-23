from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# @app.route('/')
# def greeting():
#     return "<p>Hey, Dude!</p>"

@app.route('/admin')
def admin():
    return "<h1 style='color: blue;  font-size: 3rem;'>i'm Admin</h1>"

@app.route('/user/<name>')
def greeting(name):
    return redirect(url_for('admin')) if name == 'admin' else f"Hello {name}!"

@app.route('/<num>')
def even_odd(num):
    return 'even' if int(num) % 2 == 0 else 'odd'

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

database =  {'alex': '123', 'colt': '234'}
@app.route('/form_login',methods=['POST','GET'])
def login_op():
    name = request.form['username']
    pwd = request.form['password']

    if name in database:
        if database[name]!= pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('home.html',name=name)
    else:
        return render_template('login.html', info='Invalid User')

if __name__ == '__main__':
    app.run(debug=True)

# in django views for creating a routing function/ class
# in django modal: store the data or connecting to database
# in django templates are html code/ filesnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn