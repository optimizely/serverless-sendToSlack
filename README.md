Serverless: https://serverless.com/framework/docs/providers/aws/guide/installation/

## Specifying an S3 Bucket
It is recommended that you setup a specific bucket in S3 for Serverless to keep the Cloudformation templates in. This will need to be set in your `serverless.yml` file, and must be unique. If you choose not to set a specific bucket (by removing the `deploymentBucket` key), a new one will be created on every deploy.

## Vendoring Dependencies

To install python package dependencies (`requirements.txt`) use the included
`build.sh` script:
```console
$ ./build.sh
```

This runs an `amazonlinux` docker container, matching the environment of AWS
Lambda, ensuring dependencies are compiled to the correct OS.

These dependencies won't work when invoking the function locally if you're
developing on OSX. In that case you should create a virtualenv and install the
dependencies manually:

```console
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Deployment

Start by (Vendoring Dependencies)[#vendoring-dependencies], then install
serverless:
```console
$ npm install -g serverless
```

Deploy the function with:
```console
$ serverless deploy
```
