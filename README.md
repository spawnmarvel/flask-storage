# Azure storage monitoring and more with Flask and Azure SDK

## Flask

https://tedboy.github.io/flask/index.html

## Microsoft Python SDK

https://learn.microsoft.com/en-us/python/api/overview/azure/storage?view=azure-python

* Blobs
* File shares
* File shares Data Lake
* Queues
* Tables

## Azure Web APP or container?


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

// virtualenv venv will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. 
// The name of the virtual environment (in this case, it was venv) can be anything; omitting the name will place the files in the current directory instead.


```
Note
‘venv’ is the general convention used globally. As it is readily available in ignore files (eg: .gitignore’)