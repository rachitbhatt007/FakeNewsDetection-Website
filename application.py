from flask import Flask,render_template,session,logging,url_for,redirect,request
import pickle
	
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=="POST":
		feature = (request.form["news"])
		
		prediction=model.predict([feature])
		prob=model.predict_proba([feature])
		return render_template("index.html",prediction_text="the news is {}".format(prediction[0]),probability="The truth probability score is {}".format(prob[0][1]))
	else:
		return render_template("index.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")


@app.route('/about')
def about():
	return render_template("about.html")		

if __name__ == "__main__":
	app.run(debug=True)    