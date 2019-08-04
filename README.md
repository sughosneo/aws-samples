# aws-samples (Still under making...)
This repo would actually contains resources which are important for developers who are working on different
AWS services. It would provide simple samples along with few of the tutorial reference.

Before anyone get started they would possibly require one aws free subscription account.

***```AWS Subscription```***
-----------------------------
[1] - Creating account : https://aws.amazon.com/free/start-your-free-trial/
[2] - Free service details : https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc

***```Library For AWS```***
--------------------------------
There are plenty of SDK, libraries available to interact with AWS. 
Boto3 - is for python. https://aws.amazon.com/sdk-for-python/
All the available and supported functions can be found in here - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
Here are the list of supported SDK(s) - https://aws.amazon.com/getting-started/tools-sdks/


***```[Service - 1] IAM```***
---------------------------


***```[Service - 2] DynamoDB```*** 
-----------------------------------
As per amazon doc, 
"Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. 
It's a fully managed, multiregion, multimaster, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. DynamoDB can handle more than 10 trillion requests per day 
and can support peaks of more than 20 million requests per second."

- It's a nosql popular database.
- No SQL Database : https://www.youtube.com/watch?v=ovEq4L6tGfc
- https://www.youtube.com/watch?v=tDqLwzQEOmM
- Tutorials :
- https://martinapugliese.github.io/interacting-with-a-dynamodb-via-boto3/ 
- With Boto3 : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html 
- In this sample created 2 table schema "Product" and "ProductCategory" and show case different set of
- For any one to use they would require to put their own "DYNAMO_DB_DEV_ACCESS_KEY_ID" and "DYNAMO_DB_DEV_SECRET_ACCESS_KEY" value.
- Attached are the sample values :

![Product-Table](./images/dynamodb_1.png)
  
![ProductCategoryTable](./images/dynamodb_2.png)


***```[Service - 2] Cloud9 IDE```*** 
-----------------------------------

