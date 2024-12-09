import cv2
import base64
import socketio
import time

# 创建SocketIO客户端，设置更长的超时时间
sio = socketio.Client(reconnection=True, reconnection_attempts=5, reconnection_delay=1)


def connect_to_server():
    try:
        # 设置更长的连接超时时间
        server_url = 'http://192.168.3.44:5000'
        sio.connect(server_url, wait_timeout=10)
        print(f"已连接到服务器: {server_url}")
        return True
    except Exception as e:
        print(f"连接服务器失败: {str(e)}")
        return False


@sio.event
def connect():
    print('已连接到服务器')


@sio.event
def connect_error(data):
    print('连接错误:', data)


@sio.event
def disconnect():
    print('已断开连接')


def capture_and_send():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("无法读取摄像头数据")
                break

            try:
                # 降低图像质量以减少数据量
                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                jpg_as_base64 = base64.b64encode(buffer).decode()

                # 发送到服务器
                sio.emit('video_frame', jpg_as_base64)

                time.sleep(0.1)  # 降低帧率到10fps，减少网络负载

            except Exception as e:
                print(f"发送数据时出错: {str(e)}")
                break

    except Exception as e:
        print(f"摄像头操作出错: {str(e)}")
    finally:
        cap.release()
        if sio.connected:
            sio.disconnect()


if __name__ == '__main__':
    retry_count = 0
    while retry_count < 5:  # 最多重试5次
        if connect_to_server():
            capture_and_send()
            retry_count = 0  # 重置重试计数
        else:
            retry_count += 1
            print(f"连接失败，第{retry_count}次重试...")
            time.sleep(5)

    print("达到最大重试次数，程序退出")