# -*- coding=utf-8

import oss2
from config import *
import os
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import logging


def upload(directory):
    if not directory:
        return

    files_info = os.walk(directory)

    for path, dirs, names in files_info:
        if names:
            for filename in names:
                if filename.startswith('.'):
                    continue

                local_path = os.path.join(path, filename).lstrip()
                remote_key = os.path.join(path[(path.find('/') + 1):], filename)

                logging.info("Uploading %s --> %s" % (local_path, remote_key))

                if UPLOAD_METHOD == 'oss':
                    upload_by_oss(remote_key, local_path)
                elif UPLOAD_METHOD == 'cos':
                    upload_by_cos(remote_key, local_path)


def upload_by_cos(remote_key, local_path):
    config = CosConfig(Region=COS_REGION, SecretId=COS_SECRET_ID, SecretKey=COS_SECRET_KEY)  # 获取配置对象
    client = CosS3Client(config)

    if client.object_exists(COS_BUCKET_NAME, remote_key):
        logging.info('File exist (@-@)')
    else:
        client.put_object_from_local_file(
            Bucket=COS_BUCKET_NAME,
            LocalFilePath=local_path,
            Key=remote_key,
        )


def upload_by_oss(remote_key, local_path):
    auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
    bucket = oss2.Bucket(auth, OSS_URL, OSS_BUCKET_NAME)

    if bucket.object_exists(remote_key):
        logging.info('File exist (@-@)')
    else:
        bucket.put_object_from_file(remote_key, local_path)
        logging.info('Upload success (^_^)')
