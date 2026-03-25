from model import predict
_
sentiment
def test
_predict
_positive():
assert predict
_
sentiment("I am happy today") ==
"positive"
def test
_predict
_
negative():
assert predict
_
sentiment("I feel sad") ==
"negative"
def test
_predict
_
neutral():
assert predict
_
sentiment("The sky is blue") ==
"neutral"