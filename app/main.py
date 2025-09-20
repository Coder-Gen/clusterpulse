from flask import Flask, request, render_template
from config import Config
from models import db, Log
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join(Config.UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        log = Log(filename=file.filename, path=filepath)
        db.session.add(log)
        db.session.commit()
    logs = Log.query.all()
    return render_template('index.html', logs=logs)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

