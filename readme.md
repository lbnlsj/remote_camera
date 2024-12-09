# 远程视频监控系统

这是一个基于Python的远程视频监控系统，使用Flask和SocketIO实现实时视频传输，支持通过Web浏览器查看实时视频流。

## 功能特点

- 实时视频采集和传输
- 支持移动端适配的Web界面
- 同时支持本地窗口和浏览器查看
- 自动重连机制
- 支持多客户端同时观看
- 低延迟传输

## 系统要求

### 服务端（接收端）
- Python 3.8+
- Ubuntu/Debian系统
- 必要的系统库

### 客户端（发送端）
- Python 3.8+
- Windows/Linux系统
- 可用的摄像头设备

## 安装步骤

1. 安装Python依赖：
```bash
pip install flask flask-socketio python-socketio opencv-python
```

2. 在Ubuntu服务器上安装系统依赖：
```bash
sudo apt-get update
sudo apt-get install -y libgl1-mesa-glx libglib2.0-0
```

3. 创建项目目录结构：
```
remote_camera/
  ├── receive.py      # 服务端程序
  ├── send.py         # 客户端程序
  └── templates/
      └── index.html  # Web界面模板
```

## 使用方法

### 启动服务端
1. 进入项目目录：
```bash
cd remote_camera
```

2. 运行服务端程序：
```bash
python receive.py
```

3. 服务启动后可以：
   - 通过浏览器访问 `http://服务器IP:5000` 查看视频流
   - 在服务器本地查看OpenCV窗口的视频流

### 启动客户端
1. 修改send.py中的服务器地址为你的服务器IP
2. 运行客户端程序：
```bash
python send.py
```

## 配置说明

### 服务端配置（receive.py）
- `host`：服务器IP地址
- `port`：服务端口（默认5000）
- `debug`：调试模式开关

### 客户端配置（send.py）
- `server_url`：服务器地址
- `frame_quality`：视频质量（1-100）
- `frame_rate`：视频帧率
- `resolution`：视频分辨率

## 常见问题

1. 连接问题
   - 检查服务器IP和端口是否正确
   - 确认防火墙是否开放相应端口
   - 验证网络连接是否正常

2. 视频问题
   - 检查摄像头是否正常工作
   - 调整视频质量参数
   - 查看服务器日志获取详细错误信息

3. 系统依赖问题
   - 安装必要的系统库
   - 确保OpenCV正确安装

## 优化建议

1. 性能优化
   - 调整视频压缩参数
   - 根据网络条件调整帧率
   - 选择合适的视频分辨率

2. 网络优化
   - 使用局域网环境
   - 确保网络带宽充足
   - 配置适当的超时时间

## 安全建议

1. 访问控制
   - 添加用户认证
   - 限制访问IP
   - 使用HTTPS加密传输

2. 系统安全
   - 及时更新系统和依赖
   - 定期检查日志
   - 备份重要数据

## 注意事项

1. 请确保有足够的网络带宽
2. 建议在局域网环境中使用
3. 适当调整视频参数以获得最佳效果
4. 定期检查系统运行状态
5. 注意保护隐私和数据安全

## 技术支持

如有问题，请检查：
1. 系统日志
2. 网络连接状态
3. 相关配置是否正确

欢迎提交问题反馈和改进建议。