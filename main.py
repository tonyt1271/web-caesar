from flask import Flask	#request is a "request object" in
									#flask.

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style> /*internal styling*/
            form {{
                background-color: #eee;
                padding: 20px;/*padding: 20px;*/
                margin: 0 auto;/*margin: 0 auto;*/
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;/*margin: 10px 0;*/
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action = "/encrypt" method = 'post'>
            <label>Rotate by:
                    <input name="rot" type="text" value="0"/>
            </label>

                <textarea name="text">{0}</textarea>
            
            <input type="submit"/>
        </form>
      <!-- create your form here -->
    </body>
</html>
"""
# form = """
# <!DOCTYPE html>
# <html>
# 	<head>
# 		<meta charset = "utf-8">
# 	</head>
# 	<body>
# 		<form action="/hello" method = "POST">
# 			<label for="first_name">First Name:</label>
# 			<input id="first_name" type="text" name="first_name"/>

# 			<label for="last_name">Last Name:</label>
# 			<input id="last_name" type="text" name="last_name"/>

# 			<input type="submit" />
# 		</form>
# 	</body>
# </html>
# """

@app.route("/")
def index():
	return form.format("")

@app.route("/hello", methods = ['POST'])	#defining another handeler that takes requests at
def hello():			#/hello
	#first_name = request.args.get('first_name')	#Using the request object's args method that
									#that has a .get submethod to retrieve 
									#the item named 'first_name' and save it 
									#to a variable this is for method = 'get'
	first_name = request.form['first_name'] #this is for method = 'post'
	last_name = request.form['last_name']
	#return "<h1>Hello, "+first_name+" "+last_name+"!</h1>"
	
	return "<h1>Hello {} {}!</h1>".format(first_name,last_name)


@app.route("/encrypt", methods = ['POST'])
def caesar():
	from helpers import rotate_character
	from flask import request

	rot = request.form['rot']
	text = request.form['text']

	new_text = rotate_character(text,int(rot))

	return form.format(new_text)
	return "<h1><p>Original text: {} <p/><p>rotate by: {}</p> <p>Encoded text:  {}</p></h1>".format(text,rot,new_text)
app.run()

#<form action="https://duckduckgo.com" method="get">
#			<label for="search_term">Search Term:</label>
#			<input id="search_term" type="text" name="q"/>
#			<input type="submit"/>
#		</form>