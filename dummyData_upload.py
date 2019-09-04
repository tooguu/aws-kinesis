# coding: utf-8

import sys
import random
import time
import json
import boto3

client = boto3.client('kinesis')

def dummy_data():
    BaseTmp = 20
    dummyTmp = BaseTmp + random.randint(-5,5)

    return dummyTmp

def put_kinesis(json):
    try:
        res = client.put_record(
            StreamName = 'tuenotest',
            Data = json,
            PartitionKey = 'test'
        )
        print res

    except Exception as e:
       print 'Kinesis put record excption'
       print e.message
       sys.exit

print '----------start-------------'
for i in range(200):
    try:
         #fake data
         dummy = {}
         dummy['ID'] = i
         dummy['Tmp'] = dummy_data()
         dummy['TimeStamp'] = int(round(time.time()*1000))
         put_kinesis(json.dumps(dummy))

         #time.sleep(1)


    except Exception as e:
        print 'Exception exit'
        print e.message
        sys.exit
