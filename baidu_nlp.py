# -*- coding: gbk -*-
import json
import requests

access_token_headers = {'Content-Type': 'application/json; charset=UTF-8'}
ak = 'X1bclMZIYWTYE1SHPZyGU6Pm'
sk = 'SyEAFM243BAik2aGzoc9vS4h7Hl9bdrO'
access_token_params = {'grant_type':'client_credentials', 'client_id':ak, 'client_secret':sk}
access_token_host = 'https://aip.baidubce.com/oauth/2.0/token'

def get_access_token():
    r = requests.get(access_token_host, headers=access_token_headers, params=access_token_params)
    res = r.json()
    return str(res["access_token"])

word_segment_host = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer'
word_segment_headers = {'Content-Type': 'application/json'}
def word_segment(text):
    print(text)
    gbk_text = text.decode('utf-8').encode('gbk')
    print(gbk_text)
    at = get_access_token()
    word_segment_params = {'access_token': at}
    word_segment_data = {'text': gbk_text}
    print(word_segment_data)
    print(word_segment_headers)
    print(word_segment_host)
    print(word_segment_params)
    #r = requests.post(word_segment_host, headers=word_segment_headers, params=word_segment_params, data=word_segment_data)
    #res = r.json()
    #return res