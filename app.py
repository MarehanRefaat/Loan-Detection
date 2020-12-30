'''
import numpy as numpy
from flask import Flask, request, jsonify, render_template
import pickle
import os 



def load_model():
	return pickle.load(open('classifi_model.pickle','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	labels = ['Approved','Rejected']

	features = [float(x) for x in request.form.values()]

	values = [np.array(features)]

	model = load_model()
	prediction = model.predict(values)

	result = labels[prediction[0]]

	return render_template('index.html', output= 'The status is {}'.format(result))
if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app=Flask(__name__,template_folder='templates')

model = pickle.load(open('classifi_model.pickle','rb'))

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/predict',methods = ['POST'])
def predict():

	int_features = [int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)

	output = round(prediction[0],2)

	return render_template('index.html',prediction_text = 'Loan detection is  {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)