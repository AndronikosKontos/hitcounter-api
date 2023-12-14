# Introduction
This repository creates a simple hit counter, which counts the requests that are sent to a specific URL and saves the number to a DynamoDB table.

It uses AWS CDK with Python to deploy two AWS Lambda functions, an API gateway and a DynamoDB table.

The 'simple-response' branch contains a simpler version, with only one AWS Lambda function and not a DynamoDB table.

# Architecture
This diagram shows the simple version. An API gateway proxies the requests to an AWS Lambda function which returns a simple message.

![Alt text](./hello-arch.png?raw=true "Title")

This diagram shows that the API gateway first invokes the hit-counter AWS Lambda function which executes two tasks. 1) It updates a DynamoDB table with the new hit of the URL 2) It invokes the Lambda function from before.

![Alt text](./hit-counter.png?raw=true "Title")

# Usage
After initialization, use the command 'cdk deploy' to deploy the stack to your AWS account.

The API gateway will create a URL for your application. To test it you can either use a browser or a client like **curl**.

e.g curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/

# Project Init

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```
