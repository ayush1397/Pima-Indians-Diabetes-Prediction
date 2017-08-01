#!C:/Anaconda3/python.exe
import cgi
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import numpy as np
import urllib.request
from sklearn import preprocessing

form = cgi.FieldStorage()

a1=int(form['txt1'].value)
a2=int(form['txt2'].value)
a3=int(form['txt3'].value)
a4=int(form['txt4'].value)
a5=int(form['txt5'].value)
a6=float(form['txt6'].value)
a7=float(form['txt7'].value)
a8=int(form['txt8'].value)

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

raw_data = urllib.request.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")

X = dataset[:,0:8]
y = dataset[:,8]

#X=preprocessing.normalize(X)

model = LogisticRegression()
model.fit(X, y)

a = np.array([a1,a2,a3,a4,a5,a6,a7,a8])

expected = y
predicted = model.predict(a)

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Demo</title>")
print ("</head>")
print ("<body>")
print(a1,a2,a3,a4,a5,a6,a7,a8,a)
print(predicted)
print ("</body>")
print ("</html>")