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

            .radio {{
                padding: 40px;
            }}
            
            #key {{
            	font: 12px sans-serif;
            }}
            
        </style>
    </head>
    <body>
        <form action = "/encrypt" method = 'post'>
            
            
            <p><label for="encrypt">Encrypt</label>
                <input name="direction" class="radio" id="encrypt" type="radio" checked="checked" 
                value="encrypt"></input>

                <label for="decrypt">Decrypt</label>
                <input name="direction" class="radio" id="decrypt" type="radio" value="decrypt"></input></p>

            <p><label for="caesar">Caesar</label>
                <input name="cypher_type" class="radio" id="caesar" type="radio" checked="checked" value="caesar"> 
                </input>

                <label for="decrypt">Vigenere</label>
                <input name="cypher_type" class="radio" id="vigenere" type="radio" value="vigenere"></input></p>

            <label id="key">Key int (Caesar) or word (Vigenere):
                    <input name="rot" type="text" value="0"/>
            </label>

                <textarea name="text">{0}</textarea>
            
            <input type="submit"/>
        </form>
      <!-- create your form here -->
    </body>
</html>
"""

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
	from helpers import rotate_character, vigenere
	from flask import request
	def is_int(s):
		try:
			int(s)
			return True
		except ValueError:
			return False

	direction = request.form['direction']
	cypher = request.form['cypher_type']
	rot = request.form['rot']
	text = request.form['text']

	if cypher == 'caesar' and direction == 'encrypt' and is_int(rot):
		new_text = rotate_character(text,int(rot))
		return form.format(new_text)

	if cypher == 'caesar' and direction == 'decrypt' and is_int(rot):
		new_text = rotate_character(text,-int(rot))
		return form.format(new_text)

	if cypher == 'vigenere' and direction == 'encrypt' and rot.isalpha():
		new_text = vigenere(text,rot,1)
		return form.format(new_text)

	if cypher == 'vigenere' and direction == 'decrypt' and rot.isalpha():
		new_text = vigenere(text,rot,-1)
		return form.format(new_text)
	else:
		return form.format(text)

app.run()

