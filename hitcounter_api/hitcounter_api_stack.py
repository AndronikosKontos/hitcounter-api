from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

# We are importing the aws_lambda module as _lambda because lambda is a built-in identifier in Python
# The API Gateway we are deploying proxies all requests to an AWS Lambda function
# To test after deployment use 'curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/'

from .hitcounter import HitCounter

class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda function with the handler from lambda/hello.py (path relative to root directory)
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )

        # Defines an AWS Lambda function which updates the table and invokes the 'my_lambda' function
        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )


        # Defines an API endpoint and associates it with our Lambda function
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )
