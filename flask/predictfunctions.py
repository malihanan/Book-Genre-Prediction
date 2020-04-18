from preprocessfunctions import preprocesswithoutstem
from sklearn.svm import LinearSVC

def linearsvc(clf,summary):
    summary=preprocesswithoutstem(summary)
    y_pred=clf.predict([summary])
    return {'reply':list(y_pred)}