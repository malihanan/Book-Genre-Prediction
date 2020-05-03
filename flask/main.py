from flask import  Flask,render_template,request
import pickle
import predictfunctions
import json
from preprocessfunctions import preprocesswithoutstem

with open('./clf.pickle', 'rb') as f:
    lsvc = pickle.load(f)
with open('./tf.pickle', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)
with open('multi.pickle', 'rb') as f:
    multilabel_binarizer = pickle.load(f)
with open('onevrest.pickle', 'rb') as f:
    onevrest = pickle.load(f)
with open('./sgd1.pickle','rb') as f:
    sgdclf=pickle.load(f)

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("genrepredict.html")

@app.route("/predict/",methods=['GET','POST'])
def predict():
    query = request.args.get('query')
    preprocessedq=preprocesswithoutstem(query)
    l = predictfunctions.linearsvc(lsvc,preprocessedq)
    s=predictfunctions.sgd(sgdclf,preprocessedq)
    o = predictfunctions.multionvsrest(tfidf_vectorizer,multilabel_binarizer,onevrest,query)
    data = {'linearsvc': l['reply'],'sgd':s['reply'], 'onevrest': o['reply']}
    response = data
    return response



if __name__ =="__main__":
    app.run(debug=True)