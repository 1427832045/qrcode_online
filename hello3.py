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
@app.route('/user',methods=['GET','POST'])
def user():
    #判断请求方式为POST否则为GET
    if request.method == 'POST':
        name=request.form.get('name', 'default value')#参数不存在时默认default value
        print('name:%s' % (name))
    else:
        name = request.args.get('name', 'default value')#参数不存在时默认default value
        print('name:%s' % (name))
    img = qrcode.make(name)
    img.save("static/123.jpg")
    return render_template('inde.html')
if __name__ == '__main__':
#    app.run(host="0.0.0.0",port=int("8999"))
    app.run(port=int("8080"))
