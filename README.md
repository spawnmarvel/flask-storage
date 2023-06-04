# Azure storage monitoring and more with Flask and Azure SDK

## Flask Docs

https://tedboy.github.io/flask/index.html

## Flask tutorialspoint

https://www.tutorialspoint.com/flask/flask_application.htm

## Microsoft Python SDK

https://learn.microsoft.com/en-us/python/api/overview/azure/storage?view=azure-python

* Blobs
* File shares
* File shares Data Lake
* Queues
* Tables


## Lower level: virtualenv

https://docs.python-guide.org/dev/virtualenvs/

```
// Install virtualenv via pip:
pip install virtualenv

// Test your installation:
virtualenv --version

// Basic Usage
cd flask-storage
flask-storage>virtualenv venv

// virtualenv venv will create a folder in the current directory which will contain the Python executable files, 
// and a copy of the pip library which you can use to install other packages. 
// The name of the virtual environment (in this case, it was venv) can be anything; 
// omitting the name will place the files in the current directory instead.


```
Note!
* ‘venv’ is the general convention used globally. As it is readily available in ignore files (eg: .gitignore’).
* Select Python for gitignore when you make the repository.

```
// To begin using the virtual environment, it needs to be activated:
// Could be different commands
c:\giti2023\flask-storage>venv\Scripts\activate

// Install a lib
(venv) c:\giti2023\flask-storage>pip install flask

```
![Install lib ](https://github.com/spawnmarvel/flask-storage/blob/main/images/install_lib.jpg)
```

// View lib's installed
(venv) c:\giti2023\flask-storage>pip freeze

// Export lib's to requirements file
(venv) c:\giti2023\flask-storage>pip freeze >requirements.txt

// If you are done working in the virtual environment for the moment, you can deactivate it
(venv) c:\giti2023\flask-storage>deactivate

```

## Dependencies

view requirements.txt

Azure Identity client library for Python - version 1.13.0

Authenticate during local development
```
pip install azure-identity
```

![Install Azure account ](https://github.com/spawnmarvel/flask-storage/blob/main/images/install_az_account.jpg)
https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python

## Azure Web APP or container?

Must be bicep and infrastructure deploy and code deploy

* Python/Flask Tutorial for Visual Studio Code
https://github.com/Microsoft/python-sample-vscode-flask-tutorial

* Use CI/CD to deploy a Python web app to Azure App Service on Linux
https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops

## Reason

* Have fun with Python and Azure storage
* Use more Bicep for IAC
* Test web app or container.


~~## Start the app for now~~

```
(venv) c:\giti2023\flask-storage>python app\run.py
 * Serving Flask app 'run'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
Press CTRL+C to quit
```
## Start the app locally and build for Azure Web App

```
# cmd

c:\giti2023\flask-storage>venv\Scripts\activate
(venv) c:\giti2023\flask-storage>cd flaskstazmonitor
(venv) c:\giti2023\flask-storage\flaskstazmonitor>set FLASK_APP=webapp
(venv) c:\giti2023\flask-storage\flaskstazmonitor>set FLASK_ENV=development
(venv) c:\giti2023\flask-storage\flaskstazmonitor>flask run


```

https://github.com/Microsoft/python-sample-vscode-flask-tutorial
