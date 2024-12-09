from flask import Flask, render_template
from flask_socketio import SocketIO
import base64
import cv2
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('video_frame')
def handle_video_frame(data):
    # 接收到视频帧后，广播给所有客户端
    socketio.emit('update_frame', data)


if __name__ == '__main__':
    # 指定主机地址和端口
    socketio.run(app, host='0.0.0.0', port=9877, debug=True, allow_unsafe_werkzeug=True)
