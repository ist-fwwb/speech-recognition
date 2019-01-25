# -*- coding: utf-8 -*-

import os
import shutil
import oss2

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'LTAIqMIT5KX4oGAT')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'wYwZdNHrnvAiM9GNddiXqaeHcB4xfz')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'speech')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-cn-hangzhou.aliyuncs.com')

# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

def save_file_to_oss(object_name, file_name):
    bucket.put_object_from_file(object_name, file_name)

def get_file_from_oss(object_name, file_name):
    bucket.get_object_to_file(object_name, file_name)

def delete_local_file(file_name):
    if (os.path.exists(file_name)):
        os.remove(file_name)