from flask import Flask

app = Flask(__name__)

@app.route('/')
def entry():
    return 'Entry site'

if __name__ == '__main__':
    fs_host = 'localhost'
    fs_port = 5000
    fs_debug = True

    app.run(host=fs_host, port=fs_port, debug=fs_debug)