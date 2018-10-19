#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

def factors(num):
	return [x for x in range(1, num+1) if num%x==0]

@app.route('/factors_raw/<int:num>')
def factors_display_raw_html(num):
	factors_list = factors(num)
	# The Header of the HTML page
	html = "<h1>The factors of " + str(num) + " are:</h1>" + "\n" + "<ul>"

	# For each factor, we are putting a <li> tag for it
	for f in factors_list:
		html += "<li>" + str(f) + "</li>" + "\n"
	
	# Closing HTML tags
	html += "</ul>"

	# return the variable 'html'
	return html

@app.route('/factors/<int:num>')
def factors_rout(num):
	return "The factors of {} are {}".format(num, factors(num))

@app.route('/')
def hello_world():
	return 'Hello World! Open the URL in another tab and then go to /hello/yourname'

@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello ' + name + '!'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
