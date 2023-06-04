from flask import Flask, render_template
from . import container_worker as cn
from . import app

@app.route('/')
def index():
    data_dict = get_storage()
    return render_template("index.html", data=data_dict)

@app.route("/about")
def about():
    return render_template("about.html")


def get_storage():
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