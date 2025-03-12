from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = "Kisegaeningyou-main"
IMAGES_DIR = os.path.join(BASE_DIR, "images")

@app.route('/')
def index():
    images = []
    
    # 遍历 BASE_DIR 下所有 images* 目录
    for root, _, files in os.walk(BASE_DIR):
        if os.path.basename(root).startswith("images"):  # 仅匹配 images 相关文件夹
            for file in files:
                if file.endswith(".png"):
                    image_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
                    text_file = file + ".desc.txt"
                    text_path = os.path.join(root, text_file)
                    text_content = ""

                    if os.path.exists(text_path):
                        with open(text_path, "r", encoding="utf-8") as f:
                            text_content = f.read().strip()

                    images.append({"image": image_path, "text": text_content})

    return render_template("index.html", images=images)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)