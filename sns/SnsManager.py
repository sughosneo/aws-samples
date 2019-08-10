import boto3
from Constant import *

class SnsManager:

    snsClient = None
    topicARN = "arn:aws:sns:ap-south-1:936264745787:ProductInformationTopic"

    def __init__(self):

        try:

            print("trying to initiate the connection with SNS topic !")

            # This is the high level object which actually gets represented by the Boto3 in pretty abstract way.
            # If someone wants to use the low level API like boto3.client they can do that too.
            self.snsClient = boto3.client('sns', region_name=Constant.SNS_DEV_REGION_NAME,
                                      aws_access_key_id=Constant.SNS_DEV_ACCESS_KEY_ID,
                                      aws_secret_access_key=Constant.SNS_DEV_SECRET_ACCESS_KEY)

        except Exception as error:
            print("Connection to SNS topic has been failed !")
            print(error)

    def publishMessageToTopic(self,message):

        print("In publishMessageToTopic() method !")

        try:

            response = self.snsClient.publish(
                TopicArn=self.topicARN,
                Message=message,
            )

            print(response)

        except Exception as error:
            print("Not able to publish the message in the publish !")
            print(error)


if __name__ == '__main__':

    snsManager = SnsManager()
    snsManager.publishMessageToTopic("New product is available! Please purchase !")