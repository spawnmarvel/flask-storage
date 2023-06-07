from flask import Flask, render_template
from . import container_worker as cn
from . import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/container')
def container():
    data_dict = get_container()
    return render_template("container.html", data=data_dict)

def get_container():
    cont_worker = cn.ContainerWorker()
    data_dict = cont_worker.get_container()
    return data_dict


# https://medium.com/reactorlabs/quickly-get-started-with-flask-58201a1f1f61


## Cannot be used for Azure Web app
#if __name__ == '__main__':
#    fs_host = 'localhost'
#    fs_port = 5000
#    fs_debug = True
#    app.run(host=fs_host, port=fs_port, debug=fs_debug)