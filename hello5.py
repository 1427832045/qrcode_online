#!/user/bin/env python3
# -*- coding: utf-8 -*-
import qrcode
from flask import Flask
from flask import render_template,url_for
from flask import jsonify
from flask import request
from datetime import timedelta
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)
@app.route('/login',methods=['GET','POST'])
def login():
    #判断请求方式为POST否则为GET
    if request.method == 'POST':
        user = request.form['nm']
        print(user)
    else:
        user = request.args.get('nm')
        print(user)
    img = qrcode.make(user)
    img.save("static/123.jpg")
    return '<img src="/static/123.jpg"/>'
if __name__ == '__main__':
    app.run()
