from flask import  Flask,render_template,request
import pickle
import predictfunctions
import json
with open('./clf.pickle', 'rb') as f:
    lsvc = pickle.load(f)
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("genrepredict.html")

@app.route("/predict/",methods=['GET','POST'])
def predict():
    query = request.args.get('query')

    # stuff happens here that involves data to obtain a result

    response = predictfunctions.linearsvc(lsvc,query)

    # result = [CBReply(data[0]['query'])]

    return json.dumps(response)



if __name__ =="__main__":
    app.run(debug=True)