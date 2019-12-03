from flask import Flask, render_template, url_for, request
from gec_code.predict import gec_predict

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/',methods=['POST'])
def predict():

	if request.method == 'POST':
		message = request.form['message']
		my_prediction = gec_predict(message)

	return render_template('result.html', prediction=my_prediction, message=message)


if __name__ == '__main__':
	app.run(debug=True)
