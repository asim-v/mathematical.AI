from flask import Flask,render_template
import os
import openai
openai.api_key = ""

def process(input_proof):
	#input_proof = 'Let ABC be any triangle. If the angle ABC is greater than any of thetwo other internal angles of the triangle, shows that the length of side AC is greaterthan any of the lengths of the other two sides of the triangle. This is, in anytriangle, the greater angle subtends to the greater side.'

	result = openai.Completion.create(
	  engine="davinci",
	  prompt=
	'This system knows how to clearly write any mathematical proof in english, when the proof ends, it always adds this symbol:□, for the following proposition:\n"""\n{}\n""".\nIt outputs the following simple and rigorous proof:\n1) '.format(input_proof),
	  max_tokens=200,
	  frequency_penalty = 0.4,
	  best_of=3,
	  stop="□"
	)

	output = result["choices"][0]["text"]	
	if output[0:2] != "1)":	
		output = '1) '+result["choices"][0]["text"]	
	return output

app = Flask('__app__')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/<input_query>',methods=["GET",	"POST"])
def api(input_query):
	return process(input_query)

if __name__ == '__main__':
	app.run()

