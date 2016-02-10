# Jenkins Bitbucket Webhook Proxy

A proxy that transforms Bitbucket webhook calls to a format that can trigger Jenkins parameterized builds.

## Why?

1. Bitbucket's webhook can only post **JSON** requests
2. **Change details** (e.g. commit author, commit SHA, etc) of Bitbucket's webhook calls is located **in the request body**
3. Jenkins' remotely triggered jobs (via webhook) **cannot inspect the request body**
4. We need commit details from webhook to be **available as build parameters** in Jenkins jobs
  - so we can checkout and build **only those specific commits**
