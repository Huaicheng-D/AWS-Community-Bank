import json
import boto3

# =============== User Request Handler =============== #
#                                                      #
# 1. Display posted requests for specific userid (GET) #
# 2. Create user records with user's information (POST)#
#                                                      #
#======================================================#

def lambda_handler(event, context):

    db = boto3.resource('dynamodb')
    request_table = db.Table('CBUser')

    if event['httpMethod'] == 'GET':
        id = event['queryStringParameters']['id']
        item = request_table.get_item(Key={
            'id': id
            })
        if item != None:
            return item['Item']
        
    elif event['httpMethod'] == 'POST':
        request_table.put_item(Item=event['body'])
        return(event['body'])

# ===================================================== #

# =============== Mapping Template ====================
#
# Content-type: application/json
'''
 GET:
 {
    "queryStringParameters": {
        "id": "$input.params('id')"

    },
    "httpMethod": "$context.httpMethod"
 }

 POST:
 {
    "body" : $input.json('$'),
    "httpMethod": "$context.httpMethod"
 }
'''
# ======================================================
