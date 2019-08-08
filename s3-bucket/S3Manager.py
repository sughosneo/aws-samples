import boto3
from Constant import *

class S3Manager:

    def __init__(self):

        try:

            print("trying to initiate the S3 resource connection object !")

            # This is the high level object which actually gets represented by the Boto3 in pretty abstract way.
            # If someone wants to use the low level API like boto3.client they can do that too.
            self.s3_resource = boto3.resource('s3', region_name=Constant.S3_BUCKET_REGION_NAME,
                                           aws_access_key_id=Constant.S3_DEV_ACCESS_KEY_ID,
                                           aws_secret_access_key=Constant.S3_DEV_SECRET_ACCESS_KEY)

        except Exception as error:
            print("Connection to S3 has been failed !")
            print(error)


    def listS3BucketContent(self):

        print("In listS3BucketContent() method !")

        try:

            s3_bucket = self.s3_resource.Bucket(Constant.S3_BUCKET_NAME)
            for file in s3_bucket.objects.all():
                print(file.key)

        except Exception as error:
            print("Not able to list S3 bucket item !")
            print(error)


    def readS3Content(self):
        pass

    def writeContentS3(self):
        pass

if __name__ == '__main__':

    manager = S3Manager()
    manager.listS3BucketContent()
