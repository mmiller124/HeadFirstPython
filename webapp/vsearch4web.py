from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
	phrase = request.form['phrase']
	letters = request.form['letters']
	title = 'Here are your results:'
	results = str(search4letters(phrase,letters))
	if results == 'set()':
		pass
	else:
		results = results[1:-1]
	return render_template('results.html', 
							the_title=title, 
							the_letters=letters, 
							the_phrase=phrase, 
							the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
	return render_template('entry.html',the_title='Welcome to search4letters on the web!')

app.run(debug=True)