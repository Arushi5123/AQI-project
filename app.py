from flask import Flask,url_for,render_template,request
import joblib
models=joblib.load('./models/decisiontreeclassifier.lb')
app=Flask(__name__)
@app.route('/')
def contact():
    return render_template('project.html')
@app.route('/prediction', methods=['GET','POST'])#by defaultm get if method not specified
def prediction(): # city	year	aqi	co	no	no2	o3	so2	pm2_5	pm10	nh3
    if request.method=='POST':
        city=int(request.form['city'])
        year=int(request.form['year'])
        co=int(request.form['co'])
        no=int(request.form['no'])
        no2=int(request.form['no2'])
        o3=int(request.form['o3'])
        so2=int(request.form['so2'])
        pm2_5=int(request.form['pm2_5'])
        pm10=int(request.form['pm10'])
        nh3=int(request.form['nh3'])
        unseen_data=[[city,year,co,no,no2,o3,so2,pm2_5,pm10,nh3]]
        prediction=models.predict(unseen_data)[0]
        if prediction==1:
            return  render_template('final1.html',output=prediction)
        elif prediction==2:
            return  render_template('final2.html',output=prediction)
        elif prediction==3:
            return  render_template('final3.html',output=prediction)
        elif prediction==4:
            return  render_template('final4.html',output=prediction)
        elif prediction==5:
            return  render_template('final5.html',output=prediction)
if __name__ == '__main__':
    app.run(debug=True)