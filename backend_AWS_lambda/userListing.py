# ========================= User Listing ========================

# Return the records of all user in the CBUser table

# ===============================================================

import json
import boto3

def lambda_handler(event, context):
    
    db = boto3.resource('dynamodb')
    request_table = db.Table('CBUser')

    id = '0'
    
    if event['httpMethod'] == 'GET':
        all_users = request_table.scan()
        return (all_users['Items'])

# ===============================================================


# ======================== Mapping Template =====================

'''
GET
{
    "httpMethod": "$context.httpMethod"
}
'''

# ===============================================================
