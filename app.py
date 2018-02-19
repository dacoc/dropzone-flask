import os
from flask import (
    Flask,
    request,
    render_template,
    send_from_directory,
    url_for,
    jsonify
)
from werkzeug import secure_filename
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        files = request.files.getlist('file')
        for f in files:
            if f:
                filename = secure_filename(f.filename)
                updir = os.path.join(basedir, 'upload/')
                app.logger.info(updir)
                f.save(os.path.join(updir, filename))
                file_size = os.path.getsize(os.path.join(updir, filename))
                myfinalurl = f.final-url
            else:
                app.logger.info('ext name error')
                return jsonify(error='ext name error')
        return jsonify(name=filename, size=file_size, finalurl=myfinalurl)
    else:
        return render_template('upload.html')
