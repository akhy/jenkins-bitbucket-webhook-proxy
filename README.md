# Jenkins Bitbucket Webhook Proxy

[![](https://badge.imagelayers.io/akhy/jenkins-bitbucket-webhook-proxy:latest.svg)](https://imagelayers.io/?images=akhy/jenkins-bitbucket-webhook-proxy:latest 'Get your own badge on imagelayers.io')

A proxy that transforms Bitbucket webhook calls to a format that can trigger Jenkins parameterized builds.

## Why?

1. Bitbucket's webhook can only post **JSON** requests
2. **Change details** (e.g. commit author, commit SHA, etc) of Bitbucket's webhook calls is located **in the request body**
3. Jenkins' remotely triggered jobs (via webhook) **cannot inspect the request body**
4. We need commit details from webhook to be **available as build parameters** in Jenkins jobs
    - so we can checkout and build **only those specific commits**

## Setup

### 1. Run the proxy

There are two methods to run it.

#### Running the script with Python

It requires Python 2.7 and preferably isolated environment (e.g. virtualenv).

```
git clone https://github.com/akhyrul/jenkins-bitbucket-webhook-proxy webhook-proxy
cd webhook-proxy
pip install -r requirements.txt
python app.py
```

#### Running with Docker

```
docker run -p 5000:5000 -i -t akhy/jenkins-bitbucket-webhook-proxy
```

### 2. Setting up Bitbucket and Jenkins

#### Jenkins side

1. Open up your job configuration
2. Check **"This build is parameterized"** and add a string parameter named **"GIT_HASH"**. This parameter will be provided by our proxy app from Bitbucket webhook.
3. In build triggers section check **Trigger builds remotely** and enter any random authentication token. This token will be used in the next Bitbucket configuration.
4. Make sure in source code management section, you choose Git. Set **branches to build** to **${GIT_HASH}**

#### Bitbucket side

Create a webhook with **repository push** trigger and this URL template:

> http://**myproxy.tld:5000**/build?jenkins=**https://jenkins.mycompany.com:8080**&job=**job**&token=**token**

- **myproxy.tld:5000** is where your proxy is listening
- **jenkins** query param is your Jenkins URL
- **job** query param is the Jenkins job's name (see the URL when you're editing the job)
- **token** query param is the token you have set in the Jenkins job before

Note: Currently the proxy can only handle repository push trigger.

## TODOs

- Handle more Bitbucket webhook triggers
- Tests
