import boto3
import json
from Constant import *

class SqsManager:

    sqs = None
    queueName = "ProductInformationMessageQueue.fifo"
    messageGroupId = "api-message-group"

    def __init__(self):

        try:

            print("trying to initiate the SQS resource connection object !")

            # This is the high level object which actually gets represented by the Boto3 in pretty abstract way.
            # If someone wants to use the low level API like boto3.client they can do that too.
            self.sqs = boto3.resource('sqs', region_name=Constant.SQS_DEV_REGION_NAME,
                                      aws_access_key_id=Constant.SQS_DEV_ACCESS_KEY_ID,
                                      aws_secret_access_key=Constant.SQS_DEV_SECRET_ACCESS_KEY)

        except Exception as error:
            print("Connection to message queue has been failed !")
            print(error)

    def writeMessageToQueue(self,message):

        print("In writeMessageToQueue() method !")

        try:

            # Get the queue
            queue = self.sqs.get_queue_by_name(QueueName=self.queueName)

            # Ref : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message
            response = queue.send_message(
                MessageBody=message,
                MessageGroupId=self.messageGroupId
            )

            print(response)

        except Exception as error:
            print("Not able to write the message to queue !")
            print(error)

    def readMessageFromQueue(self):

        print("In readMessageFromQueue() method !")

        try:

            # Get the queue
            queue = self.sqs.get_queue_by_name(QueueName=self.queueName)

            messages = queue.receive_messages()

            for eachMessage in messages:
                print(eachMessage)
                print("Message Got as an action as :: {0}".format(eachMessage.body))

        except Exception as error:
            print("Not able to write the message to queue !")
            print(error)


if __name__ == '__main__':

        queueManager = SqsManager()

        # message formation based on the action
        message = {"action":"GET","api_info":{"name":"product_information_api","url":"http://<dns_name>/develop/v.1.0/product/information","type":"REST"},"data":{"product_id":1}}

        # Write Message
        queueManager.writeMessageToQueue(json.dumps(message))

        # Read Message
        queueManager.readMessageFromQueue()