# Jenkins Bitbucket Webhook Proxy

[![](https://badge.imagelayers.io/akhy/jenkins-bitbucket-webhook-proxy:latest.svg)](https://imagelayers.io/?images=akhy/jenkins-bitbucket-webhook-proxy:latest 'Get your own badge on imagelayers.io')

A proxy that transforms Bitbucket webhook calls to a format that can trigger Jenkins parameterized builds.

## Why?

1. Bitbucket's webhook can only post **JSON** requests
2. **Change details** (e.g. commit author, commit SHA, etc) of Bitbucket's webhook calls is located **in the request body**
3. Jenkins' remotely triggered jobs (via webhook) **cannot inspect the request body**
4. We need commit details from webhook to be **available as build parameters** in Jenkins jobs
  - so we can checkout and build **only those specific commits**

## Running the Proxy

### Running Flask directly

WIP

### Running via Docker

WIP

## Setting up Bitbucket and Jenkins

WIP
