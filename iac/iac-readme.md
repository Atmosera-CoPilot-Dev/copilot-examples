
# Infrastructure as Code

This is an example of building some boilerplate infrastructure as code using Docker to wrap a Python Flask hello world app. It should run on port 5001.
A very simple prompt will get use the basic files we need:

```
please generate me template of starter files that is a python flask application and wraps the application in a docker application.
```

## Bonus prompt

It out of scope to do a deploy of this app, but Copilot will generate other IaC such as Terraform. For example:

```
generate terraform to deploy this to Azure K8s
```

# Pre-requisites

## Install Docker

### macOS

```
brew install docker
```

### Windows

```
choco install docker-desktop
```

## Install Python Modules

```
pip install -r requirements.txt
```

# Build and run Docker container

```
docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app
```

## Open the app in a browser

```
http://localhost:5000
```

## Results

### Build Console Output

If you the build worked it will look like this:

<details>
  <summary>Click to expand!</summary>

```
iac % docker build -t my-flask-app .      
[+] Building 2.2s (9/9) FINISHED                                                                                                               docker:desktop-linux
 => [internal] load .dockerignore                                                                                                                              0.0s
 => => transferring context: 106B                                                                                                                              0.0s
 => [internal] load build definition from Dockerfile                                                                                                           0.0s
 => => transferring dockerfile: 552B                                                                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim-buster                                                                                      0.2s
 => [1/4] FROM docker.io/library/python:3.9-slim-buster@sha256:320a7a4250aba4249f458872adecf92eea88dc6abd2d76dc5c0f01cac9b53990                                0.0s
 => [internal] load build context                                                                                                                              0.0s
 => => transferring context: 1.47kB                                                                                                                            0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                                  0.0s
 => [3/4] ADD . /app                                                                                                                                           0.0s
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt                                                                                                   1.8s
 => exporting to image                                                                                                                                         0.1s
 => => exporting layers                                                                                                                                        0.1s
 => => writing image sha256:bacea39869e088affb0c6892fbcd00d5b3892e77b57f2788d205a19d570d7d4b                                                                   0.0s
 => => naming to docker.io/library/my-flask-app                                                                                                                0.0s

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
```

</details>

 ### Run Console Output

If you the run worked it will look like this:

<details>
  <summary>Click to expand!</summary>

```
iac % docker run -p 5001:5001 my-flask-app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5001/ (Press CTRL+C to quit)
192.168.65.1 - - [12/Dec/2023 16:51:26] "GET / HTTP/1.1" 200 -
192.168.65.1 - - [12/Dec/2023 16:51:26] "GET /favicon.ico HTTP/1.1" 404 -

```

</details>

# Troubleshooting

## Port in use

If you get an error like this:

```
docker: Error response from
daemon: driver failed programming external connectivity on endpoint
```

Then you may have another process running on port 5000. You can check this with:

```
lsof -i :5000
```

If you see a process running on port 5000, you can kill it with:

```
kill -9 <PID>
```

## Old dependencies

Out of the box you may get an error installing the requirements. This is typically because the LLM is behind on more recent dependency versions. In these cases use the latest versions and/or feed the error to Copilot to help you resolve it.

For example, out of the box when running the application in Docker we get this error:

```
iac % docker run -p 5001:5001 my-flask-app
Traceback (most recent call last):
  File "/app/app.py", line 1, in <module>
    from flask import Flask
  File "/usr/local/lib/python3.9/site-packages/flask/__init__.py", line 7, in <module>
    from .app import Flask as Flask
  File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 28, in <module>
    from . import cli
  File "/usr/local/lib/python3.9/site-packages/flask/cli.py", line 18, in <module>
    from .helpers import get_debug_flag
  File "/usr/local/lib/python3.9/site-packages/flask/helpers.py", line 16, in <module>
    from werkzeug.urls import url_quote
ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (/usr/local/lib/python3.9/site-packages/werkzeug/urls.py)
```

The fix is to update the requirements.txt file to use the latest version of Werkzeug:

```
Werkzeug==2.0.2
```


## Hello World not working but Docker run is successful

If the default IP/port does not work, just try to visit `http://localhost:5001/`