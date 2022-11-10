from flask import Flask, request, jsonify
from hanzannlp.hanzannlp import nlpfunction
from urllib import parse
import json
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route("/sendstr", methods=['POST'])
def test():
   result = request.get_json()
   modestr = result['mode']
   inputString = result['inputstring']
   strlist = nlpfunction(modestr, inputString)
   return strlist;

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)