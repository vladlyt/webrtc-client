from flask import Flask, render_template, send_from_directory
import os

PORT = os.environ.get('PORT', 5000)
app = Flask(__name__)


# TODO add possibility to mute/stop video
# TODO add rooms per uuid
# TODO show name of the user?

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        directory=os.path.join(app.root_path, 'static'),
        filename='favicon.ico',
        mimetype='image/vnd.microsoft.icon',
    )


if __name__ == '__main__':
    app.run(port=PORT)
