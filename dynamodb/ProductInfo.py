import boto3
from boto3.dynamodb.conditions import Key
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
            print(error)

    def getSpecificProductInformation(self,keyValue):

        print("In getSpecificProductInformation() method !")

        try:

            table = self.dynamodb.Table('Product')
            resp = table.get_item(Key=keyValue)

            # resp returns following value.
            print(resp)
            # {'Item': {'Id': Decimal('1'), 'ProductCategoryId': Decimal('1'), 'Name': 'IPhone 8\n'}, 'ResponseMetadata': {'RequestId': '358GVSU2ECQI3BNVFSV3OVL2SNVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Sun, 04 Aug 2019 10:35:27 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '81', 'connection': 'keep-alive', 'x-amzn-requestid': '358GVSU2ECQI3BNVFSV3OVL2SNVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '3394591035'}, 'RetryAttempts': 0}}

            if resp and resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print(resp["Item"])
            else:
                raise Exception

        except Exception as error:
            print("Not able to fetch item !")
            print(error)

    '''
        This is another way to show how we can directy query the dynamodb table using key condition.
    '''
    def getSpecificProductCategoryInformation(self,productCategoryId):

        print("In getSpecificProductCategoryInformation() method !")

        try:

            table = self.dynamodb.Table('ProductCategory')
            resp = table.query(KeyConditionExpression=Key('Id').eq(productCategoryId))

            print(resp)
            # {'Items': [{'Id': Decimal('1'), 'Name': 'Mobile'}], 'Count': 1, 'ScannedCount': 1, 'ResponseMetadata': {'RequestId': '7BTH1IP26CAI2FG2QTJAAO2IFRVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Sun, 04 Aug 2019 11:09:43 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '77', 'connection': 'keep-alive', 'x-amzn-requestid': '7BTH1IP26CAI2FG2QTJAAO2IFRVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '3260165158'}, 'RetryAttempts': 0}}

            if resp and resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
                for item in resp['Items']:
                    print(item)
            else:
                raise Exception

        except Exception as error:
            print("Not able to fetch item !")
            print(error)


    def getAllProductInformation(self):

        print("In getAllProductInformation() method !")

        try:

            table = self.dynamodb.Table('Product')
            resp = table.scan()

            # resp returns following value.
            print(resp)
            # {'Items': [{'Id': Decimal('3'), 'ProductCategoryId': Decimal('2'), 'Name': 'Lenevo'}, {'Id': Decimal('2'), 'ProductCategoryId': Decimal('1'), 'Name': 'Motorola'}, {'Id': Decimal('4'), 'ProductCategoryId': Decimal('2'), 'Name': 'HP'}, {'Id': Decimal('1'), 'ProductCategoryId': Decimal('1'), 'Name': 'IPhone 8\n'}], 'Count': 4, 'ScannedCount': 4, 'ResponseMetadata': {'RequestId': 'CVV755AER658UI1OR1P6KDF67JVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Sun, 04 Aug 2019 11:02:59 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '316', 'connection': 'keep-alive', 'x-amzn-requestid': 'CVV755AER658UI1OR1P6KDF67JVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '455596218'}, 'RetryAttempts': 0}}

            if resp and resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print(resp["Items"])
            else:
                raise Exception

        except Exception as error:
            print("Not able to fetch item !")
            print(error)

    def insertMultipleProductSchema(self,itemDictList):

        print("In insertMultipleProductInformation() method !")

        try:

            table = self.dynamodb.Table('Product')

            with table.batch_writer() as batch:

                for eachItem in itemDictList:
                    batch.put_item(Item=eachItem)

            return "success"

        except Exception as error:
            print(error)
            return "failed"

    def deleteMultipleItemsFromProductSchema(self,keyValueDictList):

        print("In deleteItemsFromProductSchema() method !")

        try:

            table = self.dynamodb.Table('Product')

            with table.batch_writer() as batch:

                for eachKeyItem in keyValueDictList:
                    batch.delete_item(Key=eachKeyItem)

            return "success"

        except Exception as error:
            print(error)
            return "failed"

if __name__ == '__main__':

    productInfo = ProductInfo()

    # Delete multiple items from the existing table
    keyValueDictList = [
        {"Id":5},
        {"Id":6}
    ]
    print(productInfo.deleteMultipleItemsFromProductSchema(keyValueDictList))

    # Get specific product information
    productInfo.getSpecificProductInformation({"Id"})

    # Get specific product category information
    # Need to notice how response gets changed based on passed params.
    productInfo.getSpecificProductCategoryInformation(1)

    # Get all product information
    productInfo.getAllProductInformation()

    # Insert items in product schema
    productItemDictList = [
        {"Id":5,"Name": "Samsung", "ProductCategoryId":1},
        {"Id":6, "Name": "Dell", "ProductCategoryId": 2}
    ]

    print(productInfo.insertMultipleProductSchema(productItemDictList))

    # Again all product information
    productInfo.getAllProductInformation()