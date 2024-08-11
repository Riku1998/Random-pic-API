# 随机图片 API

这是一个使用 Flask 框架构建的简单 API，用于从指定的图片文件夹中随机选择一张图片并将其返回。此项目旨在提供一个简单的图片服务接口，适用于需要动态图片内容的应用程序或测试场景。

## 主要功能

- 从指定的图片文件夹中随机选择一张图片。
- 提供一个固定的 UUID 路径来访问随机图片。
- 自动根据图片文件扩展名猜测 MIME 类型，并返回图片。

## 安装和运行

### 克隆仓库：

```bash
git clone https://github.com/Riku1998/Random-pic-API.git
cd Random-pic-API
```

### 创建虚拟环境并安装依赖：

```bash
python -m venv venv
source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
pip install -r requirements.txt
```


### 配置图片文件夹：

确保在项目根目录下有一个名为 images 的文件夹，并将您的图片放入该文件夹中。

### 运行应用程序：

```bash
python app.py
```

服务器将绑定到 0.0.0.0 的 5000 端口，您可以通过访问 http://localhost:5000/your-uuid/random-image 来获取随机图片。

### 在生产环境中创建系统服务（以 Ubuntu 为例）

#### 安装 gunicorn：

Gunicorn 是一个 Python WSGI HTTP 服务器，用于生产环境中运行 Flask 应用程序。

```bash
pip install gunicorn
```

#### 创建 Gunicorn 服务文件：

创建一个新的系统服务文件 random-pic-api.service。

```bash
sudo nano /etc/systemd/system/random-pic-api.service
```

在文件中添加以下内容：

```ini
[Unit]
Description=Random Picture API
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

替换 /path/to/your/project 和 /path/to/your/venv 为实际的路径。

#### 重新加载系统服务并启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl start random-pic-api
sudo systemctl enable random-pic-api
```

#### 检查服务状态：

```bash
sudo systemctl status random-pic-api
```

## 代码说明

- app.py：主应用程序文件，使用 Flask 框架构建 API。
- /your-uuid/random-image 路径：返回一张随机选择的图片。
- images_folder：指定图片文件夹的路径。
- fixed_uuid：一个固定的 UUID，作为 API 路径的一部分。

## 注意事项

- 请确保在 images 文件夹中有足够的图片文件。
- 如果图片文件夹为空，API 将无法返回图片。
- 在生产环境中，建议使用 Gunicorn 或其他 WSGI 服务器来运行 Flask 应用，并创建系统服务以确保应用程序在服务器重启后自动启动。

## 许可证

本项目使用 MIT 许可证。有关详细信息，请参阅 LICENSE 文件。
```
