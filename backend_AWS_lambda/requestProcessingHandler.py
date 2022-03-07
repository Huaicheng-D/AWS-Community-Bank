# ======================= Request Processing Handler =======================
#
# Returns HTTP Response based on types of requests
#
# GET: Returns the details of an item that user choosed to view
#
# POST: When the user creates a new request post, this function gets the parameters
#       and insert as record into the database
#
# DELETE: Delete the item from the database with corresponding item id

# ==========================================================================

import json
import uuid
import boto3

def lambda_handler(event, context):
    # Process the incoming user interaction based on different HTTP request method
    
    db = boto3.resource('dynamodb')
    list = db.Table('Listing')
    
    if event['httpMethod'] == 'GET':
        # When the user wants to view information of a specific request
        # this function returns the information of that item in JSON format
        id = event['id']
        view_request = list.get_item(Key={
            'id': id
        })
        return view_request['Item']
    
    elif event['httpMethod'] == 'POST':
        # When the user creates the new request post, this function gets the parameters to insert into the database
        body = event['body']
        #id = body['id']

        uuid_id = str(uuid.uuid4())

        purchase_amount = body['purchase_amount']
        item_name = body['item_name']       
        transaction_description = body['transaction_description']
        item_description = body['item_description']
        date_published = body['date_published']
        
        #purchaser_id = body['purchaser_id']
        #status = body['status']
        #lister_id = body['lister_id']
        
        response = list.put_item(
            Item={
                'id': uuid_id,
                'date_published': date_published,
                'item_description': item_description,
                'item_name': item_name,
                'purchase_amount': purchase_amount,
                'transaction_description': transaction_description,
                'purchaser_id': '0',
                'lister_id': '0',
                'status': 'ACTIVE',
            })
        return ({
                'id': uuid_id,
                'date_published': date_published,
                'item_description': item_description,
                'item_name': item_name,
                'transaction_description': transaction_description,
                'purchase_amount': purchase_amount,
                'purchaser_id': '0',
                'lister_id': '0',
                'status': 'ACTIVE',})
    
    elif event['httpMethod'] == 'DELETE':
        # Delete the specific request that the user wants to delete
        # Remove it from the database
        # *** Should it return the list of all items in the database?
        id = event['id']
        view_request = list.get_item(Key={
            'id': id
        })
        if ('Item' not in view_request):
            return {
                'error': json.dumps('No listing was found with id='+ id)
            }

        response = list.delete_item(
            Key={
                'id': id
            }
        )
        return {
            'success': json.dumps('listing id='+ id + ' was successfully deleted')
        }

# ==========================================================================


# ============================ Mapping Template ============================

# Content-type: application/json

'''
GET
{
    "id": "$input.params('id')",
    "httpMethod": "$context.httpMethod"
}


POST
{
    "body" : $input.json('$'),
    "httpMethod": "$context.httpMethod"
}

DELETE
{
    "id": "$input.params('id')",
    "httpMethod": "$context.httpMethod"
}

'''

# ==========================================================================
