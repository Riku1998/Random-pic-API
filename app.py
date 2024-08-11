from flask import Flask, send_file
import random
import os
from mimetypes import guess_type

app = Flask(__name__)

# 图片文件夹路径
images_folder = 'images'
# 获取所有图片路径
images = [os.path.join(images_folder, file) for file in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, file))]

# 假设我们有一个固定的UUID
fixed_uuid = 'your-uuid'

@app.route(f'/{fixed_uuid}/random-image')
def random_image():
    # 随机选择一张图片
    image_path = random.choice(images)
    # 根据文件扩展名猜测mimetype
    mime_type, _ = guess_type(image_path)
    # 如果无法猜测到mimetype，则默认使用'image/jpeg'
    if mime_type is None:
        mime_type = 'image/jpeg'
    # 返回图片
    return send_file(image_path, mimetype=mime_type)

if __name__ == '__main__':
    # 绑定到所有网络接口，并指定端口为5000
    app.run(debug=True, host='0.0.0.0', port=5000)
