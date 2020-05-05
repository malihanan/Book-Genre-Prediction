from flask import  Flask,render_template,request
from flask_cors import CORS,cross_origin
import pickle
import predictfunctions
import json
import logging
from flask import jsonify
from preprocessfunctions import preprocesswithoutstem

with open('./clf.pickle', 'rb') as f:
    lsvc = pickle.load(f)
with open('./tf.pickle', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)
with open('multi.pickle', 'rb') as f:
    multilabel_binarizer = pickle.load(f)
with open('onevrest.pickle', 'rb') as f:
    onevrest = pickle.load(f)
with open('./sgd.pickle','rb') as f:
    sgdclf=pickle.load(f)

app = Flask(__name__)
cors = CORS(app, resources={r"/predict/*": {"origins": "http://127.0.0.1"}})

if app.debug is not True:   
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('info.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("genrepredict.html")

@app.route("/predict/",methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'GET':
        app.logger.error("GET request")
        query = request.args.get('query')
        title = request.args.get('name')
    else:
        app.logger.error("POST request")
        query = request.form.get('query')
        title = request.form.get('name')

    preprocessedq=preprocesswithoutstem(query)
    l = predictfunctions.linearsvc(lsvc,preprocessedq)
    s=predictfunctions.sgd(sgdclf,preprocessedq)
    o = predictfunctions.multionvsrest(tfidf_vectorizer,multilabel_binarizer,onevrest,query)
    data = {'linearsvc': l['reply'],'sgd':s['reply'], 'onevrest': o['reply']}
    
    app.logger.error("TITLE: " + str(title))
    app.logger.error("SUMMARY: " + str(query))
    app.logger.error("LSVC: " + str(l['reply']))
    app.logger.error("SGD: " + str(s['reply']))
    app.logger.error("OVSR: " + str(o['reply']) + "\n")
    response = jsonify(data)
    return response
    
if __name__ =="__main__":
    app.run(host='0.0.0.0', port=80)