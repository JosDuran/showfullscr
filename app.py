from flask import Flask, send_file, flash, redirect, session, render_template, request, url_for, jsonify,json, make_response
from werkzeug import secure_filename

import sqlite3, base64
import os, io, subprocess

 
app = Flask(__name__)
app.secret_key = 'super secret key'
 
    
DEFAULT_PATH = os.path.dirname(os.path.realpath(__file__))

 
@app.route('/')
def home():
    return render_template('index.html')
    
    
@app.route('/showfs', methods = ['POST'])
def shofs():
	afile = request.files['selectfile']
	asecure = secure_filename(afile.filename)
	afile.save(asecure)
	print(asecure);
	image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "black", "-g", "1280x800", asecure])		  
	return ('image displayed');
    
if __name__ == "__main__" :
    app.run(debug = True, host='0.0.0.0')
