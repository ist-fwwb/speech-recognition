# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from speech_recognition import *
import thread
from oss import *

app = Flask(__name__)
# 使 jsonify 能够返回中文
app.config['JSON_AS_ASCII'] = False

def checkAndDelete(taskid, file_name):
    while True:
        # 每隔20秒获取一次任务进度
        progress = get_progress(taskid, file_name)
        progress_dic = json.loads(progress)
        if progress_dic['err_no'] != 0 and progress_dic['err_no'] != 26605:
            print 'task error: ' + progress_dic['failed']
            return
        else :
            data = progress_dic['data']
            task_status = json.loads(data)
            if task_status['status'] == 9:
                print 'task ' + taskid + ' finished'
                delete_local_file(file_name)
                break
            print 'The task ' + taskid + ' is in processing, task status: ' + data

        # 每次获取进度间隔20S
        time.sleep(20)

@app.route('/recognize/<file_name>')
def recognize(file_name):
    get_file_from_oss(file_name, file_name)
    pr = prepare(file_name)
    prepare_result = json.loads(pr)
    if prepare_result['ok'] != 0:
        print 'prepare error, ' + pr
        return jsonify({'status':'error', 'detail': pr})

    taskid = prepare_result['data']
    print 'prepare success, taskid: ' + taskid

    # 2.分片上传文件
    if upload(taskid, file_name):
        print 'upload success'
    else :
        print 'uoload fail'

    # 3.文件合并
    mr = merge(taskid, file_name)
    merge_result = json.loads(mr)
    if merge_result['ok'] != 0:
        print 'merge fail, ' + mr
        delete_local_file(file_name)
        return jsonify({'status':'error', 'detail': mr})
    thread.start_new_thread(checkAndDelete, (taskid, file_name))
    return jsonify({'taskid':taskid,'status':'success', 'detail': 'null'})

@app.route('/check/<file_name>/<taskid>')
def check(file_name, taskid):
    progress = get_progress(taskid, file_name)
    progress_dic = json.loads(progress)
    if progress_dic['err_no'] != 0 and progress_dic['err_no'] != 26605:
        return jsonify({'taskid': taskid, 'status':'failed', 'detail':progress_dic['failed']})
    else :
        data = progress_dic['data']
        task_status = json.loads(data)
        if task_status['status'] == 9:
            return jsonify({'taskid':taskid, 'status':'finished', 'detail':'null'})
        return jsonify({'taskid':taskid, 'status':'processing', 'detail':data})

@app.route('/result/<file_name>/<taskid>')
def result(file_name, taskid):
    lfasr_result = json.loads(get_result(taskid, file_name))
    print "result: " + lfasr_result['data']
    return jsonify(lfasr_result['data'])

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
