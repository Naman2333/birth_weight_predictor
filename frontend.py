from flask import Flask,jsonify,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)

def cleaned_data(form_data):
    gestation=float(form_data["gestation"])
    parity=int(form_data["parity"])
    age=float(form_data["age"])
    height=float(form_data["height"])
    weight=float(form_data["weight"])
    smoke=float(form_data["smoke"])
    
    clean_data={
        "gestation":[gestation],
        "parity":[parity],
        "age":[age],
        "height":[height],
        "weight":[weight],
        "smoke":[smoke]
    }
    return clean_data
    
@app.route("/",methods=["GET"])
def home():
    return render_template("frontend.html")
    
@app.route("/predict",methods=["POST"])
def prediction():
    baby_data=request.form
    baby_cleand_data=cleaned_data(baby_data)
    Data_frame_baby=pd.DataFrame(baby_cleand_data)
    with open ("model.pkl","rb") as f:
        model=pickle.load(f)
    model_predict=model.predict(Data_frame_baby)
    model_predict=round(float(model_predict),2)
    return render_template("frontend.html",model_predict=model_predict)    


if __name__=="__main__":
    app.run(debug=True)

