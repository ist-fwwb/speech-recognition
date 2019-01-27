# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from speech_recognition import *
from text_structure import *
import thread


app = Flask(__name__)
# 使 jsonify 能够返回中文
app.config['JSON_AS_ASCII'] = False

@app.route('/recognize/<file_name>/<meeting_id>')
def recognize_controller(file_name, meeting_id):
    result = recoginze(file_name, meeting_id)
    if result["status"] != "error":
        thread.start_new_thread(checkAndDelete, (file_name, result["taskid"]))
    return jsonify(result)

@app.route('/check/<file_name>/<taskid>')
def check_controller(file_name, taskid):
    return jsonify(check(file_name, taskid))

@app.route('/result/<file_name>/<taskid>')
def result_controller(file_name, taskid):
    return jsonify(result(file_name, taskid))

@app.route('/tag/<text>')
def tag_controller(text):
    return jsonify(tag(text))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
