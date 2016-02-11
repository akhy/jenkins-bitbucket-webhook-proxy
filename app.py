from flask import Flask
from flask import request
from flask import make_response
from unirest import post

app = Flask(__name__)

@app.route('/build', methods = ['GET', 'POST'])
def build():
  jenkins = request.args.get('jenkins')
  jenkins = jenkins if jenkins.startswith('http://') or jenkins.startswith('https://') else 'http://%s' % jenkins
  jenkins = jenkins[:-1] if jenkins.endswith('/') else jenkins
  job = request.args.get('job')
  token = request.args.get('token', None)
  query = '' if token is None else 'token=%s' % token

  json = request.json
  git_hash = json['push']['changes'][0]['new']['target']['hash']
  print git_hash

  # forward the request
  jenkins_url = '%s/job/%s/buildWithParameters?%s' % (jenkins, job, query)
  response = post(jenkins_url, params = { 'GIT_HASH': git_hash })

  if (response.code in range(400, 500)):
    return "Request error"
  elif (response.code >= 500):
    return "Server error"
  else:
    return make_response(response.raw_body, response.code, {})

if __name__ == '__main__':
    app.run()
