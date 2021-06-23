# Python Http Cloud Functions Hello World

A hello world project, for Python Http Cloud Functions

**Source :** https://codelabs.developers.google.com/codelabs/cloud-functions-python-http

## Local environment

Run this app locally by creating an HTTP server using Flask

```
$ python3 -m flask run --port 8080
```

### Call functions

```
$ curl -w "\n" http://127.0.0.1:8080/

$ curl -w "\n" http://127.0.0.1:8080/hello?name=Lucas

$ curl -w "\n" http://127.0.0.1:8080/powered-by
```

## Google Cloud environment

Run this app in the cloud using Google Cloud Functions

### Set GCP project

```
$ gcloud projects list
$ gcloud config set project <your-project-id>
```

### Enable cloud functions

```
$ gcloud services enable cloudfunctions.googleapis.com cloudbuild.googleapis.com
```
 
### Unit test Cloud Functions

Run from `functions` directory

```
$ python3 -m unittest
```
 
### Deploy function

Run from `functions` directory

```
$ gcloud functions deploy hello_world --runtime python39 --trigger-http --allow-unauthenticated
```

### Call functions

```
$ curl -w "\n" $(gcloud functions describe hello_world --format "value(httpsTrigger.url)")

$ curl -w "\n" $(gcloud functions describe hello_name --format "value(httpsTrigger.url)")?name=Lucas

$ curl -w "\n" $(gcloud functions describe python_powered --format "value(httpsTrigger.url)")
```

### Delete functions

```
$ gcloud functions delete hello_world --quiet

$ gcloud functions delete hello_name --quiet

$ gcloud functions delete python_powered --quiet
```
