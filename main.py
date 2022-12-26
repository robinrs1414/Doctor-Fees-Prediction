import pickle
from flask import Flask, render_template,request,url_for


app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))

# home html
@app.route('/',methods=['GET','POSt'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POSt'])
def predict():
    features=[x  for x in request.form.values()]
    inputs=[]
    for i in range(len(features)):
        if i==0 or i==2:
            for j in list(features[i]):
                    inputs.append(float(j))
        elif i==4: 
            x=features[i].replace('%','') 
            inputs.append(float(x))
        else:
            inputs.append(float(features[i]))
    input=scaler.transform([inputs])
    prediction=model.predict(input)
    output=int(round(prediction[0],-2))
    return render_template('index.html', prediction_text=f'Doctor Fee Prediction : {output}/-')
    
 
if __name__=='__main__':
    app.run(debug=True)


