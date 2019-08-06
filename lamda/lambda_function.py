import json
import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from Constant import *


class ProductInfo:
    dynamodb = None

    def __init__(self):

        try:

            print("trying to initiate the dynamoDB object !")

            # This is the high level object which actually gets represented by the Boto3 in pretty abstract way.
            # If someone wants to use the low level API like boto3.client they can do that too.
            self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1',
                                           aws_access_key_id=Constant.DYNAMO_DB_DEV_ACCESS_KEY_ID,
                                           aws_secret_access_key=Constant.DYNAMO_DB_DEV_SECRET_ACCESS_KEY)

        except Exception as error:
            print("Connection to Dynamo DB has been failed !")
            raise error

    def getSpecificProductInformation(self, keyValue):

        print("In getSpecificProductInformation() method !")

        try:

            table = self.dynamodb.Table('Product')
            resp = table.get_item(Key=keyValue)

            # resp returns following value.
            print(resp)
            # {'Item': {'Id': Decimal('1'), 'ProductCategoryId': Decimal('1'), 'Name': 'IPhone 8\n'}, 'ResponseMetadata': {'RequestId': 'NMDA30M1HHF514MJVVUIBCELEFVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Mon, 05 Aug 2019 17:12:19 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '81', 'connection': 'keep-alive', 'x-amzn-requestid': 'NMDA30M1HHF514MJVVUIBCELEFVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '3394591035'}, 'RetryAttempts': 0}}

            if resp and resp["ResponseMetadata"]["HTTPStatusCode"] == 200:

                deserializer = TypeDeserializer()
                serializer = TypeSerializer()

                if resp["Item"]:
                    print(resp["Item"])
                    # {'Id': Decimal('1'), 'ProductCategoryId': Decimal('1'), 'Name': 'IPhone 8\n'}
                    data = {k: serializer.serialize(v) for k, v in resp["Item"].items()}

                else:
                    data = {}

                return data
            else:
                raise Exception

        except Exception as error:
            print("Not able to fetch item !")
            raise error

'''
    This is the actual driver function which would gets called 
    during the actual lambda execution. It has respective event and context.
    In this scenario event is nothing but input parameter request.
    {
        "product_id" : 1
    }
'''
def lambda_handler(event, context):
    try:

        productInfo = ProductInfo()
        productInformation = productInfo.getSpecificProductInformation({"Id": event["product_id"]})

        return {
            'statusCode': 200,
            'body': json.dumps(productInformation)
        }

    except Exception as error:
        print(error)
        return {
            'statusCode': 500,
            'body': "Not able to fetch product information"
        }