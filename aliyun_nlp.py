# -*- coding: utf8 -*-
import uuid
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.http import method_type
import json
# 创建AcsClient实例
client = AcsClient('LTAIby5D2cxpu0zG', 'EGjFkYGV1o2Q2gRYwBM7DiryBSB96T', 'cn-shanghai')
request = CommonRequest()
request.set_domain("nlp.cn-shanghai.aliyuncs.com") # 必须设置domain
request.set_method(method_type.POST); # 设置请求方式，目前只支持POST
request.add_header("x-acs-signature-method", "HMAC-SHA1") # 设置签名方法
request.add_header("x-acs-signature-nonce", uuid.uuid4().hex)# 设置请求唯一码，防止网络重放攻击, 每个请求必须不同
request.add_header("x-acs-signature-version", "1.0") # 设置签名版本
request.set_content_type("application/json;chrset=utf-8")  # 设置请求格式
request.set_accept_format("application/json;chrset=utf-8") # 设置响应格式
request.set_version('2018-04-08') # 设置版本
request.set_action_name("None")

def text_structure(text):
    content = json.dumps({
        "tag_flag":"true",
        "text":text,
        })
    request.set_uri_pattern("/nlp/api/textstructure/ecommerce") #设置所要请求的API路径
    request.set_content(content.encode('utf-8')) # 设置请求内容

    response = client.do_action_with_exception(request)
    return json.loads(response)

def word_segment(text):
    content = json.dumps({
        "text":text,
        "lang":"ZH",
        })
    request.set_uri_pattern("/nlp/api/wordsegment/general") #设置所要请求的API路径
    request.set_content(content.encode('utf-8')) # 设置请求内容

    response = client.do_action_with_exception(request)
    return json.loads(response)

def word_pos(text):
    content = json.dumps({
        "text":text,
        })
    request.set_uri_pattern("/nlp/api/wordpos/general") #设置所要请求的API路径
    request.set_content(content.encode('utf-8')) # 设置请求内容

    response = client.do_action_with_exception(request)
    return json.loads(response)

if __name__ == "__main__":
    text = "等会儿四点半开个会"
    res = word_pos(text)
    print(res)