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
