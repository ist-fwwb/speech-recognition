# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import speech_recognition
import text_structure
import dao
import thread


app = Flask(__name__)
# 使 jsonify 能够返回中文
app.config['JSON_AS_ASCII'] = False

@app.route('/recognize/<note_id>')
def recognize_controller(note_id):
    note = dao.MeetingNote.objects(id=note_id)
    if len(note) == 0:
        return jsonify({"status": "error", "detail": "Note not exist"})
    note = note[0]

    if note.meetingNoteType != "VOICE":
        return jsonify({"status": "error", "detail": "Not a voice note"})

    meeting = dao.Meeting.objects(id=note.meetingId)
    if len(meeting) == 0:
        return jsonify({"status": "error", "detail": "Meeting not exist"})

    meeting = meeting[0]

    result = speech_recognition.recognize(note.voiceFileName)
    if result["status"] != "error":
        thread.start_new_thread(speech_recognition.checkAndDelete, (result["taskid"], note, meeting))
    return jsonify(result)

@app.route('/check/<file_name>/<taskid>')
def check_controller(file_name, taskid):
    return jsonify(speech_recognition.check(file_name, taskid))

@app.route('/result/<file_name>/<taskid>')
def result_controller(file_name, taskid):
    return jsonify(speech_recognition.result(file_name, taskid))

@app.route('/tag/<text>')
def tag_controller(text):
    return jsonify(text_structure.tag(text))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
