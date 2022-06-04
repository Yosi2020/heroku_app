"""
   Welcome to Hearty plc flask app

"""

import joblib

from flask import Flask, request, jsonify
import json
import numpy as np

app = Flask(__name__)

model = joblib.load('decision_tree_model')

@app.route('/', methods = ['POST'])

def predict():
	event = json.loads(request.data)
	print(event)
	values = event['values']
	values = list(map(np.float, values))
	pre = np.array(values)
	pre = pre.reshape(1, -1)
	res = model.predict(pre)
	print(res)
	# send back to browser
	output = {'results': int(result[0])}
	
	# return data
	return jsonify(results=output)

if __name__ == '__main__':
	app.run(debug = True)
