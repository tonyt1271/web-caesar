from flask import Flask, request	#request is a "request object" in
									#flask.

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset = "utf-8">
	</head>
	<body>
		<form action="/hello" method = "POST">
			<label for="first_name">First Name:</label>
			<input id="first_name" type="text" name="first_name"/>

			<label for="last_name">Last Name:</label>
			<input id="last_name" type="text" name="last_name"/>

			<input type="submit" />
		</form>
	</body>
</html>
"""

@app.route("/")
def index():
	return form

@app.route("/hello", methods = ['POST'])	#defining another handeler that takes requests at
def hello():			#/hello
	#first_name = request.args.get('first_name')	#Using the request object's args method that
									#that has a .get submethod to retrieve 
									#the item named 'first_name' and save it 
									#to a variable this is for method = 'get'
	first_name = request.form['first_name'] #this is for method = 'post'
	last_name = request.form['last_name']
	return "<h1>Hello, "+first_name+" "+last_name+"!</h1>"
app.run()

#<form action="https://duckduckgo.com" method="get">
#			<label for="search_term">Search Term:</label>
#			<input id="search_term" type="text" name="q"/>
#			<input type="submit"/>
#		</form>