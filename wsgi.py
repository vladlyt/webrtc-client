from flask import Flask, render_template, send_from_directory, request
import os

PORT = os.environ.get('PORT', 5000)
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:room_id>/')
def room(room_id: str):
    return render_template('room.html', room_id=room_id, name=request.args.get('name') or 'Incognito')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        directory=os.path.join(app.root_path, 'static'),
        filename='favicon.ico',
        mimetype='image/vnd.microsoft.icon',
    )


if __name__ == '__main__':
    app.run(port=PORT)
