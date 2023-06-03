from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = get_storage()
    return render_template("index.html", data=data)

@app.route("/about")
def about():
    return render_template("about.html")


def get_storage():
    return "Storage 0010"

if __name__ == '__main__':
    fs_host = 'localhost'
    fs_port = 5000
    fs_debug = True

    app.run(host=fs_host, port=fs_port, debug=fs_debug)