# Day : 1
# Date : 20-03-21

# My first Flask app
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
# 	return " Everythig is Possible, Just never give up so fast.. Got it"


# @app.route('/david')
# def david():
# 	return "Hello David"


# Another to see any name

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return f'Hello , World !'

# @app.route("/<string:name>")
# def hello(name):
# 	name = name.capitalize() # To capitalize First word in the name.
# 	return f'<h1>Hello {name} </h1>!'


# To render file in the HTML

# from flask import Flask , render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
# 	headline = 'Hello , World Headline !'
# 	return render_template('index.html', headline = headline)

# @app.route('/bye')
# def bye():
# 	headline = 'GoodBye Now!! Reload'
# 	return render_template('index.html' , headline = headline)


# Day : 2
# Date : 21-03-21


# from flask import Flask, render_template

# myapp = Flask(__name__)

# @myapp.route('/')
# def hello():
# 	button = "Click me ! Now ? again now"
# 	return render_template ('index.html',button = button)

# @myapp.route('/next')
# def next():
# 	headline = 'This is the next Line !'
# 	return render_template('index.html', headline = headline)









