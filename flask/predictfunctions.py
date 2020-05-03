from preprocessfunctions import preprocesswithoutstem,clean_text,remove_stopwords1
from sklearn.svm import LinearSVC

def linearsvc(clf,summary):
    y_pred=clf.predict([summary])
    return {'reply':list(y_pred)}

def sgd(clf,summary):
    y_pred=clf.predict([summary])
    return {'reply':list(y_pred)}

def multionvsrest(tfidf_vectorizer,multilabel_binarizer,clf,q):
    q = clean_text(q)
    q = remove_stopwords1(q)
    q_vec = tfidf_vectorizer.transform([q])
    q_pred_prob = clf.predict_proba(q_vec)
    t = 0.2505 # threshold value 0.2505 -> 0.7110468896756014
    q_pred_new = (q_pred_prob >= t).astype(int)
    return {'reply': multilabel_binarizer.inverse_transform(q_pred_new)}