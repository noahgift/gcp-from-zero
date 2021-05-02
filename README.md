[![Python application test with Github Actions](https://github.com/noahgift/gcp-from-zero/actions/workflows/python-publish.yml/badge.svg)](https://github.com/noahgift/gcp-from-zero/actions/workflows/python-publish.yml)

# gcp-from-zero
This is a new repo


## First thing to do is DevOps Workflow

* Get SSH-Keys setup in a Cloud Environment

`ssh-keygen -t rsa`

Give github this content: `cat /home/ec2-user/.ssh/id_rsa.pub`

Then checkout the code.
* Python Scaffold

1. Create virtualenv

`virtualenv ~/.gcp-from-zero`

2.  Source it

`source ~/.gcp-from-zero/bin/activate`


* Setup Continuous Integration

## To integrate Cloud Build instead of Github Actions

Example here:  [cloudbuild.yaml](https://github.com/noahgift/gcp-from-zero/blob/main/cloudbuild.yaml)

```
steps:
- name: python:3.7
  id: INSTALL
  entrypoint: python3
  args:
  - '-m'
  - 'pip'
  - 'install'
  - '-t'
  - '.'
  - '-r'
  - 'requirements.txt'
- name: python:3.7
  entrypoint: ./pylint_runner
  id: LINT
  waitFor:
  - INSTALL
- name: "gcr.io/cloud-builders/gcloud"
  args: ["app", "deploy"]
timeout: "1600s"
images: ['gcr.io/$PROJECT_ID/pylint']
```
