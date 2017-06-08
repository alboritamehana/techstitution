from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('home/index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0',
   	port=82, debug=True)

@app.router("/about", method=['GET', 'POST'])
def about():
   	return "About page %s" %request.method

if __name__ == '__main__':
	app.run(host='0.0.0.0',
		port=82, debug=True)