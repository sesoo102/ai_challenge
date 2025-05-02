from PIL import Image
import os

folder = "data_ssafy_collection_resized"

# 지원하는 이미지 확장자 목록 (대소문자 모두 포함)
image_extensions = (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")

for filename in os.listdir(folder):
    if filename.lower().endswith(image_extensions):
        img_path = os.path.join(folder, filename)
        img = Image.open(img_path).convert("RGB")
        new_filename = os.path.splitext(filename)[0] + ".jpg"
        new_path = os.path.join(folder, new_filename)
        img.save(new_path, quality=95)
        if new_filename != filename:
            os.remove(img_path)
            print(f"변경: {filename} → {new_filename}")

print("확장자 변환 완료!")