import os, datetime, humanize
from flask import Flask, render_template, send_from_directory, request, jsonify
from auth import auth
app = Flask(__name__)
UPLOAD = 'files'
os.makedirs(UPLOAD, exist_ok=True)
@app.route('/')
@auth.login_required
def index():
    items = []
    for f in os.listdir(UPLOAD):
        path = os.path.join(UPLOAD, f)
        stat = os.stat(path)
        items.append({
            "name": f,
            "size": humanize.naturalsize(stat.st_size),
            "time": datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')
        })
    return render_template('index.html', files=items)
@app.route('/download/<path:name>')
@auth.login_required
def download(name):
    return send_from_directory(UPLOAD, name, as_attachment=True)
@app.route('/upload', methods=['POST'])
@auth.login_required
def upload():
    file = request.files['file']
    if file:
        file.save(os.path.join(UPLOAD, file.filename))
        return jsonify(status='ok')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)