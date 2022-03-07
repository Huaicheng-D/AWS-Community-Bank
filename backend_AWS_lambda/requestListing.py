# =================== RequestListing ===================

# Return a HTTP Response where the body contains a key-value pair

# 'body' : { 'Items': [dictionaries of records] }

# ======================================================

import json
import boto3

def lambda_handler(event, context):

    db = boto3.resource('dynamodb')
    list = db.Table('Listing')
    
    if event['httpMethod'] == 'GET':
        all_requests = list.scan()
        return {
            'statusCode': 200, 
            'body': all_requests['Items']
        }

# =======================================================


# ================== Mapping Template ===================

# Content-type: application/type

'''
{
    "httpMethod": "$context.httpMethod"
}
'''

# =======================================================
