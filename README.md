# aws-samples (Still under making...)
This repo would actually contains resources which are important for developers who are working on different
AWS services. It would provide simple samples along with few of the tutorial reference.

Before anyone get started they would possibly require one aws free subscription account.

***```AWS Subscription```***
-----------------------------
[1] - Creating account : [https://aws.amazon.com/free/start-your-free-trial/](https://aws.amazon.com/free/start-your-free-trial/)
[2] - Free service details : [https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)

***```Library For AWS```***
--------------------------------
There are plenty of SDK, libraries available to interact with AWS. 
Boto3 - is for python. [https://aws.amazon.com/sdk-for-python/](https://aws.amazon.com/sdk-for-python/)
All the available and supported functions can be found in here - [https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html)
Here are the list of supported SDK(s) - [https://aws.amazon.com/getting-started/tools-sdks/](https://aws.amazon.com/getting-started/tools-sdks/)


***```[Service - 1] IAM```***
---------------------------
- Understanding IAM services : [https://www.youtube.com/watch?v=UqKWHZ36yEM](https://www.youtube.com/watch?v=UqKWHZ36yEM)
- Mastering IAM policies : [https://www.youtube.com/watch?v=YQsK4MtsELU](https://www.youtube.com/watch?v=YQsK4MtsELU)
- Troubleshooting IAM : [https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html)

***```[Service - 2] DynamoDB```*** 
-----------------------------------
As per amazon doc, 
"Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. 
It's a fully managed, multiregion, multimaster, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. DynamoDB can handle more than 10 trillion requests per day 
and can support peaks of more than 20 million requests per second."

- It's a nosql popular database.
- No SQL Database : [https://www.youtube.com/watch?v=ovEq4L6tGfc](https://www.youtube.com/watch?v=ovEq4L6tGfc)
- Understanding Dynamo DB : [https://www.youtube.com/watch?v=tDqLwzQEOmM](https://www.youtube.com/watch?v=tDqLwzQEOmM)
- Tutorials : [https://martinapugliese.github.io/interacting-with-a-dynamodb-via-boto3/](https://martinapugliese.github.io/interacting-with-a-dynamodb-via-boto3/)
- With Boto3 : [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)
- In this sample created 2 table schema "Product" and "ProductCategory" and show case different set of
- For any one to use they would require to put their own "DYNAMO_DB_DEV_ACCESS_KEY_ID" and "DYNAMO_DB_DEV_SECRET_ACCESS_KEY" value.
- Attached are the sample values :

![Product-Table](./images/dynamodb_1.png)
  
![ProductCategoryTable](./images/dynamodb_2.png)


***```[Service - 3] Lambda```*** 
-----------------------------------
- Serverless architecture : https://aws.amazon.com/lambda/serverless-architectures-learn-more/
- AWS Lambda is one of the implementation of serverless framework.
- Lambda Supported Runtimes : https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
- Function should be called with "lambda_function.lambda_handler"
- [Lambda - Tutorial] - [https://aws.amazon.com/lambda/](https://aws.amazon.com/lambda/)
- [Lambda reference doc] - [https://docs.aws.amazon.com/lambda/latest/dg/welcome.html](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Ref] - [https://www.youtube.com/watch?v=XZggsCITQdY](https://www.youtube.com/watch?v=XZggsCITQdY)
 

![Lambda-Function](./images/lambda_1.png)

![Lambda-Function](./images/lambda_2.png)

![Lambda-Code](./images/lambda_3.png)

![Lambda-Configure-Test-Event](./images/lambda_4.png)

![Lambda-Call-Monitoring-Dashboard](./images/lambda_5.png)

- We can configure different trigger with any lambda function 
- Below are the lambda function configuration with sample code and other details.

![Lambda-Trigger](./images/lambda_8.png)

![Lambda-Designer](./images/lambda_7.png)

![Lambda-Designer](./images/lambda_9.png)


***```[Service - 4] API Gateway```*** 
-----------------------------------
- Below example shows how it can function API can be further configured and respective methods can be enabled on that.

- Configuring one "product information" API 

![Configured Production Information API](./images/api_gateway_2.png)

- Particularly configuring one "POST" method one REST API.

![Configured Production Information API](./images/api_gateway_6.png)

- Seeing the response of any API test call with proper tracing.

![Configured Production Information API](./images/api_gateway_4.png)

- Seeing the response of any API test call with proper tracing.

![Configured Production Information API](./images/api_gateway_5.png)

- Enabling API key for a rest API.

![Configured Production Information API](./images/api_gateway_7.png)

- We would also keep it in mind every time we make any changes in the API configurations we would require to deploy the API in respective staging environment.
  Be it's ***develop/qa/uat/prod***. But we can figure that out from the staging configurations.
  
![Configured Production Information API](./images/api_gateway_11.png)   

- We would also require to set up the usage plan for individual stage and API.
- API key enablement is not enough we would require to map that against individual API level.
- Where we have options to put granular number of throttling and quotas (Could be helpful based on the subscription plan)

![Configured Production Information API](./images/api_gateway_10.png)

![Configured Production Information API](./images/api_gateway_8.png)

- After successful configuration we should be able to call the API with proper "x-api-key" as header token.

![Configured Production Information API](./images/api_gateway_9.png)

- For monitoring purpose user can also enable logging for each staging environment level.
- For each aws API services we could separately set up log/tracing. That's actually a better way of looking at it. 
  But in this scenario we could actually see the recent call with the lamnda logs itself. We could follow along with the same request correlation id everywhere. 
  
![Configured Production Information API](./images/api_gateway_12.png)

- We could also export the definition of specific API. AWS api gateway follow [Swagger](https://swagger.io/) API definitions.
- So after setting up the API through console we should be able to download the API definition as json or YAML format for future reference.
- Samples have been attached under api-gateway directory.

```References```
 
API Gateway [https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

API Gateway Tutorial : [https://www.youtube.com/watch?v=XwfpPEFHKtQ](https://www.youtube.com/watch?v=XwfpPEFHKtQ)

API Gateway With Lambda : [https://www.youtube.com/watch?v=ceVgLVXM-fs](https://www.youtube.com/watch?v=ceVgLVXM-fs)

Enabling API Key : [https://www.youtube.com/watch?v=7C3-Nf-2dS8](https://www.youtube.com/watch?v=7C3-Nf-2dS8)


***```[Service - 5] CloudWatch Log```*** 
-----------------------------------

- Cloudwatch is self-managed service which helps to monitor and manage the logging or tracingon different services.
- CloudWatch helps to configure different logging stream on all the aws services.

- [Cloud Watch Reference] : [https://aws.amazon.com/cloudwatch/features/](https://aws.amazon.com/cloudwatch/features/) 

- Below example shows how can different aws services leverage Cloud Watch service to let the user trace any request.  
 
![Cloud Watch - Logs](./images/cloud_watch_0.png)

![Cloud Watch - Logs](./images/cloud_watch_1.png)

![Cloud Watch - Detail Specific Log Stream](./images/cloud_watch_2.png)


***```[Service - 6] Cloud9 IDE```*** 
-----------------------------------

