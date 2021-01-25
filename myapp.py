from flask import Flask, render_template, request,url_for
import pickle
import numpy as np 

model1 = pickle.load(open('heart.pkl','rb'))
model2 = pickle.load(open('diabetes.pkl','rb'))
model3 = pickle.load(open('cancer.pkl','rb'))

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
	return render_template('webpage.html')

@app.route('/goback')
def goback():
	return render_template('webpage.html')

@app.route('/diabetes')
def diabetes():
	return render_template("diabetes_form.html")

@app.route('/cancer')
def cancer():
	return render_template("b_cancer.html")

@app.route('/heart_disease')
def heart_disease():
	return render_template("heart_disease.html")


@app.route('/Predict Heart Problem',methods = ['POST'])
def h_predict():

	d1 = request.form['age']
	d2 = request.form['cp']
	d3 = request.form['bp']
	d4 = request.form['chol']
	output = model1.predict([[int(d1),int(d2),int(d3),int(d4)]])

	if output==0:
		return render_template('heart_disease.html',data = 'You Dont have any Heart Problem')
	elif output==1:
		return render_template('heart_disease.html',data='It seems You Have Heart Problem :-(')
@app.route('/Predict diabetes Problem',methods = ['POST'])

def d_predict():

	d1 = request.form['age']
	d2 = request.form['Glucose']
	d3 = request.form['bp']
	d4 = request.form['ST']
	d5 = request.form['Insulin']
	d6 = request.form['DPF']
	output = model2.predict([[int(d1),int(d2),int(d3),int(d4),int(d5),float(d6)]])

	if output==0:
		return render_template('diabetes_form.html',data = 'You Dont have Diabetes Problem')
	elif output==1:
		return render_template('diabetes_form.html',data='It seems You Have diabetes Problem :-(')

@app.route('/Predict Cancer Problem',methods = ['POST'])

def c_predict():

	d1 = request.form['mean_radius']
	d2 = request.form['mean_texture']
	d3 = request.form['mean_perimeter']
	d4 = request.form['mean_area']
	d5 = request.form['mean_smoothness']
	output = model3.predict([[float(d1),float(d2),float(d3),float(d4),float(d5)]])

	if output==0:
		return render_template('b_cancer.html',data = 'You Dont have any Cancer Problem :-)')
	elif output==1:
		return render_template('b_cancer.html',data='It seems You Have Cancer Problem :-(')

if __name__=="__main__":
	app.run(debug = True)